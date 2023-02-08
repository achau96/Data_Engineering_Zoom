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
In this tutorial, we learned how to move data from google cloud storage to big query.
The first step was to make a similar python file compared to the last tutorial. 
We create a big query storage and store the transformed data from the google cloud storage onto there.
Having the transformed data loaded on here lets analysts, machine learners and visual analysts use this data.

# 2.2.5 - PParametrizing Flow & Deployments with ETL into GCS flow
Set up deployment for code to automonously set pipeline (maybe runs on schedule)
Tell prefect what to expect. Could have multiple deployments for one code.
Allows us to make work queues on prefect.

Command for setting up a deployment based of py flow:
`prefect deployment build ./parameterized_flow.py:etl_parent_flow -n "Parameterized ETL"`

Command for apply agent based off built yaml file:
`prefect deployment apply etl_parent_flow-deployment.yaml`

Command for starting deployment:
`prefect agent start -q 'default'`

# 2.2.6 - Schedules & Docker Storage with Infrastructure
Add schedule on prefect - can choose between Interval, Cron or RRule.
Can also schedule via CLI when creating deployments by:
`prefect deployment build flows/03_deployments/parameterized_flow.py:etl_parent_flow -n etl2 --cron "0 0 * * * -a`
Will create deployment at 12am everyday.

`prefect deployment build ./parameterized_flow.py:etl_parent_flow -n "Parameterized ETL" --cron "0 0 * * * -a"` 
Set to go every day at 12 am.
"minute hour day(of month) month day(of week)"

Error: failed to solve with frontend dockerfile.v0:
Solution: rename dockerfile to specifically `Dockerfile` as it is the default name docker searches for unless you specify the file name.

`prefect profile ls`
shows all profiles. Comes with default. 

Run prefect deployment with different parameters:
`prefect deployment run etl-parent-flow/docker-flow -p "months=[1,2]"`

To switch between cloud and local or any other workspaces, you can use:
`prefect profile use dev # or prod or any other profile`
Check  https://discourse.prefect.io/t/managing-environments-with-prefect-2-0-dev-staging-prod/1071 for more details!

Also had to change write_local path to match:
```
@task()
def write_local(df: pd.DataFrame, color: str, dataset_file: str) -> Path:
    """Write DataFrame out as a local parquet file"""
    path = Path(f"2_workflow_orchestration/data/{color}/{dataset_file}.parquet")
    df.to_parquet(path, compression="gzip") # need pyarrow for compression, it is installed with file
    return path
```