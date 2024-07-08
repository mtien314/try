import streamlit as st
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

# MariaDB connection details from secrets
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "work"
DB_USER = "root"
DB_PASSWORD = "123"

# Create the database connection
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Function to run a query and return a DataFrame
def run_query(query):
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result

# Streamlit app
st.title('MariaDB Streamlit App')

query = "SELECT * FROM your_table LIMIT 10;"
data = run_query(query)

st.write(data)
