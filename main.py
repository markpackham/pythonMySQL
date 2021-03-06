# create database and tables before running "python main.py"
from database import cursor, db

def add_log(text,user):
    sql = ("INSERT INTO logs(text, user) VALUES (%s, %s)")
    cursor.execute(sql, (text, user))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

def get_logs():
    sql = ("SELECT * FROM logs ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row[1])

def get_log(id):
    sql = ("SELECT * FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()
    print ("The specific log info for log id: {}".format(id))
    for row in result:
        print(row)

def update_log(id, text):
    sql = ("UPDATE logs SET text = %s WHERE id = %s")
    cursor.execute(sql, (text, id))
    db.commit()
    print("Log {} updated".format(id))

def delete_all():
    sql = ("DELETE FROM logs")
    cursor.execute(sql)
    db.commit()
    print("All logs deleted")

def delete_log(id):
    sql = ("DELETE FROM logs WHERE id = %s")
    cursor.execute(sql, (id,))
    db.commit()
    print("Log {} deleted".format(id))

# add_log("This is log one", "Mark")
# add_log("This is log two", "Alice")
# add_log("This is log three", "Bob")
# delete_all()
# get_log(1)
# update_log(2, 'I have been UPDATED!!!')
# delete_log(3)
get_logs()
