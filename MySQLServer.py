import mysql.connector
from mysql.connector import Error

# Replace with your connection details
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Likemerun@23",
            # database="alx_book_store"
            )
        
        
        # Execute SQL statements using the execute() method on the cursor
        if mydb.is_connected():
            cursor = mydb.cursor()
            # SQL query to create the database if it does not exist
            create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
            
            cursor.execute(create_database_query)
            print("Database 'alx_book_store' created successfully:")
            
            # cursor.execute("USE alx_book_store;")
            # record = cursor.fetchone()
            # print("you're connected to database:",record)
            
            
    except Error as e:
        print("mysql.connector.Error", e)
    finally:
        # Close the connection
        if (mydb.is_connected()):
            mydb.close()
            print("MySQL connection is closed")
            
connect_to_database()            