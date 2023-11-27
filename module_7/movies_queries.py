import mysql.connector
from mysql.connector import Error

# Function to connect to MySQL
def connect_to_mysql():
    try:
        db_config = {
            'host': 'localhost',
            'user': 'levonte.abercrombie@gmail.com',
            'password': 'Noahjackson23!',
            'database': 'Movies',
        }
        db = mysql.connector.connect(**db_config)
        return db
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to execute queries with formatted output
def execute_query(cursor, query, description, format_q):
    cursor.execute(query)
    result = cursor.fetchall()
    print("\n-- DISPLAYING {} RECORDS --".format(description))
    
    for row in result:
        formatted_output = format_q.format(*row)
        print("{}".format(formatted_output))

# Connect to MySQL
db = connect_to_mysql()

if db:
    try:
        # Create a cursor
        cursor = db.cursor()

        # Query 1: Select all fields for the studio table
        query1 = "SELECT * FROM studio;"
        format_q1 = "Studio ID: {}\nStudio Name: {}"
        execute_query(cursor, query1, "Studio", format_q1)

        # Query 2: Select all fields for the genre table
        query2 = "SELECT * FROM genre;"
        format_q2 = "Genre ID: {}\nGenre Name: {}"
        execute_query(cursor, query2, "Genre", format_q2)

        # Query 3: Select movie names for movies with a run time of less than two hours
        query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;"
        format_q3 = "Film Name: {}\nRuntime: {}"
        execute_query(cursor, query3, "Short Film", format_q3)

        # Query 4: Get a list of film names and directors ordered by director
        query4 = "SELECT film_name, film_director FROM film ORDER BY film_director;"
        format_q4 = "Film Name: {}\nDirector: {}"
        execute_query(cursor, query4, "Director", format_q4)

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
else:
    print("Unable to connect to MySQL.")
