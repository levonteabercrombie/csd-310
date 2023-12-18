import mysql.connector
from mysql.connector import Error
from datetime import datetime, timedelta

# Function to establish a database connection
def connect_to_database():
    try:
        config = {
            "user": "root",
            "password": "password",
            "host": "localhost",
            "database": "outland",
            "raise_on_warnings": True,
            "port": 3306
        }
        db = mysql.connector.connect(**config)
        return db
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to select the database and print countries, start dates, end dates, number of trips, and total customer count for each continent
def print_country_info():
    try:
        cursor = db.cursor()

        cursor.execute("USE outland")

        # Calculate the date 10 years ago from the current date
        ten_years_ago = datetime.now() - timedelta(days=365 * 10)

        # Query to fetch countries, start dates, end dates, count of trips, and total customer count for specific countries and continent
        query = """
            SELECT country, start_date, end_date, COUNT(*) AS num_trips, COUNT(customer_id) AS total_customers
            FROM trip
            WHERE start_date >= %s
            GROUP BY country, start_date, end_date
        """
        cursor.execute(query, (ten_years_ago,))
        result = cursor.fetchall()

        # Print for Africa
        print("\n Bookings for Africa (Last 10 years)")
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Country", "Start Date", "End Date", "Num Trips", "Total Customers"))
        print("-" * 80)
        total_africa = 0
        total_customers_africa = 0
        for row in result:
            country = row[0]
            start_date = row[1].strftime("%Y-%m-%d") if row[1] else "N/A"
            end_date = row[2].strftime("%Y-%m-%d") if row[2] else "N/A"
            num_trips = row[3]
            total_customers = row[4]
            if country in ('South Africa', 'Other Africa Country'):
                total_africa += num_trips
                total_customers_africa += total_customers
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(country, start_date, end_date, num_trips, total_customers))

        print("\n Total Trips to Africa (Last 10 years): {}".format(total_africa))
        print(" Total Customers to Africa (Last 10 years): {}".format(total_customers_africa))

        # Fetch results again for Asia
        cursor.execute(query, (ten_years_ago,))
        result_asia = cursor.fetchall()

        # Print for Asia
        print("\n Bookings for Asia (Last 10 years)")
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Country", "Start Date", "End Date", "Num Trips", "Total Customers"))
        print("-" * 80)
        total_asia = 0
        total_customers_asia = 0
        for row in result_asia:
            country = row[0]
            start_date = row[1].strftime("%Y-%m-%d") if row[1] else "N/A"
            end_date = row[2].strftime("%Y-%m-%d") if row[2] else "N/A"
            num_trips = row[3]
            total_customers = row[4]
            if country in ('China', 'Other Asia Country'):
                total_asia += num_trips
                total_customers_asia += total_customers
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(country, start_date, end_date, num_trips, total_customers))

        print("\n Total Trips to Asia (Last 10 years): {}".format(total_asia))
        print(" Total Customers to Asia (Last 10 years): {}".format(total_customers_asia))

        # Fetch results again for Europe
        cursor.execute(query, (ten_years_ago,))
        result_europe = cursor.fetchall()

        # Print for Europe
        print("\n Bookings for Europe (Last 10 years)")
        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Country", "Start Date", "End Date", "Num Trips", "Total Customers"))
        print("-" * 80)
        total_europe = 0
        total_customers_europe = 0
        for row in result_europe:
            country = row[0]
            start_date = row[1].strftime("%Y-%m-%d") if row[1] else "N/A"
            end_date = row[2].strftime("%Y-%m-%d") if row[2] else "N/A"
            num_trips = row[3]
            total_customers = row[4]
            if country in ('North Macedonia', 'Bulgaria', 'Other Europe Country'):
                total_europe += num_trips
                total_customers_europe += total_customers
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(country, start_date, end_date, num_trips, total_customers))

        print("\n Total Trips to Europe (Last 10 years): {}".format(total_europe))
        print(" Total Customers to Europe (Last 10 years): {}".format(total_customers_europe))

    except Error as e:
        print(f"Error fetching data: {e}")

# Connect to the database
db = connect_to_database()

if db:
    # Print countries, start dates, end dates, number of trips, and total customer count for each continent
    print_country_info()

    db.close()
