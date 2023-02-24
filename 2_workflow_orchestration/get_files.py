# import the wget module
import requests
from pathlib import Path
from tqdm import *


def etl_parent_flow(
    months: list[int] = [1, 2], year: int = 2019, color: str = "yellow"
):
    for month in months:
        # r = requests.get(f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{color}_tripdata_{year}-{month:02}.csv.gz", allow_redirects=True)
        # open(Path(f"data/{color}/{color}_tripdata_{year}-{month:02}.csv.gz"), 'wb').write(r.content)
        with requests.get(f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{color}_tripdata_{year}-{month:02}.csv.gz", stream=True) as r:
            r.raise_for_status()
            with open(Path(f"data/{color}/{color}_tripdata_{year}-{month:02}.csv.gz"), 'wb') as f:
                pbar = tqdm(total=int(r.headers['Content-Length']))
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        pbar.update(len(chunk))


if __name__ == '__main__':
    color = 'yellow'
    months = [10,11,12]
    year = 2019
    etl_parent_flow(months, year, color)

