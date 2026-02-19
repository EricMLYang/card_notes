## Question #34 Eric

Topic 1

The data architect has mandated that all tables in the Lakehouse should be configured as **external Delta Lake tables**.

Which approach will ensure that this requirement is met?

A. Whenever a **database** is being created, make sure that the **LOCATION** keyword is used

B. When configuring an external data warehouse for all table storage, leverage Databricks for all ELT.

**C.** Whenever a **table** is being created, make sure that the **LOCATION** keyword is used.

D. When tables are created, make sure that the **EXTERNAL keyword** is used in the CREATE TABLE statement.

E. When the workspace is being configured, make sure that external cloud object storage **has been mounted**.





## Question #35 Eric

Topic 1

To reduce storage and compute costs, the data engineering team has been tasked with curating a series of aggregate tables leveraged by business intelligence dashboards, customer-facing applications, production machine learning models, and ad hoc analytical queries.



The data engineering team has been made aware of new requirements from a customer-facing application, which is the only downstream workload they manage entirely.

As a result, an aggregate table used by numerous teams across the organization will need to have a number of fields renamed, and **additional fields** will also be added.



Which of the solutions addresses the situation while minimally interrupting other teams in the organization without increasing the number of tables that need to be managed?



A. **Send all users notice that the schema for the table will be changing**; include in the communication the logic necessary to revert the new table schema to match historic queries.



**B.** Configure a **new table** with all the requisite fields and new names and use this **as the source for the customer-facing application**; create a view that maintains the original data schema and table name by aliasing select fields from the new table.



C. Create a new table with the required schema and new fields and use Delta Lake's deep clone functionality to sync up changes committed to one table to the corresponding table.



**D**. Replace the current table definition **with a logical view defined with the query logic currently writing the aggregate table**; create a **new table** to power the customer-facing application.



E. **Add a table comment warning all users that the table schema and field names will be changing** on a given date; overwrite the table in place to the specifications of the customer-facing application.





![CleanShot 2025-12-24 at 00.10.32@2x.png](./Question%20#34%20Eric-assets/CleanShot%202025-12-24%20at%2000.10.32@2x.png)







## Question #36 Eric

Topic 1

A Delta Lake table representing metadata about content posts from users has the following schema: user_id LONG, post_text STRING, post_id STRING, longitude FLOAT, latitude FLOAT, post_time TIMESTAMP, date DATE

This table is partitioned by the date column. A query is run with the following filter: longitude < 20 & longitude > -20

Which statement describes how data will be filtered?

A. Statistics in the Delta Log will be used to identify partitions that might include files in the filtered range.

B. No file skipping will occur because the optimizer does not know the relationship between the partition column and the longitude.

C. The Delta Engine will use row-level statistics in the transaction log to identify the files that meet the filter criteria.

**D.** Statistics in the Delta Log will be used to identify data files that might include records in the filtered range.

E. The Delta Engine will scan the parquet file footers to identify each row that meets the filter criteria.









SQL Filter

   ↓

① Partition Pruning（只看 partition column）

   ↓

② File Skipping（Delta Log 的 file-level statistics）

   ↓

③ Row Scan（讀 parquet 檔、逐 row 計算）


