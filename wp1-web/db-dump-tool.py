#!/usr/bin/env python3

import mysql.connector
from tabulate import tabulate

try:
    print("Content-type:text/html\n\n")
    print("<head><title>Employee Database Dump Tool</title></head>\n")
    print("<body>\n")
    print("<h1>Employee Database Dump Tool</h1>\n")
    print("<h2>Connecting to Database</h2>")
    
    conn = mysql.connector.connect(connection_timeout=5, user='wp_user', password='wordpress', host='wp-db',database='wordpress')

except mysql.connector.Error as err:
    print("Content-type:text/html\n\n")
    print("<head><title>Employee Database Dump Tool</title></head>\n")
    print("<body>\n")
    print("<h1>Employee Database Dump Tool</h1>\n")
    print("<h2>Database Connection is broken</h2>")
    print(err)
else:
    select_user = """SELECT * FROM wp_users"""
    cursor = conn.cursor()
    cursor.execute(select_user)
    result = cursor.fetchall()

    print("Content-type:text/html\n\n")
    print("<head><title>Employee Database Dump Tool</title></head>\n")
    print("<body>\n")
    print("<h1>Employee Database Dump Tool</h1>\n")
    print(tabulate(result, tablefmt="html"))
    conn.close()





