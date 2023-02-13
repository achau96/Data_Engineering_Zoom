## Week 3 Homework
<b><u>Important Note:</b></u> <p>You can load the data however you would like, but keep the files in .GZ Format. 
If you are using orchestration such as Airflow or Prefect do not load the data into Big Query using the orchestrator.</br> 
Stop with loading the files into a bucket. </br></br>
<u>NOTE:</u> You can use the CSV option for the GZ files when creating an External Table</br>

<b>SETUP:</b></br>
Create an external table using the fhv 2019 data. </br>
Create a table in BQ using the fhv 2019 data (do not partition or cluster this table). </br>
Data can be found here: https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/fhv </p>

"Couldn't make a load that goes directly from Github to GCS"

## Question 1:
What is the count for fhv vehicle records for year 2019?
- 65,623,481
- 43,244,696
- 22,978,333
- 13,942,414

SELECT count(*) from `festive-terrain-376020.dezoomcamp.fhv_tripdata`
ANS: 43, 244, 696

## Question 2:
Write a query to count the distinct number of affiliated_base_number for the entire dataset on both the tables.</br> 
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

- 25.2 MB for the External Table and 100.87MB for the BQ Table
- 225.82 MB for the External Table and 47.60MB for the BQ Table
- 0 MB for the External Table and 0MB for the BQ Table
- 0 MB for the External Table and 317.94MB for the BQ Table 

```
SELECT count(DISTINCT(Affiliated_base_number)) from `festive-terrain-376020.dezoomcamp.fhv_tripdata`

SELECT count(DISTINCT(Affiliated_base_number)) from `festive-terrain-376020.dezoomcamp.fhv_tripdata_local`
```
PS: The fhv_tripdata is the external table.
The local (BQ Table) recorded 317.94 MB. External recorded 0MB.


## Question 3:
How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?
- 717,748
- 1,215,687
- 5
- 20,332

```
SELECT count(*) from `festive-terrain-376020.dezoomcamp.fhv_tripdata`
WHERE PUlocationID IS NULL AND DOlocationID IS NULL
```

ANS: 717,748

## Question 4:
What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?
- Cluster on pickup_datetime Cluster on affiliated_base_number
- Partition by pickup_datetime Cluster on affiliated_base_number
- Partition by pickup_datetime Partition by affiliated_base_number
- Partition by affiliated_base_number Cluster on pickup_datetime

Partition by pickup_datetime Cluster on affiliated_base_number
Partitioning is good for seperating time and clustering is good for categories.

## Question 5:
Implement the optimized solution you chose for question 4. Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 2019/03/01 and 2019/03/31 (inclusive).</br> 
Use the BQ table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values? Choose the answer which most closely matches.
- 12.82 MB for non-partitioned table and 647.87 MB for the partitioned table
- <b>647.87 MB for non-partitioned table and 23.06 MB for the partitioned table</b>
- 582.63 MB for non-partitioned table and 0 MB for the partitioned table
- 646.25 MB for non-partitioned table and 646.25 MB for the partitioned table

```
CREATE OR REPLACE TABLE `festive-terrain-376020.dezoomcamp.fhv_tripdata_partitioned`
PARTITION BY DATE(pickup_datetime)
CLUSTER BY Affiliated_base_number AS (
  SELECT * FROM `festive-terrain-376020.dezoomcamp.fhv_tripdata_local`
);

SELECT count(*) FROM `festive-terrain-376020.dezoomcamp.fhv_tripdata_partitioned`
WHERE pickup_datetime BETWEEN '2019-03-01' AND '2019-03-31'

SELECT count(*) FROM `festive-terrain-376020.dezoomcamp.fhv_tripdata_local`
WHERE pickup_datetime BETWEEN '2019-03-01' AND '2019-03-31'
```

I did not get close numbers, but I did cluster as well.
From this result, I got 329.93 MB from non-partitioned table and 11.26 MB from partitioned.
Based on the answers, the closest one would be 647.87 MB for non-partition and 23.06 MB for partitioned which is about double the size of my answers.

## Question 6: 
Where is the data stored in the External Table you created?

- Big Query
- GCP Bucket
- Container Registry
- Big Table

GCP Bucket.

## Question 7:
It is best practice in Big Query to always cluster your data:
- True
- False

In general, when querying, you have to take account costs, so it is best to cluster and partition data where applicable.

## (Not required) Question 8:
A better format to store these files may be parquet. Create a data pipeline to download the gzip files and convert them into parquet. Upload the files to your GCP Bucket and create an External and BQ Table. 


Note: Column types for all files used in an External Table must have the same datatype. While an External Table may be created and shown in the side panel in Big Query, this will need to be validated by running a count query on the External Table to check if any errors occur. 
 
## Submitting the solutions

* Form for submitting: https://forms.gle/rLdvQW2igsAT73HTA
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 13 February (Monday), 22:00 CET


## Solution

We will publish the solution here