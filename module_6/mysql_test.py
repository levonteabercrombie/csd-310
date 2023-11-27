import mysql.connector
from mysql.connector import Error

# my database configuration
db_config = {
    'host': 'localhost',
    'user': 'levonte.abercrombie@gmail.com',
    'password': 'Noahjackson23!',
    'database': 'Movies',
}

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        # Tells me if I'm connected to MySQL database
        print("Connected to MySQL database")
except Error as e:
    #prints error if there's a mistake made
    print(f"Error: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
