import os
# import datetime
import pymysql

# Get username from workspace
username = os.getenv('C9_USER')

# Connection params
conn_params = {
    'host': 'localhost',
    'user': username,
    'password': '',
    'db': 'Chinook'
}

# Connect to the database
connection = pymysql.connect(**conn_params)

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'Bob'))
        connection.commit()
finally:
    # Close the connection, regardless of whether the the above was successful
    connection.close()
