"""

pip install sqlalchemy alembic mysql-connector-python pymysql

"""

## Part 1 - Define SQLAlchemy models for patients and their medical records:
### this file below could always be called db_schema.py or something similar

from sqlalchemy import create_engine, inspect, Column, Integer, Float, String, Boolean 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BreastCancer(Base):
    __tablename__ = 'heart_failure_prediction'
    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=False)
    sex = Column(String(1), nullable=False)
    chest_pain_type = Column(String(3), nullable=False)
    resting_bp = Column(Integer, nullable=False)
    cholesterol = Column(Integer, nullable=False)
    fasting_bs = Column(Boolean, nullable=False)
    resting_ecg = Column(String(6), nullable=False)
    max_hr = Column(Integer, nullable=False)
    exercise_angina = Column(Boolean, nullable=False)
    old_peak = Column(Float, nullable=False)
    st_slope = Column(String(4), nullable=False)
    heart_disease = Column(Boolean, nullable=False)

### Part 2 - initial sqlalchemy-engine to connect to db:

engine = create_engine("mysql+mysqlconnector://yourusername:yourpassword!@fahima-mysql-final.mysql.database.azure.com/Heart_Failure_Prediction")

# Create a database engine

## Test connection

inspector = inspect(engine)
inspector.get_table_names()


### Part 3 - create the tables using sqlalchemy models, with no raw SQL required:

Base.metadata.create_all(engine)

### Running migrations 
""" these steps are then performed in the termainl, outside of your python code

1. alembic init migrations
` alembic init migrations `

2. edit alembic.ini to point to your database
` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

3. edit env.py to point to your models
`from db_schema import Base`
`target_metadata = Base.metadata `

4. create a migration
` alembic revision --autogenerate -m "create tables" `

5. run the migration
` alembic upgrade head `

in addition, you can run ` alembic history ` to see the history of migrations
or you can run with the --sql flag to see the raw SQL that will be executed

so it could be like:
` alembic upgrade head --sql `

or if you then want to save it:
` alembic upgrade head --sql > migration.sql `

6. check the database

7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
The downgrade command allows you to revert the database schema to a previous 
migration version. Here's how you can use it:

`alembic downgrade <target_revision>` 

or if you want to roll back to the previous version, you can use the -1 flag:
`alembic downgrade -1`
 

"""