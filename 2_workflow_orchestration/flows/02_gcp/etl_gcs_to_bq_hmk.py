from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(log_prints=True, retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""
    gcs_path = f"data\{color}\{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("zoom-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../../data/yellow")
    return Path(f"{gcs_path}")


@task(log_prints=True)
def transform(path: Path) -> pd.DataFrame:
    """This part is ignored"""
    df = pd.read_parquet(path)
    # print(f"pre: missing passenger count: {df['passenger_count'].isna().sum()}")
    # df["passenger_count"].fillna(0, inplace=True)
    # print(f"post: missing passenger count: {df['passenger_count'].isna().sum()}")
    return df


@task(log_prints=True)
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("zoom-gcp-credentials")

    df.to_gbq(
        destination_table="dezoomcamp.rides",
        project_id="festive-terrain-376020",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )


@flow(log_prints=True)
def etl_gcs_to_bq(year, month, color):
    """Main ETL flow to load data into Big Query"""

    path = extract_from_gcs(color, year, month)
    df = transform(path)
    write_bq(df)
    print(f"rows: {len(df)}")
    return len(df)

@flow(log_prints=True)
def etl_parent_flow_bq(
    months: list[int] = [1, 2], year: int = 2021, color: str = "yellow"
):
    total_rows = 0
    for month in months:
        df = etl_gcs_to_bq(year, month, color)
        total_rows = total_rows + df

    print(total_rows)


if __name__ == '__main__':
    color = 'yellow'
    months = [2,3]
    year = 2019
    etl_parent_flow_bq(months, year, color)