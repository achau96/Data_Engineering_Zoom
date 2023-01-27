# Week 1 Notes

## Issues

- Install wget with chocolatey for windows -> run command "wget 
- Using git bash, need to lead with // when using C:/  
- Port number must be changed due to having Postgres installed locally.  
- pgcli did not work with git bash -> used powershell instead. This will only be used temporarily until we access pgAdmin 4  
- jupyter nbconvert --to FileName.ipynb //this converts to py file for script
- multiline cursor shortcut Ctrl+Alt+UP/DOWN

## 1.2.3
- Remember database is what you set it as from network -> in this case pg-database

## 1.2.4
- argparse to send commands through to py file

## 1.2.5 - Running Postgres and pgAdmin with Docker-Compose
Specify R/W, do not need to add full path as we did before
```
    volumes:
     - ./ny_taxi_postgres_data:/var/lib/postgresql/data:rw
```
Command to run docker compose:
`docker-compose up`

Add `-d` to Docker Compose up for detatched mode (gives back access to terminal).

Command shut down in Docker Compose:
`docker-compose down`

Note: Docker compose comes with Docker Desktop for Mac and Windows, but you will have to install seperately on Linux Systems.

## 1.2.6 - SQL Refresher
taxi_zone_lookup.csv Address Link:
```
https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
```

## 1.3.1 - Intro to Terraform and GCP
What is terraform?
Terraform is an IaC (Infrastructure as Code) that acts as a GIT/ Version Control for infrastructure.
GCP - Create free account.

Download terraform and GCP SDK -> connect GCP to coomputer/shell -> allow admin access to storage