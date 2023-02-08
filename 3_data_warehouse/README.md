# Data Warehouse

## 3.1.1 - Data warehouse and BigQuery

OLAP vs OLTP - Online analytical processing (OLAP) and online transactional processing (OLTP) are the two primary data processing systems.
OLTP is usually meant for processing data (inserts,updates,deletes) while OLAP is used for data scientists and analysts for researching purposes and understanding the businesss. 

BigQuery is a serverless data warehouse. 
Partitioning in Big Query allows you to save processing time.

## 3.1.2 - Partitioning and Clustering

Clustering - Order of column is important, determines the sort of data -> improves filter and aggregate queries.
Table sizes of less then 1GB do not show improvement. You can specify up to 4 custering columns. 
Columns must be top-level with non-repeated columns.

Partition allows us to add aggregrate function to individual rows while maintaining columns. Group by you would affect the columns.

Time-unit column
Ingenstion time (_PRATITIONTIME)
Integer range partitioning
When using Time unit or Ingestion Time - Daily, Hourly, Monthly or Yearly
Number of partitions limit is 4000
More at https://cloud.google.com/bigquery/docs/partitioned-tables