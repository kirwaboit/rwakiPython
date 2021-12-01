# more on this here https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html 

import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='Gazagda1@',
    host='127.0.0.1',
    database='sakila')

cursor = cnx.cursor()
cursor.execute('SELECT * FROM sakila.actor')

for row in cursor:
    print(row)

cnx.close()
