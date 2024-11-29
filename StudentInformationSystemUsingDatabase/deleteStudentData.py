import mysql.connector
def deleteStudentData():
    while(True):
        try:
            conn=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="12345",
                                        database="StudentInformationSystem")
            sno=int(input("Enter a student Roll Number That You want to Delete:"))
            cur=conn.cursor()
            iq="delete from StudentInformation where s_no=%d"
            cur.execute(iq %(sno))
            conn.commit()
            if cur.rowcount > 0:
                print("Your Record Successfully Deleted--Verify")
            else:
                print("Your Record Not Exist--Try Again")    
            ch=input("Do You Want To Delete The Data:(yes/no):")
            if ch.lower()=="no":
                print("Thnx for using Delete Operation")
                break
        except mysql.connector.DatabaseError as db:
            print("Your Problem In MySQl DB",db)

    


