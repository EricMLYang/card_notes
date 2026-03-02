---
tags:
  - system-design
---
# Dependable and Adaptable Systems Standards

## \[ Intorduction \]

- 5 High : Performance, Scalability, High Availability, *Reliability, Maintainability*

- Reliability:

   - The system should continue to work *correctly* (performing the correct function at the desired level of performance) even in the face of *adversity* (hardware or software faults, and even human error)

- Performance: 

   - a system's ability to process tasks and respond to requests quickly and efficiently. This can be measured in various ways such as :  Throughput, 

      Latency,  Response time

- Availability:

   - a system's ability to remain operational and accessible with minimal downtime, even in the face of failures. This is often achieved through redundancy and fault tolerance mechanisms,

- Scalability:

   - As the system *grows* (in data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth.

- Maintainability:

   - Over time, many different people will work on the system (engineering and operations, both maintaining current behavior and adapting the system to new use cases), and they should all be able to work on it *productively*



## \[ Performance \]

### Relationship DB

- Read-Write Splitting

   - 讀寫分離架構不複雜，但需要處理複製延遲帶來的複雜性

- Database Sharding & Partitioning



### Cache 

- Data that through complex calculated

-   Read   >>>  Write

### Column-based storage

- Fit to Big Data Analysis Scenarios

- Parquet

   - a column-based storage format

   - Databricks use Parquet as a ACID information layer in Delta Lake

   - 


