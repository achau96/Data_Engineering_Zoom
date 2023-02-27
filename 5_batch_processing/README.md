# 5 - Batch processing & Spark

## 5.1.1 - Introduction to batch processing
Two ways to process data -> Batch and streaming.

Advantages of batch: (80% of companies use batch)
 - Easy to manage
 - Retry
 - Scale

Disadvantage:
 - Delay

## 5.1.2 - Introduction to Spark
Data Processing Engine written in Scala but there is good Python wrapper.

When to use Spark?
Datalake -> Spark (SQL) -> Datalake

## 5.2.1 - Installing Spark on Linux
Downloading Spark on VM -> https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_5_batch_processing/setup/linux.md

Start VM similar to week 1, install spark and anaconda. Use jupyter notebook to test as shown in video. Spark runs on local host 4040. 

## 5.3.1 - First Look at Spark/PySpark

Use this instead of video method of creating new file due to gz file:
`df_pandas = pd.read_csv('fhvhv_tripdata_2021-01.csv.gz', nrows=1001)`

Alt+Z to word wrap in VS Code!

To create a schema in spark, import types and choose the proper format.

Tab to autocomplete; Shift + Tab to see what function does in Jupyter Notebook.

```
from pyspark.sql import types

schema = types.StructType([
    types.StructField('hvfhs_license_num', types.StringType(), True), 
    types.StructField('dispatching_base_num', types.StringType(), True), 
    types.StructField('pickup_datetime', types.TimestampType(), True), 
    types.StructField('dropoff_datetime', types.TimestampType(), True), 
    types.StructField('PULocationID', types.IntegerType(), True), 
    types.StructField('DOLocationID', types.IntegerType(), True), 
    types.StructField('SR_Flag', types.StringType(), True)
])
```

## 5.3.2 - Spark DataFrames
### Actions vs Transformations
Transformations - lazy(not executed immediately - doesn't show on spark jobs)
 - Selecting columns
 - Filtering
 - Joins
 - Group by
Actions - eager (executed immediately - shows up on spark jobs)
 - show()
 - take()
 - head()
 - write

### Adding functions to pysparks function library:
 ```
 from pyspark.sql import functions as F
 def crazy_stuff(base_num):
    num = int(base_num[1:])
    if num % 7 == 0:
        return f's/{num:03x}'
    elif num % 3 == 0:
        return f'a/{num:03x}'
    else:
        return f'e/{num:03x}'
 crazy_stuff('B02884')
 crazy_stuff_udf = F.udf(crazy_stuff, returnType=types.StringType())
 ```