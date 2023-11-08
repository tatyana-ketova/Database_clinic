import mysql.connector
import pandas as pd

#connect to server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=input('Write password')
)

sql_code = """
SELECT id, CONCAT(first_name, ' ',last_name) AS full_name, job_title, salary
FROM clinic_db.employees
WHERE salary>1000
ORDER BY id
"""



sql_query = pd.read_sql_query(sql_code, mydb)
result = pd.DataFrame(sql_query,columns = ['id', 'full_name', 'job','salary'])
print(result)

