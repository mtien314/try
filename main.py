import mysql.connector
import streamlit as st

host = st.secret["HOST"]
port = st.secret["PORT"]
user = st.secret["USER"]
password = st.secret["PASSWORD"]
db = st.secret["DB"]
conn = mysql.connector.connect(host = host,
                       port =port,
                       user = user,
                       passwd = password,
                       db = db)

cursor = conn.cursor()
