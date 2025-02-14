import mysql.connector
def updateStudentData():
    while(True):
        try:
            conn=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="12345",
                                        database="studentinformationsystem")
            sno=int(input("Enter A Student Nuumber That you Want To Update:"))
            cur=conn.cursor()
            q="select s_no from StudentInformation"
            cur.execute(q)
            records=cur.fetchall()
            s_no = sno,
            if s_no in records:
                sname=input("Enter a Student Name:")
                smarks=float(input("Enter a student marks:"))
                q="update  StudentInformation set s_Name='%s',s_Marks=%f where s_no=%d"
                cur.execute(q %(sname,smarks,sno))
                conn.commit()
                print("Your data Updated Successfully--Verify")
            else:
                print("Your Data In The Table Is Not Found--Try Again")   
            ch=input("Do you want to update a Record:(yes/no)")
            if ch.lower()=="no":
                print("Thnx For Updating Recoreds")
                break
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQl db",db) 
        except ValueError:
            print("Don't Enter Alnums,Stars and Symbols:")

    
