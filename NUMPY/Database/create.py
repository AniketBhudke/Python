# import oracledb as orc
# def database():
#     try:
#         con=orc.connect("ANIKET/1234@localhost/orcl")
#         cu=con.cursor()
#         ct="create table A(cno number(2) primary key,cname varchar2(10) not null)"
#         cu.execute(ct)
#         print("Python program created successfully")
#     except orc.DatabaseError as db:
#         print(db)  
# database()          


# import oracledb as orc #step-1
# def createTable():
#     try:
#         con=orc.connect("system/12345@Localhost/orcl") #step-2
#         cur=con.cursor() #step-3
#         ct="create table Schools1(roll_No number(2) primary key,s_Name varchar2(10) not null,s_Marks number(5))"
#         cur.execute(ct)
#         print("Table Created Successfully--Verify")
#     except orc.DatabaseError as db:
#         print(db)    

# createTable()


# import oracledb as orc
# def createtable():
#     try:
#         conn=orc.connect("ANIKET/1234@localhost/orcl")
#         cur=conn.cursor()
#         q=input("Enter a query of database:")
#         cur.execute(q)

#         print("Table Created Successfully-----Verify")
#     except orc.DatabaseError as db:
#         print("problem",db)

# createtable()

# import oracledb as orc 
# class Teacher:
#     def createTable(self):
#         conn=orc.connect("ANIKET/1234@Localhost/orcl")
#         cur=conn.cursor()
#         iq="create table Teacher(TName varchar(20),TFaculty varchar(20),TNumber number(20))"
#         cur.execute(iq)
#         print("Table Created Successfully----Verify")

# s1=Teacher()
# s1.createTable()

# import oracledb as orc
# class Teacher:
#     def insertData(self):
#         try:
#             conn=orc.connect("ANIKET/1234@Localhost/orcl")
#             cur=conn.cursor()
#             self.name=input("Enter Name OF Teacher:")
#             self.faculty=input("Enter Faculty OF The TEacher:")
#             self.number=int(input("Enter The Teacher Number:"))
#             iq="insert into TEACHER values('%s','%s',%d)"
#             cur.execute(iq %(self.name,self.faculty,self.number))
#             conn.commit()
#             print("Data Inserted Successfully---Verify")
#         except orc.DatabaseError as db:
#             print("Problem in Oracle DB",db)
# t1=Teacher()
# t1.insertData()


