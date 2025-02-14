import mysql.connector
def viewSingleRecored():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345",
                                     database="studentinformationsystem")
        sno=int(input("Enter a Student Number That Data you want to see:"))
        cur=conn.cursor()
        q="select * from StudentInformation where s_no=%d"
        cur.execute(q %(sno))
        #cur.commit()
        #getting column_name
        #data in column
        records=cur.fetchall()
        for record in records:
            if record[0]==sno:
                column_name=cur.description
                for column in column_name:
                    print(column[0],end="\t\t")
                print()
                for val in record:
                    print(val,end="\t\t")
                print()        
        if cur.rowcount > 0:
            print("Your Selected Record Getting Successfully--Verify")
        else:
            print("Your Inserted Student Number Not In Table--Try Again")    
    except mysql.connector.DatabaseError as db:
        print("your Problem in MySQL db",db)

      
