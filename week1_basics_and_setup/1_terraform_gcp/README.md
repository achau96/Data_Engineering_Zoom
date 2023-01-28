# Terraform and GCP
## 1.3.2 - Creating CGP Infrastructure with Terraform
- Terraform only has 4 commands: init, plan, apply, destroy
- I accidentally put key up to GitHub. Instead of making a new project I could just make a new key.
- Check to see if removed from status

## 1.3.4 - Setting up Environment 
### Link - https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13
Create a virtual machine on GCP using Google Compute Engine
Set up SSH Key.
```
ssh-keygen -t rsa -f C:\Users\WINDOWS_USER\.ssh\KEY_FILENAME -C USERNAME -b 2048
```

Make a config file in .ssh folder
```
Host de-zoomcamp
    HostName {external ip address}
    User {user}
    IdentityFile C:/Users/{USER}/.ssh/gcp
```

Access with the 
`ssh de-zoomcamp` command. Or manually ssh every time.

Access docker without sudo:
https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md

Install Docker Compose from GitHub releases and put into a bin directory and give it executable property with `chmod +x docker-compose`

Ran into issue where conda was stuck at solving environment, might 
have worked but would take too long due to long list of packages and different version included. Therefore, we create a new environment which uses the latest packages by using the command:
`conda create --name myenv` or with a specific version of python
`conda create -n myenv python=3.9`
and activating (similar to git checkout) by `conda activate myenv`.

This will solve the loading times.

Use sftp to get data over to VM. 
Set GOOGLE_APPLICATION_CREDENTIALS to point to the file:
```export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/ny-rides.json```
Then authenticate:
```gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS```

Install pandas, psycopg2-binary and sqlalchemy as needed on VM.
Change data file to a .gz file. 

Issues not solved:
Port 5432 was used on my comptuer to local host moved it to 5433. When I tried connecting by changing ports it was frozen and did not run. Perhaps next time we can set postgres to launch on an empty port to the port forwarding matches.