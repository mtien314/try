import streamlit as st
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

# MariaDB connection details from secrets
DB_HOST = st.secrets["DB_HOST"]
DB_PORT = st.secrets["DB_PORT"]
DB_NAME = st.secrets["DB_NAME"]
DB_USER = st.secrets["DB_USER"]
DB_PASSWORD = st.secrets["DB_PASSWORD"]

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
