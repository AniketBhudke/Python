import college
import mysql.connector

class student(college.college):
    def getstddata(self):
        self.sno=int(input("Enter The Number Of The Student:"))
        self.sname=input("Enter The Name Of the Student:")
        self.scrs=input("Enter The course Of The Student:")
        self.getclgdata()
        self.getunivdata()
    def dispstdtdata(self):
        print(f"Number Of The Student:{self.sno}")
        print(f"Name Of the Student:{self.sname}")
        print(f"Course Of The Student:{self.scrs}")  
        self.dispclgdata()
        self.dispunivdata()
    def savestuddata(self):
        try:
            conn=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="12345",
                                        database="univcollstudent")
            cur=conn.cursor()
            iq="insert into unclgstd values(%d,'%s','%s','%s','%s','%s','%s')"
            cur.execute(iq %(self.sno,self.sname,self.scrs,self.cname,self.cloc,self.uname,self.uloc))
            conn.commit()
            print("Your Data In the Table Inserted Successfully---Verify")
        except mysql.connector.DatabaseError as db:
            print("problem in mysql db:",db)   

