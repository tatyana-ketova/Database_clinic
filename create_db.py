import mysql.connector
#connect to server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=input('Write password')
)

#create a database if exists
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

database_exists = False
for db in mycursor:
    if db[0] == "clinic_db":
        database_exists = True
        break
if not database_exists:
    mycursor.execute("CREATE DATABASE clinic_db")
    print(f"Database clinic_db created.")
else:
    print(f"Database clinic_db already exists.")


sql_code = """
USE clinic_db;

CREATE TABLE IF NOT EXISTS departments(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50)
);

INSERT INTO departments(name) VALUES
('Therapy'),('Support'),('Management'),('Other');

CREATE TABLE IF NOT EXISTS employees(
id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
job_title VARCHAR(50) NOT NULL,
department_id INT NOT NULL,
salary DOUBLE NOT NULL,
CONSTRAINT fk_department_id FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO employees(first_name,last_name,job_title,department_id,salary) VALUES
('Maria','Andersson','Therapist',1,400.00),
('Anna','Johansson','Acupuncturist',1,830.00),
('Ingrid','Petersson','Technician',2,1140.00),
('Lena','Magnussson','Supervisor',3,1200.00),
('Sandy','Petersson','Dentist',4,1400.00),
('Max','Perrsson','Therapist',1,992.00),
('Anders','Tegnell','Epidemiologist',4,1340.00),
('Margareta','Olssson','Medical Director',3,2500.00),
('Daniel','Nilssson','Nuttririon Technician',4,2600.00);

CREATE TABLE IF NOT EXISTS rooms(
id INT PRIMARY KEY AUTO_INCREMENT,
occupation VARCHAR(30)
);

INSERT INTO rooms(occupation) VALUES ('free'),('occupied'),('free'),('free'),('occupied');

CREATE TABLE IF NOT EXISTS patients(
id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(50),
last_name VARCHAR(50),
room_id INT NOT NULL
);

INSERT INTO patients(first_name,last_name,room_id)
VALUES
('Birgitta','Larsson',1),
('Marianne','Lindeberg',3),
('Bertil','Dahlberg',2),
('Filip','Willhelm',2),
('Nikolay','Nikolaev',3);


"""
mycursor.fetchall()
mycursor = mydb.cursor()
mycursor.execute(sql_code)


mycursor.close()
mydb.close()