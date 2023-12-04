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

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

# Creating tables with corrected syntax
cursor.execute("CREATE DATABASE outland")
cursor.execute("CREATE TABLE staff (staff_id int not null auto_increment PRIMARY KEY, first_name varchar(30) not null, last_name varchar(30) not null, title varchar(30) not null,  email varchar(50) not null, phone_number varchar(12) not null, address varchar(50) not null, city varchar(30) not null, state varchar(30) not null, zip int not null, country varchar(30) not null, birth_date DATE not null, hire_date DATE not null)")

cursor.execute("CREATE TABLE customer(customer_id int not null auto_increment PRIMARY KEY, first_name varchar(30), last_name varchar(30), email varchar(50), phone_number varchar(12), address varchar(50), city varchar(30), state varchar(30), zip int, country varchar(30), birth_date DATE)")

cursor.execute("CREATE TABLE supplier(supplier_id int not null auto_increment PRIMARY KEY, company_name varchar(30) not null, contact_name varchar(30), email varchar(50) not null, phone_number varchar(12) not null, address varchar(50) not null, city varchar(30) not null, state varchar(30) not null, zip int not null, country varchar(30) not null)")

cursor.execute("CREATE TABLE order(order_id int not null auto_increment PRIMARY KEY, customer_id int not null, ship_address varchar(50) not null, ship_city varchar(30) not null, ship_state varchar(30) not null, ship_zip int not null, ship_country varchar(30) not null, order_date DATE not null, shipped_date DATE not null, required_date DATE not null)")
cursor.execute("CREATE TABLE order_details(order_id int not null, product_id int not null, unit_price DECIMAL(10,2) not null, quantity int not null, discount DECIMAL(10,2) not null, PRIMARY KEY (order_id, product_id))")

cursor.execute("CREATE TABLE product(product_id int not null auto_increment PRIMARY KEY, supplier_id int not null, category_id int not null, product_name varchar(50) not null, unit_price DECIMAL(10,2) not null, unit_stock int not null, discount DECIMAL(10,2) not null)")
cursor.execute("CREATE TABLE trip (trip_id int not null auto_increment PRIMARY KEY, staff_id int not null, customer_id int not null, address varchar(50) not null, city varchar(30) not null, state varchar(30), zip int not null, country varchar(30) not null, start_date DATE not null, end_date DATE not null)")

cursor.execute("CREATE TABLE category(category_id int not null auto_increment PRIMARY KEY, category_name varchar(30) not null, category_description varchar(30) not null)")

# Adding foreign key constraints
cursor.execute("ALTER TABLE order ADD CONSTRAINT customer_id FOREIGN KEY (customer_id) REFERENCES customer (customer_id)")
cursor.execute("ALTER TABLE product ADD CONSTRAINT supplier_id FOREIGN KEY (supplier_id) REFERENCES supplier (supplier_id)")
cursor.execute("ALTER TABLE product ADD CONSTRAINT category_id FOREIGN KEY (category_id) REFERENCES category (category_id)")
cursor.execute("ALTER TABLE trip ADD CONSTRAINT staff_id FOREIGN KEY (staff_id) REFERENCES staff (staff_id)")
cursor.execute("ALTER TABLE trip ADD CONSTRAINT customer_id_fk FOREIGN KEY (customer_id) REFERENCES customer (customer_id)")

# Inserting records
cursor.execute("INSERT INTO staff(first_name, last_name, title,  email, phone_number, address, city, state, zip, country, birth_date, hire_date) VALUES('John','MacNell','Guide','John12389@gmail.com','705-603-8788','955 East Cherry Street', 'Denver', 'Colorado', 80012,'United States','1980-12-17','2010-2-15')")
# ... (other staff records)
cursor.execute("INSERT INTO customer( first_name, last_name, email, phone_number, address, city, state, zip, country, birth_date) VALUES('Sophie','Johnson','John12389@gmail.com','705-603-3342','778 East Carlton Street', 'Denver', 'Colorado', 80012,'United States','1998-5-20')")
# ... (other customer records)
cursor.execute("INSERT INTO supplier(company_name, contact_name, email, phone_number, address, city, state, zip, country) VALUES('Mal & Co','Dean Striffer','deanStriff77@MalCo.com','765-780-5625','878 Silver Avenue', 'New York', 'New York', 10001,'United States')")
# ... (other supplier records)
# ... (similar inserts for order, category, product, trip, and order_details)

db.commit()
db.close()
