# fetchmany-----aaplya jevdhe pahijat tevdhe Dete
#1.()---return all record
#2.(0)----return 0 record 
#3.(5)-----return 5 record 
#4.(100)----return all record 
#5.(-5)----returns 0 record 
#fetchmany------purna record dete
#fetchone-------eka ch record dete
#description[0]----return column name


# import oracledb as orc # Step-1
# def insertrecord():
#     try:
#         con=orc.connect("ANIKET/1234@localhost/ORCL") #Step-2
#         cur=con.cursor() # Step-3
#         #Step-4
#         iq="drop table "
#         #ctq="create table bharat(cno number(2) primary key,cname varchar2(10) not null)"
#         cur.execute(iq) # Step-5
#         con.commit()
#         print("Employee Record Inserted Sucessfully") #Step-6

#     except orc.DatabaseError as db:
#         print("Problem in Oracle DB:",db)

# #Main Program
# insertrecord() # Function Call

#dynamically
# import oracledb as orc
# def inserDynamically():
#     while(True):
#         try:
#             conn=orc.connect("ANIKET/1234@localhost/orcl")
#             cur=conn.cursor()
#             Name=input("Enter a name:")
#             Roll_No=int(input("Enter a Roll Number:"))
#             faculty=input("Enter a Faculty:")
#             marks=int(input("Enter a marks:"))
#             iq="insert into STUDENT1 values('%s',%d,'%s',%d)"
#             cur.execute(iq % (Name,Roll_No,faculty,marks))    
#             conn.commit()
#             print(f"your data inserted successfully--Verify {cur.rowcount}")
#             ch=input("Do you want to insert data yes/no:")
#             if ch.lower()== "no":
#                 print("Thnx for using these program")
#                 break
#         except orc.DatabaseError as c:
#             print("Problem in database db:",c)    
# inserDynamically()


# import oracledb as orc
# def selecttable():
#     try:
#         conn=orc.connect("ANIKET/1234@Localhost/orcl")
#         cur=conn.cursor()
#         iq="SELECT * FROM STUDENT1"
#         cur.execute(iq)
#         rec=cur.description
#         for metadata in rec:
#             print(metadata[0])
#         records=cur.fetchall()
#         for record in records:
#             for value in record:
#                 print(value)    
#     except orc.DatabaseError as db_error:
#         print("The problem in oracle db",db_error)

# selecttable()


# import oracledb as orc
# def selecttable():
#     try:
#         conn=orc.connect("ANIKET/1234@Localhost/orcl")
#         cur=conn.cursor()
#         iq="SELECT * FROM STUDENT1"
#         cur.execute(iq)
#         rec=cur.description
#         for metadata in rec:
#             print(metadata[0])
#         records=cur.fetchone()
#         for record in records:
#             print(record)    
#     except orc.DatabaseError as db_error:
#         print("The problem in oracle db",db_error)


# selecttable()

import oracledb as orc
def selecttable():
    try:
        conn=orc.connect("ANIKET/1234@Localhost/orcl")
        cur=conn.cursor()
        iq="SELECT * FROM STUDENT1"
        cur.execute(iq)
        rec=cur.description
        for metadata in rec:
            print(metadata[0])
        records=cur.fetchmany(-5)
        for record in records:
            for value in record:
                print(value)    
    except orc.DatabaseError as db_error:
        print("The problem in oracle db",db_error)

selecttable()