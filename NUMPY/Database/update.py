# import oracledb as orc 
# def insertData():
#     try:
#         conn=orc.connect("ANIKET/1234@localhost/ORCL")
#         cur=conn.cursor()
#         iq="UPDATE STUDENT1 SET s_Name='HARSHAL' WHERE s_Roll_No = 2"
#         cur.execute(iq)
#         conn.commit()
#         print("Data Updated Successfully--Verify")
#     except orc.DatabaseError as db:
#         print("Problem in oracle db:",db)    
# insertData()


import oracledb as orc
def updaterecords():
    while(True):
        try:
            conn=orc.connect("ANIKET/1234@localhost/orcl")
            cur=conn.cursor()
            roll_no=int(input("Enter a Roll number that you want to update record:"))
            name=input("Enter a name:")
            faculty=input("Enter a Faculty Of Student:")
            q="update STUDENT1 set s_Name='%s' ,s_FACULTY ='%s' where s_ROLL_No=%d" %(name,faculty,roll_no)
            cur.execute(q )
            conn.commit()
            print("Your Record Successfully Updated:")
            ch=input("you want to insert record say yes/no..!")
            if ch.lower()=="no":
                print("thnx for using these program:")
                break
        except orc.DatabaseError as db:
            print("Problem in oracle db :",db)    
        except ValueError as v:
            print("Don't Enter Alnums ,Stars And Symbols")    
updaterecords()