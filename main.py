import mysql.connector
import streamlit as st

host = st.secrets["HOST"]
port = st.secrets["PORT"]
user = st.secrets["USER"]
password = st.secrets["PASSWORD"]
db = st.secrets["DB"]
conn = mysql.connector.connect(host = host,
                       port =port,
                       user = user,
                       passwd = password,
                       db = db)

cursor = conn.cursor()
