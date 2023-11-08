import mysql.connector
import pandas as pd

#connect to server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=input('Write password')
)

sql_code = """
DELETE FROM clinic_db.employees
WHERE department_id IN (3, 4)
ORDER BY id;
"""
mycursor = mydb.cursor()
mycursor.execute(sql_code)


mycursor.close()
mydb.close()