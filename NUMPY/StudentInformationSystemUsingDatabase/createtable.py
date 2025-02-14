import mysql.connector
def createtable():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345",
                                     database="studentinformationsystem")
        cur=conn.cursor()
        q="create table StudentInformation(s_no int,s_Name varchar(20),s_Marks varchar(20))";
        cur.execute(q)
        print("Your Tbale Created Successfully--Varify")
    except mysql.connector.DatabaseError as db:
        print("Problem occuer in MySQL DB:",db)
createtable()            