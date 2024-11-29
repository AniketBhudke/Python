import mysql.connector
def selectAllreacords():
    try:
        conn=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="12345",
                                    database="studentinformationsystem")
        cur=conn.cursor()
        q="select * from StudentInformation"
        cur.execute(q)
        #to get column name
        column_name=cur.description
        for column in column_name:
            print(column[0], end="\t")
        print()    
        #to get Data from student information table 
        records=cur.fetchall()
        for record in records:
            for val in record:
                print(val,end="\t")
            print()        
    except mysql.connector.DatabaseError as db:
        print("Problem in MySQl db:",db)


