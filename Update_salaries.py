import mysql.connector
import pandas as pd

#connect to server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=input('Write password')
)

sql_code = """
SET SQL_SAFE_UPDATES = 0;
UPDATE clinic_db.employees
SET salary = salary * 1.10
WHERE job_title = 'Dentist';
"""
mycursor = mydb.cursor()
mycursor.execute(sql_code)


mycursor.close()
mydb.close()

