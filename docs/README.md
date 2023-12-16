# flask_e2e_project
This is the final assignment for HHA 504

The web service you created (what is it and what does it do)
I used this data set from kaggle (explain here) I cleaned the dataset chnamging column naes, check if any nan values were present  - non, chnage TF to 0 and 1 exercise angina instaed of y and N I chose this dataset because it cinclided string, boolean, intigers, values. after cleaning the data the data was pushed into mysql database. 
the web service priomts the usedr to loin with their google account once the user loging in wioth thier google account they see the dashboard woith their ggole account and a button that says veiw data. whn the viewer clock view data they see the data in the data base in a tbale format. 
the user cannot see the dashbaord or the dataset if they are not logged in. 


The technologies you used
cleaning of dataset : PANDAS 
PUPUALOTING DATASET IN MYSQL - SQLALCHEMY, MySQL, Azure, alembic
Front end technologies : html, jinja templating , CSS, tailwind 

autentication- google oauth, flask 
back-end technologies: mysql, flask (api)

deployment: Azure 
logging: Logger
containerization: Docker

The steps to run your web service if someone wanted to either run locally or deploy to the cloud
## How could they run it without Docker locally?
Update the .env file with your google credentials as well as database credentials. Once that is completed run 
`pip3 install -r requirements.txt`. Follow the instructions in `azure.py` to run the migration. Comment out line 134 in `app.py`. Call the function `clean_data` in `app.py`.Now run `python3 app.py`. Be sure to comment out the call to `clean_data` once completed.
## How could they run it with Docker locally?
Update the .env file with your google credentials as well as database credentials. Once that is completed run 
`pip3 install -r requirements.txt`. Follow the instructions in `azure.py` to run the migration. Comment out line 134 in `app.py`. Call the function `clean_data` in `app.py`. Now run the following two commands: `docker build -t docker_example_1 .` and `docker run -d -p 5001:5000 docker_example_1`. Be sure to comment out the call to `clean_data` once completed.
## How could they deploy it to the cloud?
Follow the instructions in `azure.py` to run the migration for the database.
- I first had to connect my VSC to my Azure acount, so I went into this url: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
- This url gave me a command that I pasted into my terminal: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash (this command is used to install azure).
- I then typed az to make sure my Azure and VSC were connected.
- I then copied and pasted this code to login: az login --use-device-code and hit enter.
- I was provided with another url and a code in my terminal. I followed by copying the code and clicking into the url. I pasted the code in the spave provided.
- To get the azure student subscription ID I used this code: az account list --output table and hit enter.
- I copied the last subscriptionID which was linked to Azure for students and I pasted it into this code: az account set --subscription yoursubscriptionId (I pasted the ID towards the end where it says yoursubscriptionId). I had already used an old resource group.
- Finally, I pasted this code: az webapp up --resource-group --name --runtime PYTHON:3.9 --sku B1 for groupname I changed it to my resource groupname, which is Fahima504 and for app-name I made up Fahima-flask-app-video.
- FINALLY, I pasted this code to re-deploy: az webapp up
Update your application configuration to include all the env variables listed in .env template below. 
Change line 134 to include your url instead in `app.py`. Call the function `clean_data` in `app.py`.
Redeploy by running `az webapp up` and then comment out the call all to the function `clean_data` in `app.py` once the data is added. Redeploy again using `az webapp up`.

## A template of the .env file structure you used, which should include all of the environment variables you used like below. Please be sure to NOT include your actual API keys in the github repo.:
```
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
DB_HOST=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
```



App URL: https://fahima-504-final.azurewebsites.net/