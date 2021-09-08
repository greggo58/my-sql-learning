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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = ("SELECT * FROM Genre")
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether the the above was successful
    connection.close()
