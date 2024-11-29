import mysql.connector
def deleterecord():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345",
                                     database="mydb2")
        cur=conn.cursor()
        iq="delete from student1 where no=1"
        cur.execute(iq)
        conn.commit()
        print("your table record successfully deleted---verify")
    except mysql.connector.DatabaseError as db:
        print('problem occur in MYSQL :',db)

deleterecord()
