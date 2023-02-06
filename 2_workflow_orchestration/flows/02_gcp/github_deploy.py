from prefect.deployments import Deployment
from etl_web_to_gcs_hmk import etl_web_to_gcs
from prefect.filesystems import GitHub 

storage = GitHub.load("zoom-github")

deployment = Deployment.build_from_flow(
     flow=etl_web_to_gcs,
     name="github-example",
     storage=storage,
     entrypoint="2_workflow_orchestration/flows/02_gcp/etl_web_to_gcs_hmk.py:etl_web_to_gcs")

if __name__ == "__main__":
    deployment.apply()





# prefect deployment build flows/02_gcp/etl_web_to_gcs_hmk.py:etl_web_to_gcs --name github_deploy --tag dev -sb github/zoom-github -a

	
# prefect deployment run etl-web-to-gcs/github_deploy

# prefect deployment build -n etl_github -sb github/zoom-github  ./2_workflow_orchestration/flows/02_gcp/etl_web_to_gcs_hmk.py:etl_web_to_gcs -a