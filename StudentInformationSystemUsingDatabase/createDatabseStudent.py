import mysql.connector
def createStudentDatabase():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345")
        cur=conn.cursor()
        q="create database StudentInformationSystem"
        cur.execute(q)
        print("Your DataBase Created SuccessFully--Verify")
    except mysql.connector.DatabaseError as db:
        print("Your Problem  of MyQL db:",db)
        
          