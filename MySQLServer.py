import mysql.connector
from mysql.connector import Error

# Replace with your connection details
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Likemerun@23",
            database="alx_book_store"
            )
        
        
        # Execute SQL statements using the execute() method on the cursor
        if mydb.is_connected():
            print("Database 'alx_book_store' created successfully")
            # Create a cursor object
            cursor = mydb.cursor()
            
            cursor.execute("USE alx_book_store;")
            record = cursor.fetchone()
            print("you're connected to database:",record)
            
            
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # Close the connection
        if (mydb.is_connected()):
            mydb.close()
            print("MySQL connection is closed")
            
connect_to_database()            