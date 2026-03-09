Chapter 3. Joins (SQL and Core)
A Note for Early Release Readers
With Early Release ebooks, you get books in their earliest form—the author’s raw and unedited content as they write—so you can take advantage of these technologies long before the official release of these titles.

This will be the 6th chapter of the final book. Please note that the GitHub repo is available at https://github.com/high-performance-spark/high-performance-spark-examples.

If you have comments about how we might improve the content and/or examples in this book, or if you notice missing material within this chapter, please reach out to the editor at sevans@oreilly.com.

Joining data is an important part of many of our pipelines, and both Spark Core and SQL support the same fundamental types of joins. While Core and SQL support the same types they have very different execution options and performance. While joins are very common and powerful, they warrant special performance consideration as they may require large network transfers or even create datasets beyond our capability to handle.1 In core Spark it can be more important to think about the ordering of operations, since the DAG optimizer, unlike the SQL optimizer, isn’t able to re-order or push down filters.

To understand the performance of joins in Spark it’s important to distinguish two similar-sounding concepts, join types and join execution techniques. Join types impact the result and are things like left and right inner joins, outer joins, full-self-joins, etc. Join execution techniques refer to how the engine, Spark, computes the result and can be things like broadcast, hash, sort, and so on. The join type, as well as the data sizes, conditions, configuration, and hints, all influence what join technique Spark chooses.

Core Spark Joins
In this section, we will go over the RDD-type joins. Joins, in general, are expensive since they require that corresponding keys from each RDD are located on the same machine so that they can be combined locally. If the RDDs do not have known partitioners, they must be shuffled so that both RDDs share a partitioner,1 and data with the same keys lives in the same partitions, as shown in Figure 3-1. If they have the same partitioner, data may still need to be transferred but not shuffled.

The partitioning, and if Spark is aware of it, of your data has a large impact on joins. If the RDDs you are joining have the same known partitioners, their can be narrow dependencies on both RDDs, as in Figure 3-4. If there is one known and one unknown, or they have different known partioners2 there will be a narrow dependency on one RDD and a shuffle/wide dependency on the other, as in Figure 3-2. In the best case with the same partioner materialized in the same operation the data may be colocated, as in Figure 3-3, so as to avoid network transfer entirely.

As with most key/value operations, the cost of the join increases with the number of keys and the distance the records have to travel in order to get to their correct partition.

0601
Figure 3-1. Shuffle join
0602
Figure 3-2. One known partitioner join
0603
Figure 3-3. Colocated join
Tip
Two RDDs are colocated if they have the same partitioner and are shuffled as part of the same action.

Tip
Core Spark joins are implemented using the cogroup function. We discuss cogroup in “Co-Grouping”.

Choosing a Join Type
The default join operation in Spark includes only values for keys present in both RDDs, and in the case of multiple values per key, provides all permutations of the key/value pair. The best scenario for a standard join is when both RDDs contain the same set of distinct keys. With duplicate keys, the size of the data may expand dramatically causing performance issues, and if one key is not present in both RDDs you will lose that row of data. Here are a few guidelines:

When both RDDs have duplicate keys, the join can cause the size of the data to expand dramatically. It may be better to perform a distinct or combineByKey operation to reduce the key space or to use cogroup to handle duplicate keys instead of producing the full cross product. By using smart partitioning during the combine step, it is possible to prevent a second shuffle in the join (we will discuss this in detail later).

If keys are not present in both RDDs you risk losing your data unexpectedly. It can be safer to use an outer join, so that you are guaranteed to keep all the data in either the left or the right RDD, then filter the data after the join.

If one RDD has some easy-to-define subset of the keys, you may be better off filtering or reducing the second RDD before the join to reduce the size of shuffle data, which you will ultimately throw away anyway.

Tip
Join is one of the most expensive operations you will commonly use in Spark, so it is worth doing what you can to shrink your data before performing a join.

For example, suppose you have one RDD with some data in the form (Panda id, score) and another RDD with (Panda id, address), and you want to send each panda some mail with her best score. You could join the RDDs on id and then compute the best score for each address, as shown in Example 3-1.

Example 3-1. Basic RDD join
  def joinScoresWithAddress1( scoreRDD : RDD[(Long, Double)],
   addressRDD : RDD[(Long, String )]) : RDD[(Long, (Double, String))]= {
    val joinedRDD = scoreRDD.join(addressRDD)
    joinedRDD.reduceByKey( (x, y) => if(x._1 > y._1) x else y )
  }
However, this is not as fast as first reducing the score data, so that the first dataset contains only one row for each panda with her best score, and then joining that data with the address data (as shown in Example 3-2).

Example 3-2. Pre-filter before join
  def joinScoresWithAddress2(scoreRDD : RDD[(Long, Double)],
    addressRDD: RDD[(Long, String)]) : RDD[(Long, (Double, String))]= {
   val bestScoreData = scoreRDD.reduceByKey((x, y) => if(x > y) x else y)
   bestScoreData.join(addressRDD)
  }
If each Panda had 1,000 different scores then the size of the shuffle we did in the first approach was 1,000 times the size of the shuffle we did with this approach!

If we wanted to we could also perform a left outer join to keep all keys for processing even those missing in the right RDD by using leftOuterJoin in place of join, as in Example 3-3. Spark also has fullOuterJoin and rightOuterJoin depending on which records we wish to keep. Any missing values are None and present values are Some('x').

Example 3-3. Basic RDD left outer join
  def outerJoinScoresWithAddress(scoreRDD : RDD[(Long, Double)],
   addressRDD: RDD[(Long, String)]) : RDD[(Long, (Double, Option[String]))]= {
    val joinedRDD = scoreRDD.leftOuterJoin(addressRDD)
    joinedRDD.reduceByKey( (x, y) => if(x._1 > y._1) x else y )
  }
Choosing an Execution Plan
In order to join data, Spark needs the data that is to be joined (i.e., the data based on each key) to live on the same machine. The default implementation of a join in Spark is a shuffled hash join. The shuffled hash join ensures that data on each partition will contain the same keys by partitioning the second dataset with the same partitioner as the first, so that the keys with the same hash value from both datasets are in the same partition. While this approach always works, it can be more expensive than necessary because it requires a shuffle. The shuffle can be avoided if:

Both RDDs share a known partitioner.

One of the datasets is small enough to fit in memory, in which case we can do a broadcast hash join (we will explain what this is later).

Note that if the RDDs are colocated, the network transfer can be avoided, along with the shuffle.

Speeding up joins by assigning a known partitioner
If you have to do an operation before the join that requires a shuffle, such as aggregateByKey or reduceByKey, you can prevent the joins shuffle by adding a hash partitioner with the same number of partitions as an explicit argument to the first operation before the join. You could make the example in the previous section even faster, by using the partitioner for the address data as an argument for the reduceByKey step, as in Example 3-4 and Figure 3-4.

Example 3-4. Known partitioner join
  def joinScoresWithAddress3(scoreRDD: RDD[(Long, Double)],
   addressRDD: RDD[(Long, String)]) : RDD[(Long, (Double, String))]= {
    // If addressRDD has a known partitioner we should use that,
    // otherwise it has a default hash parttioner, which we can reconstruct by
    // getting the number of partitions.
    val addressDataPartitioner = addressRDD.partitioner match {
      case (Some(p)) => p
      case (None) => new HashPartitioner(addressRDD.partitions.length)
    }
    val bestScoreData = scoreRDD.reduceByKey(addressDataPartitioner,
      (x, y) => if(x > y) x else y)
    bestScoreData.join(addressRDD)
  }
Tip
If the RDDs sharing the same partitioner are materialized by the same action, they will end up being co-located (which can even reduce network traffic). One way to do this is by unioning them and calling count()

0604
Figure 3-4. Co-Partioned but not Co-Located
Speeding up joins using a broadcast hash join
A broadcast hash join collects all of the data from the smaller RDD onto the driver and then pushes a copy to each worker node. Then it does a map-side combine with each partition of the larger RDD. If one of your RDDs can fit in memory or can be made to fit in memory it is always beneficial to do a broadcast hash join, since it doesn’t require a shuffle. This is illustrated in Figure 3-5.

0604
Figure 3-5. Broadcast hash join
Spark Core does not have an implementation of the broadcast hash join. Instead, we can manually implement a version of the broadcast hash join by collecting the smaller RDD to the driver as a map, then broadcasting the result, and using mapPartitions to combine the elements.

Example 3-5 is a general function that could be used to join a larger and smaller RDD. Its behavior mirrors the default “join” operation in Spark. We exclude elements whose keys do not appear in both RDDs.

Example 3-5. Known partitioner join
 def manualBroadcastHashJoin[K : Ordering : ClassTag, V1 : ClassTag,
 V2 : ClassTag](bigRDD : RDD[(K, V1)],
  smallRDD : RDD[(K, V2)])= {
  val smallRDDLocal: Map[K, V2] = smallRDD.collectAsMap()
  val smallRDDLocalBcast = bigRDD.sparkContext.broadcast(smallRDDLocal)
  bigRDD.mapPartitions(iter => {
   iter.flatMap{
    case (k,v1 ) =>
     smallRDDLocalBcast.value.get(k) match {
      // Note: You could switch this to a left join by changing the empty seq
      // to instead return Seq(k, Seq.empty[(V1, V2)])
      case None => Seq.empty[(K, (V1, V2))]
      case Some(v2) => Seq((k, (v1, v2)))
     }
   }
  }, preservesPartitioning = true)
 }
Partial manual broadcast hash join
Sometimes not all of our smaller RDD will fit into memory, but some keys are so overrepresented in the large dataset that you want to broadcast just the most common keys. This is especially useful if one key is so large that it can’t fit on a single partition. In this case you can use countByKeyApprox2 on the large RDD to get an approximate idea of which keys would most benefit from a broadcast. You then filter the smaller RDD for only these keys, collecting the result locally in a HashMap. Using sc.broadcast you can broadcast the HashMap so that each worker only has one copy and manually perform the join against the HashMap. Using the same HashMap you can then filter your large RDD down to not include the large number of duplicate keys and perform your standard join, unioning it with the result of your manual join. This approach is quite convoluted but may allow you to handle highly skewed data you couldn’t otherwise process.

Spark SQL Joins
Spark SQL supports the same basic join types as core Spark, but the optimizer can do more of the heavy lifting for you—​although you also give up some of your control. For example, Spark SQL can sometimes push down or reorder operations to make your joins more efficient. On the other hand, you don’t control the partitioner for the RDDs making up the DataFrames or Datasets, so you can’t manually avoid shuffles as you did with core Spark joins.

DataFrame Joins
Joining data between DataFrames is one of the most common multi-DataFrame transformations. The standard SQL join types are all supported and can be specified as the joinType in df.join(otherDf, sqlCondition, joinType) when performing a join. As with joins between RDDs, joining with nonunique keys will result in the cross product (so if the left table has R1 and R2 with key1 and the right table has R3 and R5 with key1 you will get (R1, R3), (R1, R5), (R2, R3), (R2, R5)) in the output. While we explore Spark SQL joins we will use two example tables of pandas, Table 3-1 and Table 3-2.

Once we’ve covered the kinds of joins you can do with DataFrames / Spark SQL, we’ll look at the different ways these joins can be executed, their performance characteristics, and how the Spark SQL optimizer chooses the join type. While some of these are similar to the RDD joins discussed above there are important differences and new options for join execution.

Warning
While self-joins are supported, you must first alias the relevant fields to distinct names to access them.

Table 3-1. Table of pandas and sizes (our left DataFrame)
Name	Same
Happy

1.0

Sad

0.9

Happy

1.5

Coffee

3.0

Table 3-2. Table of pandas and zip codes (our right DataFrame)
Name	Zip
Happy

94110

Happy

94103

Coffee

10504

Tea

07012

Spark’s supported join types are “inner,” “left_outer” (aliased as “outer”), “left_anti,” “right_outer,” “full_outer,” and “left_semi.”3 With the exception of “left_semi” these join types all join the two tables, but they behave differently when handling rows that do not have keys in both tables.

The “inner” join is both the default and likely what you think of when you think of joining tables. It requires that the key be present in both tables, or the result is dropped as shown in Example 3-6 and Table 3-3.

Example 3-6. Simple inner join
    // Inner join implicit
    df1.join(df2, df1("name") === df2("name"))
    // Inner join explicit
    df1.join(df2, df1("name") === df2("name"), "inner")
Table 3-3. Inner join of df1, df2 on name
Name	Size	Name	Zip
Happy

3.0

Coffee

10504

Happy

1.5

Happy

94110

Happy

1.5

Happy

94103

Happy

1.0

Happy

94110

Happy

1.0

Happy

94103

Left outer joins will produce a table with all of the keys from the left table, and any rows without matching keys in the right table will have null values in the fields that would be populated by the right table. Right outer joins are the same, but with the requirements reversed. A sample left outer join is in Example 3-7, and the result is shown in Table 3-4.

Example 3-7. Left outer join
    // Left outer join explicit
    df1.join(df2, df1("name") === df2("name"), "left_outer")
Table 3-4. Left outer join df1, df2 on name
Name	Size	Name	Zip
Sad

0.9

null

null

Coffee

3.0

Coffee

10504

Happy

1.0

Happy

94110

Happy

1.0

Happy

94103

Happy

1.5

Happy

94110

Happy

1.5

Happy

94103

A sample right outer join is in Example 3-8, and the result is shown in Table 3-5.

Example 3-8. Right outer join
    // Right outer join explicit
    df1.join(df2, df1("name") === df2("name"), "right_outer")
Table 3-5. Right outer join df1, df2 on name
Name	Size	Name	Zip
Coffee

3.0

Coffee

10504

Happy

1.0

Happy

94110

Happy

1.0

Happy

94103

Happy

1.5

Happy

94110

Happy

1.5

Happy

94103

null

null

Tea

07012

To keep all records from both tables you can use the full outer join, which results in Table 3-6.

Table 3-6. Full outer join df1, df2 on name
Name	Size	Name	Zip
Sad

0.9

null

null

Coffee

3.0

Coffee

10504

Happy

1.0

Happy

94110

Happy

1.0

Happy

94103

Happy

1.5

Happy

94110

Happy

1.5

Happy

94103

null

null

Tea

07012

Left semi joins (as in Example 3-9 and Table 3-7) and left anti joins (as in Table 3-8) are the only kinds of joins that only have values from the left table. A left semi join is the same as filtering the left table for only rows with keys present in the right table. The left anti join also only returns data from the left table, but instead only returns records that are not present in the right table.

Example 3-9. Left semi join
    // Left semi join explicit
    df1.join(df2, df1("name") === df2("name"), "left_semi")
Table 3-7. Left semi join
Name	Size
Coffee

3.0

Happy

1.0

Happy

1.5

Table 3-8. Left anti join
Name	Size
Sad

0.9

Self joins
Self-joins are supported on DataFrames, but we end up with duplicate column names. So that you can access the results, you need to alias the DataFrames to different names—otherwise, you will be unable to select the columns due to name collision (see Example 3-10). Once you’ve aliased each DataFrame, in the result, you can access the individual columns for each DataFrame with dfName.colName.

Example 3-10. Self join
    val joined = df.as("a").join(df.as("b")).where($"a.name" === $"b.name")
Cross / Cartesian Joins
Cross joins are a special case which are even more likely to create large results. Every row in the first dataframe is joined with every row in the second dataframe which can quickly blow up the results. Cross joins are best used when one of the two DataFrames is small, like a list of provinces.

Complex Join Conditions
Efficient joins in Spark depend on Spark’s (re-)partitioning the data so that equality can be computed between two partitions. Certain functions (e.g a UDF, regexes, >=, etc.) will work as join conditions but force something similar to cartesian joins. This is because there is no static way for Spark to ensure the matching data is in the same partitions. Joins with an equality condition are sometimes called “equi-joins” and others are called “non-equi-joins.”

Understanding equi-joins can be a bit confusing since not all UDF usage in a join function results in this fall-back. If the core join condition is still a “simple” operation performed on the results of complex operations, like equality on UDF results, Spark can still perform it’s regular join. It’s simplest to see with two example uses of UDFS for joins, one “cheap” and one expensive.

Example 3-11. Bad Complex / UDF Join – Forces All-To-All Comparison
  def badJoin(df1: Dataset[Pandas], df2: Dataset[Pandas]): Dataset[(Pandas, Pandas)] = {
    val session = df1.sparkSession
    val sle = session.udf.register("strLenEq", (s: String, s2: String) => s.length() == s2.length())
    df1.joinWith(df2, sle(df1("name"), df2("name"))).alias("strlenEqJoin")
  }
When possible, instead of the above, separate out your equality checking and write your UDF to return the per-value results as below.

Example 3-12. Safe Join with UDFs – follows regular join operations
  def okJoin(df1: Dataset[Pandas], df2: Dataset[Pandas]): Dataset[(Pandas, Pandas)] = {
    val session = df1.sparkSession
    val sl = session.udf.register("strLen", (s: String) => s.length())
    df1.joinWith(df2, sl(df1("name")) === sl(df2("name"))).alias("strlenJoin")
  }
While intuitively, all to all comparisons are more expensive, the next section will look at the different join execution operators’ performance in more detail.

Concrete SQL Join Execution Operators
Spark SQL has a few key join execution techniques for different data sizes, skews, join conditions and join types. Understanding the join techniques and their trade-offs is useful so you can provide correct join hints when necessary and structure your code to support the desired join technique.

The core Spark SQL join techniques are Broadcast Hash Join, Broadcast Nested Loop, Shuffle-Hash, Shuffle-Sort-Merge, and Shuffle and Replicate Nested Loop. A brief summary table is shown below and we’ll dive into each in more detail.

Table 3-9. Summary table
Join name	Join Types	Join Conditions	Input Partitioninga	Output Partitioning	Performance	Narrow or Wide
Broadcast Hash

All except full outer

equi-join

Any

Same as larger dataframe

Fast when one DataFrame is small

Narrow (non-broadcast)

Broadcast Nested Loop

All

equi & non-equi

Any

Often same as larger

Depends on one DataFrame being small & being able to do minimal passes

Narrow (non-broadcast)

Shuffle and Replicate (also known as Cartesian)

Inner & Cartesian

equi-join

Any

Undefined

High chance of data explosion

Narrow

Shuffle Hash

All

equi-join

No skew: Any, skew: Clustered

Depends on join type

Requires High Cardinality

Wide

Shuffle Sort Merge

All

equi-join on sortable

No skew: Any, skew: Clustered

Depends on join type

Requires High Cardinality, less likely to OOM

Wide

a Spark will automatically insert a shuffle if needed to match the desired input partioning.

Broadcast Hash avoids shuffling and is immensely performant if one of the two Dataframes is small enough. They support all join types except for full-outer joins. Broadcast joins require equi-joins, although the similar broadcast nested loop join supports non-equi-joins. Broadcast joins are most often selected by spark.sql.autoBroadcastJoinThreshold, which has a default value of ~10mb. The output partitioning is the same as the input partitioning of the non-broadcasted Dataframe. While they can be performant when used correctly, they can also often cause too large task result errors and out-of-memory issues when the broadcast data frame is too large. Since this is such a high performance operation, when possible Spark will use this strategy.

Broadcast nested loop joins are similar to broadcast hash joins but with fewer restrictions. The nested loop does not refer to iteratively broadcasting parts of the dataset; instead, it refers to iterating over the dataset multiple times to compute the join conditions. They support all join types and both equi and non-equi join conditions. As with broadcast join, there is a chance of out-of-memory errors when the broadcast data frame is too large. It also performs poorly when multiple iterations are required to compute the join. The ideal cases, with single iterations over the datasets, are left broadcast w/ right outer join, right broadcast with left outer, left semi, left anti, or existence join, and either side broadcasted in an inner-join. Because this join is more likely to be slow or OOM, it is normally only created as a last resort.

Shuffle and replicate joins, also known as cartesian product joins, are the most likely to cause an explosion in terms of data size. They are implemented by computing each partition with every other partition. For inner joins, the result is filtered on the join condition, which is pipelined as part of the evaluation. Uniquely, shuffle and replicate joins have the advantage of creating comparatively narrow dependencies where each output partition depends only on one partition from each of its parents.

The next two shuffle based joins, shuffle hash and shuffle sort, joins are similar to the RDD based joins discussed earlier in this chapter.

Shuffle Hash joins are one of Spark’s earliest forms and offer reasonable performance in many cases. It supports the majority of join conditions and data types and has fairly reasonable performance. Shuffle Hash joins require that one of the two RDDs have partitions that are small enough to create a hash map of the keys.

Shuffle sort joins are very similar to shuffle hash joins but use sorting instead of hashing. It requires that the key you are joining on are sortable, which the majority of primitive types are. Complex types, like maps, however are not sortable.

On top of the core join techniques, Spark AQE adds an optimized skew join, which, while not exactly another join technique, splits large partitions in shuffle sort & hash-based joins. Spark’s AQE can also add additional join hints dynamically to suggest a better strategy using runtime data size statistics.

Broadcast hash joins
In Spark SQL you can see the type of join being performed by calling queryExecution.executedPlan. As with core Spark, if one of the tables is much smaller than the other you may want a broadcast hash join. You can hint to Spark SQL that a given DF should be broadcast for join by calling broadcast on the DataFrame before joining it (e.g., df1.join(broadcast(df2), "key")). Spark also automatically uses the spark.sql.conf.autoBroadcastJoinThreshold to determine if a table should be broadcast.

Using Join Hints
Join hints can help Spark choose the “correct” sorting operation, broadcast the desired side of a join, or target a specific output partitioning. You can specify these hints with /* [name of hint], [next hint], etc */ in SQL.

Dataset Joins
You can also join Datasets with joinWith and this behaves similarly to a regular relational join, except the result is a tuple of the different record types as shown in Example 3-13. This is somewhat more awkward to work with after the join, but also does make self joins, as shown in Example 3-14, much easier, as you don’t need to alias the columns first.

Example 3-13. Joining two Datasets
    val result: Dataset[(RawPanda, CoffeeShop)] = pandas.joinWith(coffeeShops,
      $"zip" === $"zip")
Example 3-14. Self join a Dataset
    val result: Dataset[(RawPanda, RawPanda)] = pandas.joinWith(pandas,
      $"zip" === $"zip")
Note
Using a self join and a lit(true), you can produce the cartesian product of your Dataset, which can be useful but also illustrates how joins (especially self joins) can easily result in unworkable data sizes.

As with DataFrames you can specify the type of join desired (e.g., inner, left_outer, right_outer, left_semi), changing how records present only in one Dataset are handled. Missing records are represented by null values, so be careful.

Conclusion
Now that you have explored joins, it’s time to focus on transformations and their associated performance considerations.

As the saying goes, the cross product of big data and big data is an out-of-memory exception.

If the number of distinct keys is too high, you can also use reduceByKey, sort on the value, and take the top k.

The quotes are optional and can be left out. We use them in our examples because we think it is easier to read with the quotes present.

1 Except for broadcast joins.

2 Spark picks the partitioner with the highest number of partitions regardless of the actual amount of data. Alternatively you can specify which partioner to choose as part of the join.