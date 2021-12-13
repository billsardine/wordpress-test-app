#!/usr/bin/env python3

import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(user='wp_user', password='wordpress', host='wp-db',database='wordpress')

# if conn:
#    print ("Connected Successfully")
# else:
#    print ("Connection Not Established")

select_user = """SELECT * FROM wp_users"""
cursor = conn.cursor()
cursor.execute(select_user)
result = cursor.fetchall()

print("Content-type:text/html\n\n")
print("<head><title>Employee Database Dump Tool</title></head>\n")
print("<body>\n")
print("<h1>Employee Database Dump Tool</h1>\n")
print(tabulate(result, tablefmt="html"))

