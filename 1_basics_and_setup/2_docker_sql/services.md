services:
  pgdatabase:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxi
    volumes:
      - "./ny_taxi_postgres_data:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"



winpty docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v //c/Users/Austin/Desktop/DataEngineerZoom/week1_basics_and_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
 -p 5431:5432 \
 postgres:13

winpty docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
dpage/pgadmin4

308b8f65569b073eaf0252aeaf60bd2cea84602d134b6d48455024a0aa57ec46

## network
winpty docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v //c/Users/Austin/Desktop/DataEngineerZoom/week1_basics_and_setup/2_docker_sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
 -p 5431:5432 \
 --network=pg-network \
 --name pg-database \
 postgres:13

 winpty docker run -it \
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
-e PGADMIN_DEFAULT_PASSWORD="root" \
-p 8080:80 \
--network=pg-network \
--name pgadmin \
dpage/pgadmin4

python ingest_data.py \
 --user=root \
 --password=root \
 --host=localhost \
 --port=5431 \
 --db=ny_taxi \
 --table_name=yellow_taxi_trips \
 --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

 # building the docker image
 docker build -t taxi_ingest:v001 .

URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

# running the docker image
winpty docker run -it \
 --network=pg-network \
 taxi_ingest:v001 \
 --user=root \
 --password=root \
 --host=pg-database \
 --port=5432 \
 --db=ny_taxi \
 --table_name=yellow_taxi_trips \
 --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

 # running the docker image for zones
winpty docker run -it \
 --network=pg-network \
 taxi_ingest:v001 \
 --user=root \
 --password=root \
 --host=pg-database \
 --port=5432 \
 --db=ny_taxi \
 --table_name=zones \
 --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"