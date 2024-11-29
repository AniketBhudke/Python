import mysql.connector
def createdynamically():
    try:
        conn=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="12345",
                                    database="mydb2")
        sno=int(input("Enter a number:"))
        name=input("enter a name:")
        faculty=input("Enter a faculty:")
        cur=conn.cursor()
        dc="insert into student1 values(%d,'%s','%s')"
        cur.execute(dc %(sno,name,faculty))
        conn.commit()
        print("Data inserted successfully---varify")
    except mysql.connector.DatabaseError as db:
        print("problem occur in mysql db",db)

createdynamically()