#Ethan Sandstrom
#Databases final project Fall 2023

#Implement basic querying abilities through python

import sqlite3

conn = sqlite3.connect('causes.db')
cursor = conn.cursor()

#cursor.execute('SELECT * from data WHERE id=20')
cursor.execute('SELECT * FROM data ORDER BY Deaths DESC LIMIT 1')
results = cursor.fetchall()
print(results)
print()


conn.close()