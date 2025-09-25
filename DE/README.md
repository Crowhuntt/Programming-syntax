# Data Engineering Lifecycle and Terminology

Master data: Master data is data about business entities such as employees, customers, products, and locations. As organizations grow larger and more complex through organic growth and acquisitions, and collaborate with other businesses, maintaining a consis‐ tent picture of entities and identities becomes more and more challenging.

Golden Records: Master data management (MDM) is the practice of building consistent entity defi‐ nitions known as golden records. Golden records harmonize entity data across an organization and with its partners. For example, an MDM team might determine a standard format for addresses, and then work with data engineers to build an API to return consistent addresses and a system that uses address data to match customer records across company divisions.

## Source Systems

**API**:  Application programming interfaces (APIs) are a standard way of exchanging data between systems. In theory, APIs simplify the data ingestion task for data engineers. In practice, many APIs still expose a good deal of data complexity for engineers to manage.

**CDC (Change Data Capture)**: Is a method for extracting each change event (insert, update, delete) that occurs in a database. CDC is frequently leveraged to replicate between databases in near real time or create an event stream for downstream processing.

**ACID**: Atomicity, consistency, isolation, durability.

**OLTP**: Online transactional processing. OLTP databases support low latency and high concurrency. An RDBMS (Relational Database Management System) database can select or update a row in less than a millisecond (not account‐ ing for network latency) and handle thousands of reads and writes per second

**OLAP**: An Online analytical processing (OLAP) system is built to run large analytics queries and is typically inefficient at handling lookups of individual records.

**CRUD**:  Stands for create, read, update, and delete. Is a transactional pattern commonly used in programming and represents the four basic operations of persistent storage. CRUD is the most common pattern for storing application state in a database.

**Insert-Only**:  The insert-only pattern retains history directly in a table containing data. Rather than updating records, new records get inserted with a timestamp indicating when they were created.  With the insert-only pattern, a new address record is inserted with the same customer ID. To read the current customer address by customer ID, you would look up the latest record under that ID. In a sense, the insert-only pattern maintains a database log directly in the table itself.

## Storage

**Serialization**:  Serialization is the process of flattening and packing data into a standard format that a reader will be able to decode. Serialization formats provide a standard of data exchange. We might encode data in a rowbased manner as an XML, JSON, or CSV file and pass it to another user who can then decode it using a standard library.
- **Row-based serialization**: As its name suggests, row-based serialization organizes data by row. CSV format is an archetypal row-based format.
  - **CSV**: Data engineers should avoid using CSV files in pipelines because they are highly error-prone and deliver poor performance.
  - **XML**: It is now viewed as legacy; it is generally slow to deserialize and serialize for data engineering applications.
  - **JSON / JSONL**: Has emerged as the new standard for data exchange over APIs, and it has also become an extremely popular format for data storage. JSON Lines (JSONL) is a specialized version of JSON for storing bulk semistructured data in files. JSONL stores a sequence of JSON objects, with objects delimited by line breaks.
  - **Avro**: Avro encodes data into a binary format, with schema metadata specified in JSON. Avro is popular in the Hadoop ecosystem and is also supported by various cloud data tools.
- **Columnar serialization**: With columnar serialization, data organization is essentially pivoted by storing each column into its own set of files. One obvious advantage to columnar storage is that it allows us to read data from only a subset of fields rather than having to read full rows at once. Columnar databases are a terrible fit for transactional workloads, so transactional databases generally utilize some form of row- or record-oriented storage.
  - **Parquet**:  Parquet stores data in a columnar format and is designed to realize excellent read and write performance in a data lake environment.
  - **ORC**: Optimized Row Columnar (ORC) is a columnar storage format similar to Parquet. ORC was very popular for use with Apache Hive. Less used.
  - **Apache Arrow or in-memory serialization**: The idea of Apache Arrow is to rethink serialization by utilizing a binary data format that is suitable for both in-memory processing and export.
- **Hybrid serialization**:  We use the term hybrid serialization to refer to technologies that combine multiple serialization techniques or integrate serialization with additional abstraction layers, such as schema management.
  - **Apache Hudi**: Hudi stands for Hadoop Update Delete Incremental. This table management technology combines multiple serialization techniques to allow columnar database performance for analytics queries while also supporting atomic, transactional updates.
  - **Apache Iceberg**: Iceberg is a table management technology. Iceberg can track all files that make up a table. It can also track files in each table snapshot over time, allowing table time travel in a data lake environment.

**Compression**: Compression makes data smaller and takes less space on the disk. Compression increases the practical scan speed per disk. With a 10:1 compression ratio, we go from scanning 200 MB/s per magnetic disk to an effective rate of 2 GB/s per disk. Network performance, given that a network connection provides 10 gigabits per second (Gbps) of bandwidth, a 10:1 compression ratio increases effective network bandwidth to 100 Gbps..
- Lossless compression: Note that we’re talking about lossless compression algorithms. Decompressing data encoded with a lossless algorithm recovers a bit-for-bit exact copy of the original data.  
- Lossy compression: Audio, images, and video aim for sensory fidel‐ ity; decompression recovers something that sounds like or looks like the original but is not an exact copy. Data engineers might deal with lossy compression algorithms in media processing pipelines but not in serialization for analytics, where exact data fidelity is required.

**Eventual Consistency**: ACID != BASE (basically available, soft-state, eventual consistency).  If you want to scale horizontally (across multiple nodes) to process data in high volumes, then eventually, consistency is often the price you’ll pay. Eventual consistency allows you to retrieve data quickly without verifying that you have the latest version across all nodes.

**Strong Consistency**: With strong consistency, the distributed database ensures that writes to any node are first distributed with a consensus and that any reads against the database return consistent values. You’ll use strong consistency when you can tolerate higher query latency and require correct data every time you read from the database.   

**Indexes**: Indexes provide a map of the table for particular fields and allow extremely fast lookup of individual records. Without indexes, a database would need to scan an entire table to find the records satisfying a WHERE condition.

**Partitioning**: We can partition a table into multiple subtables by splitting it on a field. It is quite common in analytics and data science use cases to scan over a time range, so date- and time-based partitioning is extremely common.

**Clustering**: Clusters allow finer-grained organization of data within partitions. A clustering scheme applied within a columnar database sorts data by one or a few fields, colocat‐ ing similar values. This improves performance for filtering, sorting, and joining these values.

**Data Catalog**: A data catalog is a software application that creates an inventory of an organization's data assets to help data professionals and business users find relevant data for analytics uses. Data catalogs are driven by metadata, the descriptive data about data that's used to create the data inventory. Data catalogs have both organizational and technical use cases. Data catalogs make metadata easily available to systems. For instance, a data catalog is a key ingredient of the data lakehouse, allowing table discoverability for queries.

**Schema on write**: Is essentially the traditional data warehouse pattern: a table has an integrated schema; any writes to the table must conform. To support schema on write, a data lake must integrate a schema metastore. The principal advantage of schema on write is that it enforces data standards, making data easier to consume and utilize in the future.

**Schema on read**: The schema is dynamically created when data is written, and a reader must determine the schema when reading the data. Ideally, schema on read is implemented using file formats that implement built-in schema information, such as Parquet or JSON. CSV files are notorious for schema inconsistency and are not recommended in this setting. Schema on read emphasizes flexibility, allowing virtually any data to be written. This comes at the cost of greater difficulty consuming data in the future.  

**Hot / Warm / Cold - Data Access Frequency**: Hot is accessed very frequently, it has a high storage cost (memory / SSD) but low retrieval cost (instant or frequent access requirements). Warm has infrequent access, medium storage cost (HDD) and medium retrieval cost. Cold is accessed infrequently, it has low storage cost but high retrieval cost (popular for archiving data).

**Data Retention**:  Given our discussion about hot, warm, and cold data, implement automatic data lifecycle management practices and move the data to cold storage if you don’t need the data past the required retention date. Or delete data if it’s truly not needed.

**Single-Tenant vs Multitenant Storage**: With single-tenant architecture, each group of tenants (e.g., individual users, groups of users, accounts, or customers) gets its own dedicated set of resources such as networking, compute, and storage. A multitenant architecture inverts this and shares these resources among groups of users. This means you have the liberty of designing each tenant’s storage environment to be uniform or let them evolve however they may. Schema variation across customers can be an advantage and a complication.

**Security**:  Exercise the principle of least privilege. Don’t give full database access to anyone unless required. This means most data engineers don’t need full database access in practice. Also, pay attention to the column, row, and cell-level access con‐ trols in your database. Give users only the information they need and no more.

**Privacy**: GDPR and other privacy regulations have significantly impacted storage system design. Any data with privacy implications has a lifecycle that data engineers must manage. Data engineers must be prepared to respond to data deletion requests and selectively remove data as required. In addition, engineers can accommodate privacy and security through anonymization and masking.

**COW (Copy on write)**: File-based systems don’t actually support in-place file updates. All of these systems utilize copy on write (COW). If one record in a file is changed or deleted, the whole file must be rewritten with the new changes. This is part of the reason that early adopters of big data and data lakes rejected updates: managing files and updates seemed too complicated.

## Ingestion

**Data Pipelines**:  A data pipeline is the combination of architecture, systems, and processes that move data through the stages of the data engineering lifecycle. A data pipeline could be a traditional ETL system, where data is ingested from an on-premises transactional system, passed through a monolithic processor, and written into a data warehouse. Or it could be a cloud-based data pipeline that pulls data from 100 sources, combines it into 20 wide tables, trains five other ML models, deploys them into production, and monitors ongoing performance. A data pipeline should be flexible enough to fit any needs along the data engineering lifecycle.

**Bounded vs Unbounded Data**: Unbounded data is data as it exists in reality, as events happen, either sporadically or continuously, ongoing and flowing. Bounded data is a conve‐ nient way of bucketing data across some sort of boundary, such as time.

**Frecuency**: Ingestion processes can be batch, micro-batch, or real-time. Ingestion frequencies vary dramatically from slow to fast. On the slow end, a business might ship its tax data to an accounting firm once a year. On the faster side, a CDC system could retrieve new log updates from a source database once a minute. Even faster, a system might continuously ingest events from IoT sensors and process these within seconds. Data-ingestion frequencies are often mixed in a company, depending on the use case and technologies.

**Synchronous Versus Asynchronous Ingestion**: With synchronous ingestion, the source, ingestion, and destination have complex dependencies and are tightly coupled. Each stage of the data engineering lifecycle has processes A, B, and C directly dependent upon one another. If process A fails, processes B and C cannot start; if process B fails, process C doesn’t start. With asynchronous ingestion, dependencies can now operate at the level of individ‐ ual events, much as they would in a software backend built from microservices. The big idea is that each stage of the asynchronous pipeline can process data items as they become available in parallel across the beam.

**Throughput**: Data throughput and system scalability become critical as your data volumes grow and requirements change. Design your systems to scale and shrink to flexibly match the desired data throughput.

**Payload**: A payload is the dataset you’re ingesting and has characteristics such as kind, shape, size, schema and data types, and metadata:
- **Kind**: Type (image, video, text...) and format (JPG, PNG, CSV...) of the data. 
- **Shape**: Every payload has a shape that describes its dimensions. Tabular (the number of rows and columns in the dataset, commonly expressed as M rows and N columns), JSON (the key-value pairs and nesting depth occur with subelements), images (the width, height, and RGB color depth), uncompressed audio (number of channels (e.g., two for stereo), sample depth (e.g., 16 bits per sample), sample rate (e.g., 48 kHz), and length (e.g., 10,003 seconds)) etc.
- **Size**: The size of the data describes the number of bytes of a payload. A payload may range in size from single bytes to terabytes and larger.
- **Schema and data types**: Many data payloads have a schema, such as tabular and semistructured data. Other data, such as unstructured text, images, and audio, will not have an explicit schema or data types. However, they might come with technical file descriptions on shape, data and file format, encoding, size, etc.
- **Metadata**: Metadata is data about data. Metadata can be as critical as the data itself.

**Push vs Pull vs Pool Patterns**: A push strategy involves a source system sending data to a target, while a pull strategy entails a target reading data directly from a source. Polling involves periodically checking a data source for any changes. When changes are detected, the destination pulls the data as it would in a regular pull situation.

**Snapshot or Differential Extraction**: With full snapshots, engineers grab the entire current state of the source system on each update read. With the differential update pattern, engineers can pull only the updates and changes since the last read from the source system.

**Error Handling and Dead-Letter Queues**: In message/stream ingestion, sometimes events aren’t successfully ingested. Perhaps an event is sent to a nonexistent topic or message queue, the message size may be too large, or the event has expired past its TTL. Events that cannot be ingested need to be rerouted and stored in a separate location called a dead-letter queue. If events are not rerouted to a dead-letter queue, these erroneous events risk blocking other messages from being ingested. Data engineers can use a dead-letter queue to diagnose why event ingestions errors occur and solve data pipeline problems.

**EDI**: Another practical reality for data engineers is electronic data interchange (EDI). The term is vague enough to refer to any data movement method. It usually refers to somewhat archaic means of file exchange, such as by email or flash drive. Data engineers will find that some data sources do not support more modern means of data transport, often because of archaic IT systems or human process limitations.

**Orchestration**: As data pipeline complexity grows, true orchestration is necessary. By true orches‐ tration, we mean a system capable of scheduling complete task graphs rather than individual tasks. An orchestration can start each ingestion task at the appropriate scheduled time. Downstream processing and transform steps begin as ingestion tasks are completed. Further downstream, processing steps lead to additional processing steps.

## Queries / Modeling / Transformation

## Queries 

- **DDL**: Data Definition Language operations on database objects, such as the database itself, schemas, tables, or users (CREATE, DROP, ALTER...).

- **DML**: Data Manipulation Language define database objects (SELECT, INSERT, UPDATE, DELETE, COPY, MERGE...).

- **DCL**: Data Control Language allows you to control access to the database objects or the data by using SQL commands such as GRANT, DENY, and REVOKE.

- **TCL**: Transaction Control Language supports commands that control the details of transactions. With TCL, we can define commit checkpoints, conditions when actions will be rolled back, and more. Two common TCL commands include COMMIT and ROLLBACK.

**CTE**: Common Table Expressions is a powerful construct in SQL that helps simplify a query. Use CTE instead of nested subqueries or temporary tables. Example: "WITH my_cte AS ( SELECT a FROM T1 ) SELECT a FROM my_cte WHERE...".

**Explain Plan**: The database’s query optimizer influences the execution of a query. The query optimizer’s explain plan will show you how the query optimizer determined its optimum lowest-cost query. Some databases provide a visual representation of query stages. In contrast, others make the explain plan available via SQL with the EXPLAIN command, which displays the sequence of steps the database will take to execute the query.

**Transactions (on a database)**: The purpose of a transaction is to keep a consistent state of a database both while it’s active and in the event of a failure. Transactions also handle isolation when multiple concurrent events might be reading, writing, and deleting from the same database objects. Without transactions, users would get potentially conflicting information when querying a database. Be aware that during update and delete transactions, some databases create new files to represent the new state of the database and retain the old files for failure checkpoint references.

**Vacuum**: As we just discussed, transactions incur the overhead of creating new records during certain operations, such as updates, deletes, and index operations, while retaining the old records as pointers to the last state of the database. As these old records accumu‐ late in the database filesystem, they eventually no longer need to be referenced. You should remove these dead records in a process called vacuuming.

## Modeling 

**Data Models**: When modeling data, the idea is to move from abstract modeling concepts to concrete implementation:
- **Conceptual**: Contains business logic and rules and describes the system’s data, such as sche‐ mas, tables, and fields (names and types). When creating a conceptual model, it’s often helpful to visualize it in an entity-relationship (ER) diagram, which is a standard tool for visualizing the relationships among various entities in your data (orders, customers, products, etc.).
- **Logical**:  Details how the conceptual model will be implemented in practice by adding significantly more detail. For example, we would add information on the types of customer ID, customer names, and custom addresses. In addition, we would map out primary and foreign keys.
- **Physical**: Defines how the logical model will be implemented in a database system. We would add specific databases, schemas, and tables to our logical model, including configuration details.
- **Normalization**:  Normalization is a database data modeling practice that enforces strict control over the relationships of tables and columns within a database. The goal of normalization is to remove the redundancy of data within a database and ensure referential integrity. Basically, it’s don’t repeat yourself (DRY) applied to data in a database.

**Modeling Batch Analytical Data**:  When describing data modeling for data lakes or data warehouses, you should assume that the raw data takes many forms (e.g., structured and semistructured), but the output is a structured data model of rows and columns. However, several approaches to data modeling can be used in these environments:

**Inmon**: The goal of the data warehouse was to separate the source system from the analytical system. Integrates data from across the business in the data warehouse, and serves department-specific analytics via data marts. Data from key business source systems is ingested and integrated into a highly normalized (3NF) data warehouse (as little data duplication as possible). The data is presented for downstream reports and analysis via business and department-specific data marts, which may also be denormalized.

**Kimball**: The Kimball approach makes the data mart the data warehouse itself. This may enable faster iteration and modeling than Inmon, with the trade-off of potential looser data integration, data redundancy (no normalization), and duplication. Data is modeled with two general types of tables: facts and dimensions. The star schema represents the data model of the business. Unlike highly normalized approaches to data modeling, the star schema is a fact table surrounded by the necessary dimensions. This results in fewer joins than other data models, which speeds up query performance. Another advantage of a star schema is it’s arguably easier for business users to understand and use.

**Data Vault**: Data Vault simply loads data from source systems directly into a handful of purpose-built tables in an insert-only manner. Unlike the other data modeling approaches you’ve learned about, there’s no notion of good, bad, or conformed data in a Data Vault. A Data Vault model consists of three main types of tables: hubs, links, and satellites. In short, a hub stores business keys, a link maintains relationships among business keys, and a satellite represents a business key’s attributes and context.

## Transformation

**Batch Transformations**: Batch transformations run on discrete chunks of data, in contrast to streaming trans‐ formations, where data is processed continuously as it arrives. Batch transformations can run on a fixed schedule (e.g., daily, hourly, or every 15 minutes) to support ongoing reporting, analytics, and ML models.

**Distributed joins**: The basic idea behind distributed joins is that we need to break a logical join (the join defined by the query logic) into much smaller node joins that run on individual servers in the cluster:
- **Broadcast Joins**:  A broadcast join is generally asymmetric, with one large table dis‐ tributed across nodes and one small table that can easily fit on a single node. The query engine “broadcasts” the small table (table A) out to all nodes, where it gets joined to the parts of the large table (table B). Broadcast joins are far less compute intensive than shuffle hash joins.
- **Shuffle Hash Joins**:  If neither table is small enough to fit on a single node, the query engine will use a shuffle hash join. Shuffle hash joins are generally more resource intensive than broadcast joins.

**Update Patterns**:  Since transformations persist data, we will often update persisted data in place. Updating data is a major pain point for data engineering teams, especially as they transition between data engineering technologies.
- **Truncate and Reload**: Truncate is an update pattern that doesn’t update anything. It simply wipes the old data. In a truncate-and-reload update pattern, a table is cleared of data, and transformations are rerun and loaded into this table, effectively generat‐ ing a new table version.
- **Insert Only**:  Insert only inserts new records without changing or deleting old records. Insert-only patterns can be used to maintain a current view of data.  The downside to this approach is that it can be extremely computationally expensive to find the latest record at query time.
- **Delete**:  Deletion is critical when a source system deletes data and satisfies recent regulatory changes. In columnar systems and data lakes, deletes are more expensive than inserts. When deleting data, consider whether you need to do a hard or soft delete. A hard delete permanently removes a record from a database, while a soft delete marks the record as “deleted.”
- **Upsert/merge**: Upserting takes a set of source records and looks for matches against a target table by using a primary key or another logical condition.  When a key match occurs, the target record gets updated (replaced by the new record). When no match exists, the database inserts the new record. The merge pattern adds to this the ability to delete records.

**Data wrangling**: Data wrangling takes messy, malformed data and turns it into useful, clean data. This is generally a batch transformation process. Often, the data is so malformed that a good deal of text preprocessing is involved. Developers then begin writing queries to parse and break apart the data. Data wrangling tools aim to simplify significant parts of this process.

**Views (nonmaterialized)**: A view is a database object that we can select from just like any other table. In practice, a view is just a query that references other tables. When we select from a view, that database creates a new query that combines the view subquery with our query.  A potential disadvantage of views is that they don’t do any precom‐ putation. When quering a view, the query that generates the view runs first.

**Materialized views**: A materialized view does some or all of the view computation in advance. For example, a materialized view might update every time a change occurs in the source tables. Then, when a user references the view, they’re querying from the materialized view directly.

**Composable materialized views**: In general, materialized views do not allow for composition—that is, a materialized view cannot select from another materialized view.  We've recently seen the emergence of tools that support this capability. For example, Databricks has intro‐ duced the notion of live tables. Each table is updated as data arrives from sources. Data flows down to subsequent tables asynchronously.

**Federated queries**: Federated queries are a database feature that allows an OLAP database to select from an external data source, such as object storage or RDBMS.  For example, let’s say you need to combine data across object storage and various tables in MySQL and PostgreSQL databases. Your data warehouse can issue a federated query to these sources and return the combined results.

**Data virtualization**: Data virtualization is closely related to federated queries, but this typically entails a data processing and query system that doesn’t store data internally. Any query/processing engine that supports external tables can serve as a data virtualization engine.

## Serving

- Who will use the data, and how will they use it? 
- What do stakeholders expect?
- How can I collaborate with data stakeholders (e.g., data scientists, analysts, business users) to understand how the data I’m working with will be used?

**Data validation**: Data validation is analyzing data to ensure that it accurately represents financial information, customer interactions, and sales.

**Data observability**: Data ovservability provides an ongoing view of data and data processes. These processes must be applied throughout the data engineering lifecycle to realize a good result as we reach the end.

**SLA**: Service Level Agreement or data contracts tells users what to expect from your data product; it is a contract between you and your stakeholders. An example of an SLA might be, “Data will be reliably available and of high quality.”

**SLO**: Service Level Objectives describes the ways you’ll measure performance against what you’ve agreed to. For example, given the preceding example SLA, an SLO might be, “Our data pipelines to your dashboard or ML workflow will have 99% uptime, with 95% of data free of defects.”

**Analytics**:  The first data-serving use case you’ll likely encounter is analytics, which is discovering, exploring, identifying, and making visible key insights and patterns within data:
- **Business Analytics**: Business analytics uses historical and current data to make strategic and actionable decisions. The types of decisions tend to factor in longer-term trends.
- **Operational Analytics**: Operational analytics uses data to take immediate action. The big difference between operational and business analytics is time. The engineering team might have a dashboard that shows the key metrics such as requests per sec‐ ond, database I/O, or whatever metrics are important.
- **Embedded Analytics (data applications)**: A recent trend is external-facing or embedded analytics. With so much data powering applications, companies increasingly provide analytics to end users. For example, a smart thermostat has a mobile application that shows the temperature in real time and up-to-date power consumption metrics. Here, users want low data latency. High concurrency is critical.

**Semantic and Metrics Layers**: Metrics layer tools help solve a central question in analytics that has plagued organizations since people have analyzed data: “Are these numbers correct?”. Allows users to define standard metrics and reference them in many downstream queries; this is meant to solve the traditional problem of repetition and inconsistency in traditional ETL scripts.


## EXTRA:

**Data in the C-suite**
- **CEO**:  Chief executive officers (CEOs) at nontech companies gener‐ ally don’t concern themselves with the nitty-gritty of data frameworks and software. Instead, they define a vision in collaboration with technical C-suite roles and com‐ pany data leadership. Data engineers provide a window into what’s possible with data.
- **CIO**:  Chief information officer (CIO) is the senior C-suite executive responsible for information technology within an organization; it is an internal-facing role. A CIO must possess deep knowledge of information technology and business processes.
- **CTO**:  A chief technology officer (CTO) is similar to a CIO but faces outward. A CTO owns the key technological strategy and architectures for externalfacing applications, such as mobile, web apps, and IoT. The CTO is likely a skilled technologist and has a good sense of software engineering fundamentals and system architecture.
- **CDO**:  The chief data officer (CDO) is responsible for a company’s data assets and strategy. CDOs are focused on data’s business utility but should have a strong technical grounding. CDOs oversee data products, strategy, initiatives, and core functions such as master data management and privacy.
- **CAO**:  The chief analytics officer (CAO) is a variant of the CDO role. Where both roles exist, the CDO focuses on the technology and organization required to deliver data. The CAO is responsible for analytics, strategy, and decision making for the business.
- **CAO-2**:  A chief algorithms officer (CAO-2) is a recent innovation in the C-suite, a highly technical role focused specifically on data science and ML.  

**Project Manager**: Project managers must filter a long list of requests and prioritize critical deliverables to keep projects on track and better serve the company.  Data engineers interact with project managers, often planning sprints for projects and ensuing standups related to the sprint. Feedback goes both ways.

**Product manager**: Product managers oversee product (data products) development, often owning product lines. Data engineers interact more frequently with product managers as the corporate world has adopted a data-centric focus. Like project managers, product managers balance the activity of technology teams against the needs of the customer and business.

## MORE EXTRA:

**Security Theater**: We’re amazed at the number of companies with security policies in the hundreds of pages that nobody reads, the annual security policy review that people immediately forget, all in checking a box for a security audit. This is security theater, where security is done in the letter of compliance (SOC-2, ISO 27001, and related) without real commitment.
