import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Likemerun@23",
  database = "alx"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE custom (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")