from prefect.deployments import Deployment
from etl_web_to_gcs import etl_web_to_gcs
from prefect.filesystems import GitHub

github_block = GitHub.load("zoom-github")

github_dep = Deployment.build_from_flow(
    flow=etl_web_to_gcs,
    name="docker-flow",
    infrastructure=github_block,
)


if __name__ == "__main__":
    github_dep.apply()

# for homework # 4, set -p color to green taxi for month nov (11)