from flask import Flask, render_template, url_for, redirect, session, request
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from dotenv import load_dotenv
import os
from db_functions import update_or_create_user
import sqlalchemy
import pandas as pd
import logging 
"""

This script uses the pymysql library for connecting to MySQL, 
so you might need to install that (pip install pymysql) if you haven't already.

It also uses python-dotenv for bringing in secrets from your .env file 

The .env should have the following in it:

DB_HOST=your_host
DB_DATABASE=your_database_name
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_PORT=3306
DB_CHARSET=utf8mb4

The default port is set to 3306 for MySQL, but you can override it by 
modifying the DB_PORT in your .env file.

The connection string is MySQL-specific, incorporating the specified port and charset.


"""
# Database connection settings from environment variables
load_dotenv()   
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")


GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

url_object = sqlalchemy.URL.create(
    "mysql+mysqlconnector",
    username=DB_USERNAME,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_DATABASE,
)

con = sqlalchemy.create_engine(url_object)

logging.basicConfig(
    level=logging.DEBUG,
    filename="logs/app.log",
    filemode="w",
    format='%(levelname)s - %(name)s - %(message)s'
)
def clean_data():
    df = pd.read_csv('data/heart.csv')

    #Identifying missing values in the dataset 
    logging.debug(df.isnull().values.sum())

    #Checking/Removing for any duplicate columns
    logging.debug(df.columns.duplicated())

    #Checking for any duplicate rows
    logging.debug(df.duplicated().values.sum())

    #Dropping any duplicate rows 
    df.drop_duplicates(inplace=True)

    #Cleaning column names
    df = df.rename(columns = {'Age':'age',
                        'Sex':'sex',
                        'ChestPainType':'chest_pain_type',
                        'RestingBP':'resting_bp',
                        'Cholesterol':'cholesterol',
                        'FastingBS':'fasting_bs',
                        'RestingECG':'resting_ecg',
                        'MaxHR':'max_hr',
                        'ExerciseAngina':'exercise_angina',
                        'Oldpeak':'old_peak',
                        'ST_Slope':'st_slope',
                        'HeartDisease':'heart_disease'})

    #Checkng to see if all column names are cleaned and renamed 
    logging.debug(df.columns)

    df[['exercise_angina']] = df[['exercise_angina']].replace(['N','Y'], [0, 1])
    logging.debug(df)

    df.to_sql(name='heart_failure_prediction', if_exists='append', con=con, index=False)


app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)

@app.route('/')
def index():
    try:
        logging.debug("success! index page has been accessed")
        return render_template('index.html')
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return render_template('error.html')

@app.route('/google/')
def google():
    try:
        logging.debug("success! google page has been accessed")
        CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
        oauth.register(
            name='google',
            client_id=GOOGLE_CLIENT_ID,
            client_secret=GOOGLE_CLIENT_SECRET,
            server_metadata_url=CONF_URL,
            client_kwargs={
                'scope': 'openid email profile'
            }
        )
        # Redirect to google_auth function
        ###note, if running locally on a non-google shell, do not need to override redirect_uri
        ### and can just use url_for as below
        redirect_uri = url_for('google_auth', _external=True)
        session['nonce'] = generate_token()
        ##, note: if running in google shell, need to override redirect_uri 
        ## to the external web address of the shell, e.g.,
        # redirect_uri = 'http://fahima-504-final.azurewebsites.net/google/auth/'
        return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return render_template('error.html')
   

@app.route('/google/auth/')
def google_auth():
    try:
        logging.debug("success! google_auth page has been accessed")
        token = oauth.google.authorize_access_token()
        user = oauth.google.parse_id_token(token, nonce=session['nonce'])
        session['user'] = user
        update_or_create_user(user)
        return redirect('/dashboard')
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return render_template('error.html')


@app.route('/dashboard/')
def dashboard():
    try:
        logging.debug("success! dashboard page has been accessed")
        user = session.get('user')
        if not user:
            raise Exception("User is not logged in")
        return render_template('dashboard.html',  user=user)
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return render_template('error.html')
    

@app.route('/logout')
def logout():
    try:
        logging.debug("success! logout page has been accessed")
        session.pop('user', None)
        return redirect('/')
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return render_template('error.html')
   


def execute_query_to_dataframe(query: str, engine):
    """Execute SQL query and return result as a DataFrame."""
    return pd.read_sql(query, engine)

sql_query = "SELECT * FROM heart_failure_prediction"  # Modify as per your table
df = execute_query_to_dataframe(sql_query, con)

@app.route('/data', methods=['GET'])
def data(data=df):
    try:
        user = session.get('user')
        if not user:
            raise Exception("User is not logged in")
        age = request.args.get('age')
        heart_disease = request.args.get('heart_disease')
        if age:
            data = data.loc[data['age'] == int(age)]
        if heart_disease:
            data = data.loc[data['heart_disease'] == int(heart_disease)]
        logging.debug("success! data page has been accessed")
        return render_template('data.html', data=data)
    except Exception as e:
        logging.error(f"an error occured! {e}")
        return render_template('error.html')


if __name__ == '__main__':
    app.run(
        debug=True, 
        port=5000,
        host='0.0.0.0'
    )


