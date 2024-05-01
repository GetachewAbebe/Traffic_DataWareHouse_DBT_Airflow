import os
from os.path import join, dirname
from pprint import pprint
from traceback import print_exc
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import inspect
import urllib.parse
from dotenv import load_dotenv


# Get PostgreSQL credentials from environment variables
load_dotenv()
username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
database_name = os.getenv("POSTGRES_DATABASE")
# Encode the password if needed
encoded_password = urllib.parse.quote(password)
# Create the database URL
database_url = f"postgresql://{username}:{encoded_password}@{host}/{database_name}"
# Create the engine using the database URL
engine = create_engine(database_url)

# Create the tables
def create_tables(name):
    try:
        with engine.connect() as conn:
            with open(name) as file:
                query = text(file.read())
                conn.execute(query)
        print("Successfully Created {} table".format(name.split(".")[-2]))
    except:
        print("Unable to Create the TableT")
        print(print_exc())

# Populate the tables
def insert_data(df: pd.DataFrame, table_name):
    try:
        with engine.connect() as conn:
            df.to_sql(name=table_name, con=conn,
                      if_exists='replace', index=False)
        print(f"Done inserting to {table_name}")
        #print(BANNER)
    except:
        print("Unable to Insert Data to the Table")
        print(print_exc())

# Implement Querying functions
def get_table_names():
    with engine.connect() as conn:
        inspector = inspect(conn)
        names = inspector.get_table_names()
        return names

def get_vehicles():
    with engine.connect() as conn:
        veh_df = pd.read_sql_table('vehicles', con=conn)

        return veh_df

def get_trajectories():
    with engine.connect() as conn:
        trajectories_df = pd.read_sql_table('trajectories', con=conn)

        return trajectories_df

if __name__=="__main__":
    print(get_table_names())