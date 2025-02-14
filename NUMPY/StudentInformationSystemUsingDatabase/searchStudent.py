import mysql.connector 
def searchData():
    conn=mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="12345",
                                database="studentinformationsystem")
    eno=int(input("Enter a Student Number:"))
    cur=conn.cursor()
    q="select * from StudentInformation"
    cur.execute(q)
    #column_name
    #data in table
    records=cur.fetchall()
    for record in records:
        if record[0] == eno:
            column_name=cur.description
            for column in column_name:
                print(column[0],end="\t\t")
            print()
            for val in record:
                print(val,end="\t\t")
            print()  
            res=True
            break 
        else:
            res=False
    if res:
        print("Your Record Successfully Search--Verify")        
    else:
        print("Your Record Not In Record--Try Again")

