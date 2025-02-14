import mysql.connector 
def updatetable():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345",
                                     database="mydb2")
        cur=conn.cursor()
        iq="update student1 set s_name = 'aniket' where no=1"
        cur.execute(iq)
        conn.commit()
        print("Data updated successfully---verify")
    except mysql.connector.DatabaseError as db:
        print("problem in mysql :",db)     
updatetable()
