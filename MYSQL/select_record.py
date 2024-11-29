import mysql.connector 
def selectrecords():
    try:
        conn=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="12345",
                                     database="mydb2")
        cur=conn.cursor()
        iq="select * from student1"
        cur.execute(iq)
        # conn.commit()
        #for colum name
        metadata=cur.description
        for colinfo in metadata:
            print(colinfo[0],end="\t\t")
        print()  
        records=cur.fetchall()
        for record in records:
            for value in record:
                print(value,end="/t")  
            print()        
        print("your data successfully getting--verify")
    except mysql.connector.DatabaseError as db:
        print("problem in mysql:",db)        
selectrecords()    