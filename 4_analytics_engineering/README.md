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

 ### Seeds
 Seeds are CSV files in dbt project and can be referenced using ref function.
 Seeds are best suited to static data which change infrequently.

 ## 4.3.2 - Testing and Documenting the Project
 ### Tests
  - Assumption that we make about our data
  - Tests in dbt are essentially a select sql query
  - These assumptions get compiled to sql that returns the amount of failing records
  - Tests are defined on a column in the .yml file
  - dbt provides basic tests to check if the column values are
    - Unique
    - Not null
    - Accepted values
    - A foreign key to another table
  - You can create your custom tests as queries

  ### Documentation with dbt
   - dbt provides way to generate documentation for dbt project and render it as a website
   - Documention for project includes:
    - Information about your project
     - Model code (both from .sql file and compiled)
     - Model dependencies
     - Sources
     - Auto generated DAG from the ref and source macros
     - Descriptions from .yml file and tests
    - Information about your data warehouse (information_schema)
     - Column names and data types
     - Table stats like size and rows
   - dbt docs can also be hosted in dbt cloud 

   - Severity warning : if fail, dbt should keep running and give warnings
   ```
   - name: tripid
            description: Primary key for this table, generated with a concatenation of vendorid+pickup_datetime
            tests:
                - unique:
                    severity: warn
                - not_null:
                    severity: warn
   ```

   ## 4.4.1 - Deployment using dbt Cloud
   ### What is deployment?
    - Process of running the models we created in our development environment in a production environment
    - Development and later deployment allows us to continue building models and testing them without affecting our production environment
    - A deployment environment will normally have a different schema in our data warehouse and ideally a different user
    - A development - deployment workflow will be something like:
     - Develop in a user branch
     - Open a PR to merge into the main branch
     - Merge the branch to the main branch
     - Run the new models in the production environment using the main branch
     - Schedule the models

### Running a dbt project in production
   - dbt cloud includes a scheduler which creates jobs to run in production
   - A single job can run multiple commands
   - Jobs can be triggered manually or on schedule
   - Each job will keep a log of the runs over time
   - Each run will have the logs for each command
   - A job could also generate documentation, that could be viewed under the run information
   - If dbt source freshness was run, the results can also be viewed at the end of a job

### WHat is Continuous Integration (CI)?
 - CI is the practice of regularly merge development branches into a central repository, after which automated builds and tests are run.
 - The goal is to reduce adding bugs to the production code and maintain a more stable project
 - dbt allows us to enable CI on pull requests
 - Enabled via webhooks from Github or Gitlab
 - When a PR is ready to be merged, a webhooks is received in dbt CLoud that will enqueue a new run of the specified job
 - The run of the CI job will be against a temporary schema
 - No PR will be able to be merged unless the run has been completely successful

 Link to video for <a link = https://www.youtube.com/watch?v=rjf6yZNGX8I&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=37>setting up documentation</a>