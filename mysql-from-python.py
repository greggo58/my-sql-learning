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
        rows = [("Dave", 22, "1999-02-06 23:04:56"),
                ("Jim", 11, "2010-02-06 23:04:56"),
                ("Gerald", 45, "1976-02-06 23:04:56"),
                ("Fred", 67, "1954-02-06 23:04:56")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit()
finally:
    # Close the connection, regardless of whether the the above was successful
    connection.close()
