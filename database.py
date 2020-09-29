import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'myPyDB'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()