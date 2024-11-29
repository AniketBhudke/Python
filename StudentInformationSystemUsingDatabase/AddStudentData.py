import mysql.connector
def insertStudentData():
    while(True):
        try:
            conn=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="12345",
                                        database="studentinformationsystem")
            cur=conn.cursor()
            sno=int(input("Enter A Roll Number:"))
            query = "select s_no from StudentInformation"
            cur.execute(query)
            records=cur.fetchall()
            s_no = sno,
            if s_no in records:
                print(f"Record Is Already In Database--Try Again")
            else:
                sname=input("Enter a Student Name:")
                if not sname.isalpha():
                    print("Enter The Don't")
                    break
                smarks=float(input("Enter A student Marks:"))
                q="insert into StudentInformation values(%d,'%s',%f)"
                cur.execute(q %(sno,sname,smarks))
                conn.commit()
                print("Data Inserted in Table Successfully---Verify")
            c=input("Do You Want Add Record In Table:(yes/no)")
            if c.lower() == "no":
                print("Thnx for Using these Program:")
                break
        except mysql.connector.DatabaseError as db:
            print("problem in MySQL db",db)
        except ValueError:
            print("Don't Enter Alnums,strs and symbols,Enter A Correct Value")


