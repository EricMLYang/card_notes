---
tags:
  - data-platform
---
# Azure Data Platform

## \[ Key Tips of Data Platform\]

- What factors need consideration in a framework :  grain of a dataset, scenario, scale, budget, service-level agreement (SLA)

- Single Source of Truth : 

   - supporting multiple data fabrics but there is value in having a “single source of truth”—one storage solution through which all data in the system flows. 

   - it makes it easier to repair data. In many situations, data will need to be fixed. An example of this might be a data issue upstream. Once the issue is identified and corrected, we need to re-ingest the data.

- Optimal processing & Complexity trade-off  : 

   - Hight Complexity  > more data we move around   >  more latency, costs, failure points

   - Low Complexity : EX: just use ADX  >  harder to fit all need ( analysis, pure storage …) 

- Analysis Environment :

   - Separating development and production environments

      - production environment : against which all automation runs

      - development environment :  where our data scientists can experiment

      - If a prototype in development is deemed valuable, it graduates to the production environment (deployed by an SRE)

   - There are several ways to support a development environment for analytics:

      - Provide development data.

      - Replicate the production data.

      - **Provide read-only access to the production data.**

   - Creating an analytics workflow

   - 

      ![image 79.png](./Azure%20Data%20Platform-assets/image%2079.png)

      

      

   - Supporting self-serve data movement

   - 

- 增量載入（Incremental Load）:

- Data Full Load : 

   - 當新的資料進來時，整個舊資料集會被捨棄，並以新資料集取代

   - 適合資料集小、資料經常完全更新、資料間關聯性低、系統對資料一致性要求極高

   - 優：操作簡單明瞭，保證資料集在更新後是最新、最完整的版本，不會有舊資料殘留

   - 缺：大型資料集重新載入整個資料集可能很耗時、耗資源

- Incremental Load

   - 更新時不替換現有資料，而是將新資料附加到現有的資料集中

   - 適合資料變更頻繁、資料量巨大、不需要每次更新整個資料集的情況

   - 優點：能節省時間和資源

   - 缺點：資料集越來越大，對查詢效率造成影響; 如果沒有適當的機制可能導致資料重複或數據不一致此外

- The first trade-off we’ll look at is keeping redundant data around to avoid performing joins versus using multiple tables and joining them together as needed.

- In practice, we usually have one central fact table and several dimension tables around it to represent some aspect of the business.

   ![image 80.png](./Azure%20Data%20Platform-assets/image%2080.png)

   

   ![image 81.png](./Azure%20Data%20Platform-assets/image%2081.png)

## \[ Introduction - Data Engineering \]

- *Data engineering* is the part of data science that deals with the practical applications of collecting and analyzing data. It aims to bring engineering rigor to the process of building and supporting reliable data systems.

- While many data science projects start as exploratory, once these show real value, they need to be supported in an ongoing, reliable fashion.

- Data engineering deals with building and operating big data platforms to support all data science scenarios. There are various other terms used for some of these aspects: 

   - DataOps refers to moving data in a data system

   - MLOps refers to running ML at scale as in our Netflix example (ML combined with DevOps is also known as MLOps.)

   -  Our definition of data engineering encompasses all of these and looks at how we can implement DevOps for data science.

- A key difference between data and code is that code is static: once the bugs are worked out, a piece of code is expected to work consistently and reliably. On the other hand, data moves continuously into and out of a data platform, and it is likely failures will occur due to various external reasons.

- Some of the common themes

   - making sure everything is tracked in source control

   - automatic deployments

   - monitoring  and alerting

   - Data Governance is another major topic that is specific to data: access control, cataloguing, privacy, and regulatory concerns are a big part of a data platform.



## \[ Introduction - Data Platform \]

- A *data platform* is a software solution for collecting, processing, managing, and sharing data for strategic business purposes.

- Anatomy of Data Platform 

   ![image 82.png](./Azure%20Data%20Platform-assets/image%2082.png)

- storage - the backbone of any data platform

- DevOps and what DevOps means for data.

- Orchestration layer : Data is ingested into the system from multiple sources. Data flows into and out of the platform, and various workflows are executed. All of this needs an orchestration layer to keep things running. 

- 3 main workloads that a data platform must support

   - Processing**—**Encompasses aggregating and reshaping the data, standardizing schema, and any other processing of the raw input data. This makes the data easier to consume by the other two main processes: analytics and machine learning.

   - Analytics—Covers all data analysis and reporting, thereby deriving knowledge and insights on the data.

   - Machine learning—Includes all ML models training on the data.

- Data Governance :  is the process of managing the availability, usability, integrity, regulatory compliance, and security of the data in a data system. Effective data governance ensures that data is consistent and trustworthy and doesn't get misused.

   - Metadata : Cataloguing and inventorying the data, tracking lineage, definitions, and documentation

   - Data quality - How to test data and assess its quality is the topic of chapter 9.

   - Compliance - Honoring compliance requirements like the General Data Protection Regulation (GDPR), handling sensitive data, and controlling access is covered in chapter 10

![image 83.png](./Azure%20Data%20Platform-assets/image%2083.png)



## \[ Storage \]

- Definition: - Data Fabric

   - A *data fabric* is an environment for storing and managing data. 

   - From a consumer perspective, it represents a single storage technology—the “fabric” on which the data persists. 

   - Examples of data fabrics in Azure are SQL, Azure Data Explorer, Blob Storage, and so forth.

- A large data platform needs to accommodate heterogenous data storage. By *heterogenous data storage*, we mean data spread across multiple data fabrics.

### Data Fabric

- **Azure Data Explorer** 

   - excels at querying millions of rows in a matter of seconds

   - identifies anomalies or produces aggregates

   -  high-performance indexing and caching capabilities

- Azure Data Lake Storage:

   - keep a large amount of data for historical reasons or simply to allow other teams within our enterprise to copy the data to their systems 

   - cheap storage

- Cosmos DB

   - Azure globally distributed NoSQL solution

   - provides turnkey *geo-replication* (meaning data can be replicated across different worldwide data centers with a simple configuration change)

   - retrieves one particular document in milliseconds

   - This makes it ideal as a storage layer behind a data API

- Azure Stream Analytics can perform real-time analysis on streaming data

- Azure Databricks can run big data analytics on top of Azure Data Lake Storage

### 

## \[ Data Platform DevOps \]

- Target : tracking everything in source control and deploying everything automatically

- we will talk about DevOps and how it became an industry standard for software engineering. We’ll see what learning we can take from that and apply it to the world of data and data platforms. We’ll explore Azure DevOps, the Azure offering in the DevOps space, which provides an integrated, one-stop-shop service for all our needs.

![image 84.png](./Azure%20Data%20Platform-assets/image%2084.png)

### What is DevOps

- Definition **:** A DevOps *team* owns their solution end to end, from requirements gathering and design through development and testing to deployment, monitoring, and fixing production issues.

- DevOps lets software engineers take charge of the end-to-end process.

- Two major shifts :

   - broad adoption of agile software development practices, which aim to optimize the time it takes for software delivery, from requirements to production

   - the move to the cloud created a renewed focus on automation for deployment and configuration, which is an invaluable tool in the DevOps toolbox

- Some of the key software tools that enable DevOps follow:

   - *Source code management* : Includes source control, code navigation and search, and code review tools

   - *Build automation* : An environment to host and execute builds for continuous integration, test execution, and status

   - *Packaging* : Facilitates versioning and packaging build artifacts

   - *Release automation* : Pipelines for deploying services to various environments (preproduction, production), either continuously (continuous delivery), on some schedule, or on demand

   - *Monitoring* *and alerting* : Tools to collect telemetry from running services and, in case of failure detection, to alert owners of a potential outage





## Azure Service

- Azure Event Hub is a service that can receive and process millions of events per second. An event contains some data payload sent by the client to the event hub.

- Azure Data Factory is Azure’s cloud ETL (extract, transform, load) service for scale-out serverless data integration and data transformation


