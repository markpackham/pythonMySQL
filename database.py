import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()