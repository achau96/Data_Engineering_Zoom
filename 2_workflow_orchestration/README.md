# Workflow Orchestration

## 2.1.1 - Data Lakes

### What is a Data Lake?
* Ingested structured and unstructured data. 
* Stores, secures and protects data at unlimited scales
* Catalogs and indexes for analysis without data movement
* Connects data with analytics and machine learning tools

### Data Lake vs Data Warehouse?
Data Lake - raw data, vast amounts of data, undefined data -> targets data scientists and data analysts
Data Warehouse - Refined and clean, less data for cleanliness, relational data -> targets business analysts

### ETL vs ELT
Extract, Transform and Load vs Extract, Load and transform.
ETL mainly used for small amounts of data whereas ELT used for large amounts of data.
ELT provides data lake support.

## 2.2.1 Introduction to Workflow Orchestration

Governing your data flow in a way that respects orchestration rules in your business logistics.

Downloaded anaconda for windows -> looked for conda.sh folder in Anaconda3/etc/profile.d/conda.sh and ran command to get conda environment in Git Bash.

`echo ". ${PWD}/conda.sh" >> ~/.bashrc`

Installing requirements through file (set up different env first) :
`pip install -r requirements.txt`


# 2.2.2 - Introduction to Prefect Concepts
Rearranged script into a flow. 
`conda activate (env)`
Created a basic ETL to ingest the data, clean out rows with passenger count of 0, and load it into postgres!
Check dashboard for all logs with command:
`prefect orion start`

# 2.2.3 - ETL with GCP & Prefect
Retries are helpful in flows just in case sometimes it doesn't work. 
Converted data to parquet file using pandas.
Cleaned data to remove dtype warning.
Downloaded gcs bucket on prefect Api and configured it to a bucket on gcp. Added cred key for safe transfer.
Added to code and loaded clean data to bucket!

# 2.2.4 - From google cloud storage to big query