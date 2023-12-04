import mysql.connector
from mysql.connector import Error

db_config = {
    'host': 'localhost',
    'user': 'levonte.abercrombie@gmail.com',
    'password': 'Noahjackson23!',
    'database': 'Movies',
}

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        # Tells me if I'm connected to the MySQL database
        print("Connected to MySQL database")

    cursor = connection.cursor()

    # Creating tables with corrected syntax
    cursor.execute("CREATE DATABASE outland")
    cursor.execute("CREATE TABLE staff (staff_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30) NOT NULL, last_name VARCHAR(30) NOT NULL, title VARCHAR(30) NOT NULL, email VARCHAR(50) NOT NULL, phone_number VARCHAR(12) NOT NULL, address VARCHAR(50) NOT NULL, city VARCHAR(30) NOT NULL, state VARCHAR(30) NOT NULL, zip INT NOT NULL, country VARCHAR(30) NOT NULL, birth_date DATE NOT NULL, hire_date DATE NOT NULL)")

    # (similar create statements for other tables)

    # Adding foreign key constraints
    cursor.execute("ALTER TABLE order ADD CONSTRAINT customer_id FOREIGN KEY (customer_id) REFERENCES customer (customer_id)")
    cursor.execute("ALTER TABLE product ADD CONSTRAINT supplier_id FOREIGN KEY (supplier_id) REFERENCES supplier (supplier_id)")
    cursor.execute("ALTER TABLE product ADD CONSTRAINT category_id FOREIGN KEY (category_id) REFERENCES category (category_id)")
    cursor.execute("ALTER TABLE trip ADD CONSTRAINT staff_id FOREIGN KEY (staff_id) REFERENCES staff (staff_id)")
    cursor.execute("ALTER TABLE trip ADD CONSTRAINT customer_id_fk FOREIGN KEY (customer_id) REFERENCES customer (customer_id)")

    # Inserting records
    cursor.execute("INSERT INTO staff(first_name, last_name, title, email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('John', 'MacNell', 'Guide', 'John12389@gmail.com', '705-603-8788', '955 East Cherry Street', 'Denver', 'Colorado', 80012, 'United States', '1980-12-17', '2010-2-15')")
    # ... (similar insert statements for other tables)

    connection.commit()

except Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
