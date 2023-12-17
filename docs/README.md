# flask_e2e_project
This is the final assignment/project for HHA 504

## The web service you created (what is it and what does it do)
I used a dataset from Kaggle titled "Heart Failure Prediction Dataset" to be displayed on my web service. The dataset includes 12 columns and 918 rows of data. The columns in the dataset are based on and represents health/clinical aspects that can possibly predict heart failure or the possibility of being at risk for the disease. The discription of the dataset accurately explains how heart disease is a serious health issue and so many deaths are due to heart failure all around the world. Also, health aspects such as Age, Sex, Chest pain type, Resting BP, Cholesterol, Fasting BS, Resting ECG, Max HR, Exercise Angina, Old Peak, ST Slope can really help determine if an individual possibly has or is at risk of such a detrimental health illness. I found this dataset to be very interesting to analyze and to view if any possible trends exist in the dataset, and which patient had a heart disease and which did not given all the medical data. 
I also chose to use this dataset because it included strings, booleans, and intigers. 

References: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/

To prepare the dataset, I began by cleaning the dataset. I first checked to see if any values were missing in the dataset. I then followed by checking/removing any duplicate rows and columns. I then cleaned all the column names by changing upper case to lower case and replacing spaces with underscores. I proceeded by checking to ensure all the column names were cleaned and renamed to what I wanted it to be viewed as. Lastly, for the column "exercise_angina" I replaced the "N" and "Y" with "0" and "1". 
After cleaning the dataset the data was pushed into MySQL database. 

My web service prompts the user to login with their google account. Once the user logs in with their google account, they can then view the dashboard with their google account and a button that reads "View Data". When the viewer clicks on the "View Data" button they can preview the data in the data base in a table format. 
The user cannot see the dashbaord or the dataset if they are not logged in. 



## The technologies you used
Cleaning of dataset: Pandas  

Populating dataset in MySQL: SQLAlchemy, MySQL, Azure, Alembic

Front-End technologies: HTML, Jinja templating, CSS, Tailwind 

Autentication: Google OAuth, Flask 

Back-End technologies: MySQL, Flask (API)

Deployment: Azure 

Logging: Logger

Containerization: Docker



## The steps to run your web service if someone wanted to either run locally or deploy to the cloud
## How could they run it without Docker locally?
Update the .env file with your google credentials as well as database credentials. Once that is completed run 
`pip3 install -r requirements.txt`. Follow the instructions in `azure.py` to run the migration. Comment out line 134 in `app.py`. Call the function `clean_data` in `app.py`. Then run `python3 app.py`. Be sure to comment out the call to `clean_data` once completed.
## How could they run it with Docker locally?
Update the .env file with your google credentials as well as database credentials. Once that is completed run 
`pip3 install -r requirements.txt`. Follow the instructions in `azure.py` to run the migration. Comment out line 134 in `app.py`. Call the function `clean_data` in `app.py`. Then run the following two commands: `docker build -t docker_example_1` and `docker run -d -p 5001:5000 docker_example_1`. Be sure to comment out the call to `clean_data` once completed.
## How could they deploy it to the cloud?
Follow the instructions in `azure.py` to run the migration for the database.
- First connect VSC or Cloud Shell to your Azure account, so navigate to this url: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
- The url will give you a command under option 1 that you paste into your terminal: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bas` (this command is used to install azure).
- Then type `az` to make sure Azure is installed.
- Follow by pasting this code to login: `az login --use-device-code` and hit enter.
- You will then be provided with another url and a code in the terminal. Proceed by copying the code first and clicking into the url. Paste the code in the space provided.
- To get the azure student subscription ID use this code: `az account list --output table` and hit enter.
- Copy the last subscriptionId which is linked to Azure for Students, and paste it into the end of this code: `az account set --subscription yoursubscriptionId` (paste the ID towards the end where it says yoursubscriptionId). 
- Paste this code: `az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>` For <groupname> change it to the resource group name you have created in Azure and for <app-name> make something up.
- FINALLY, paste this code to re-deploy: `az webapp up`
Update your application configuration to include all the env variables listed in .env template below. 
Change line 134 to include your url instead in `app.py`. Call the function `clean_data` in `app.py`.
Re-deploy by running `az webapp up` and then comment out the call all to the function `clean_data` in `app.py` once the data is added. Re-deploy again using `az webapp up`.



## A template of the .env file structure you used, which should include all of the environment variables you used like below. Please be sure to NOT include your actual API keys in the github repo.:
```
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
DB_HOST=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
```



## App URL: https://fahima-504-final.azurewebsites.net/



## Video of App:
https://github.com/Lfahima/flask_e2e_project/assets/140275869/4413be0e-e2db-42be-924e-6a684250b888

## Video showing error message for user that is not logged in: 
https://github.com/Lfahima/flask_e2e_project/assets/140275869/cf3fa495-8cdd-4eb7-92ba-7e1e043f6596

## Video showing flask API capabilities:
https://github.com/Lfahima/flask_e2e_project/assets/140275869/5afd5275-b17a-48c8-9385-e57bc7584f67



## Image of login page:
<img width="1512" alt="Screenshot 2023-12-13 at 4 22 52 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/2f802701-5f4c-46f3-b7ce-32e769772b13">

## Image of google login:
<img width="1511" alt="Screenshot 2023-12-13 at 4 23 19 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/559ae995-2654-46de-8374-db65f7d0783d">

## Image of dashboard with botton to view dataset:
<img width="1512" alt="Screenshot 2023-12-13 at 4 27 26 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/e00a3ef5-c6f5-4cca-847c-86a296b30fe5">

## Image of displayed dataset:
<img width="1512" alt="Screenshot 2023-12-13 at 4 27 52 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/cd00befd-30ee-4b5e-a196-41e71d1c151c">

## Image of displayed dataset:
<img width="1510" alt="Screenshot 2023-12-13 at 4 28 21 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/5fcedda0-69e7-455a-92a0-f21580510519">

## Image of displayed dataset:
<img width="1512" alt="Screenshot 2023-12-13 at 4 28 31 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/0739fabf-2c20-4ee0-b46e-c55109b89e86">

## Image of displayed dataset:
<img width="1508" alt="Screenshot 2023-12-13 at 4 28 44 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/c22539ec-080b-4241-b1d5-e496738c9031">

## Image of flask API capibilties:
<img width="1508" alt="Screenshot 2023-12-15 at 7 23 32 PM" src="https://github.com/Lfahima/flask_e2e_project/assets/140275869/407e781b-0971-4807-a290-9f9aa9b320ee">


## References:
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/
