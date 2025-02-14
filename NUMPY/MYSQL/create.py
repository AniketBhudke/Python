import mysql.connector 
def insertdatabase():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345",
                                     database="mydb2")
        cur=conn.cursor()
        dc="create table student1(no int primary key,s_Name varchar(20),faculty varchar(20))"
        cur.execute(dc)
        print("table are created in databse successfully--verify")
    except mysql.connector.DatabaseError as db:
        print("problem with oracle connection db",db)
insertdatabase()            