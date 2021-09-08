import os
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
        sql = ("SELECT * FROM Artist LIMIT 10;")
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
finally:
    # Close the connection, regardless of whether the the above was successful
    connection.close()
