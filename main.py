import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

#create table
data = cursor.execute('SELECT * FROM pets')
result = cursor.fetchall()
df = pd.DataFrame(result, columns = ['Name'])
st.dataframe(df)  
cursor.close()
