import mysql.connector
def createDatabse():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345")
        cur=conn.cursor()
        dc="create database schoo"
        cur.execute(dc)
        print("Database Created in MYsQl Successfully--Verify")
    except mysql.connector.DatabaseError as db:
        print("problem with oracle connection:",db)    

createDatabse()
