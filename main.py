import mysql.connector

conn = mysql.connector.connect(host = "127.0.0.1",
                       port ="3306",
                       user = "root",
                       passwd = "123",
                       db = "work")

cursor = conn.cursor()
