# Analytics Engineering

## 4.1.1 - Analytics Engineering Basics
Roles in a data team - Data Engineer, Analytics Engineer, Data Analyst
Analytics Engineer does a bit of both data engineering and data analyst

### Tools ->
Data Loading
Data Storing - Snowflake, Bigquery, Redshift
Data Modelling -> dbt or Dataform
Data Presentation -> Looker, Google data studio, Tableau

### Data Modelling concepts -> ETL vs ELT
ETL -> Extract, transform and Load
- Slightly more stable and compliant data analysis
- Higher storage and compute costs
ELT -> Extract, Load and Transform (Eg in chapter 3 homework where you loaded the data onto GC storage and then created external table with BigQuery and performed queries through there)
- Faster and more flexible data analysis
- Lower cost and maintenance

### Kimball's Dimensional Modelling
#### <b>Objective</b>
- Deliver data understandable to the business users
- Deliver fast query performance