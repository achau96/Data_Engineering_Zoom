winpty docker run -it \
 -e POSTGRES_USER="root" \
 -e POSTGRES_PASSWORD="root" \
 -e POSTGRES_DB="ny_taxi" \
 -v //c/Users/Austin/Desktop/DataEngineerZoom/2_workflow_orchestration/ny_taxi_postgres_data:/var/lib/postgresql/data \
 -p 5431:5432 \
 postgres:13
