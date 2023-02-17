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
#### <b>Approach</b>
Prioritize user understability and query performance over non redundant data (3NF), Bill Inmon, Data Vault

### Elements of Dimensional Modeling
Star Schema
- Fact tables -> Measurements, metrics or facts (verbs)
- Dimension Tables -> Corresponds to a business entity, provides context to a business process (nouns)

### Architecture of Dimesional Modeling
Stage Area
- Contains the raw data, not meant to be exposed to everyone
Processing Area
- From raw data to data models
- Focus on efficiency
- Ensuring standards
Presentation Area
- Final presentation of the data
- Exposure to business stakeholder

## 4.2.2 - What is dbt
dbt is a transformation tool that allows anyone that knows SQL to deploy analytics code following software engineering best practices like modularity, portability, CI/CD and documentation.

Recreated green data trips data into bucket and cleaned data types by recasting them all to floats or integers respectively.
Type casting with pandas using `df['trip_type'] = df['trip_type'].astype(int)` astype for dataframes.

### How to use dbt?
dbt Core - essence of dbt
- Builds and runs a dbt project(.sql and .yml files)
- Includes SQL compilation logic, macros and database adapters
- Includes a CLI interface to run dbt commands locally
- Opens source and free to use

dbt Cloud
SaaS application to develop and manage dbt projects
- Web-based IDE to develop, run and test a dbt project
- Jobs orchestration
- Logging and Alerting
- Integrated documentation
- Free for individuals (one developer seat)

## 4.3.1 - Build the First DBT Model
After signing up with DBT Cloud, connect BigQuery and GitHub.
### Macros
Use control structures in SQL
Use env variables in dbt project
Operate on the result of one query to generate another query
Abstract snippets in SQL into reusable macros. 
Similar to importing functions.

### Dependencies
Add dependencies to a packages.yml file in the root folder.
`dbt deps` to download all dependencies.

### Variables
Variables are useful for defining values that should be used across project
With a macro, dbt allows us to provide data to models for compilation.
To use a variable we use the {{ var{'...'}}} function
Variables can be defined in two ways
 - In the dbt_project.yml file
 - On the command line

 ### Adding a second model
 You can add more table names by adding into schema.yml