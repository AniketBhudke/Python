import sys
class spaceNameError(Exception):pass
class InvalidNumberError(Exception):pass
class zeroLengthError(Exception):pass
import mysql.connector

class nameValidation:
    def validation(self,name):
        if len(name)==0:
            raise zeroLengthError
        elif (name.isspace()):
            raise spaceNameError
        else:
            words=name.split()
            res=True
            for word in words:
                if(not word.isalpha()):
                    res=False
                    break
            if (res):
                return name
            else:
                raise InvalidNumberError


class student:
    def readstuddata(self):
        try:
            self.sno=int(input("Enter a Student Number:"))
            self.name=nameValidation().validation(input("Enter A Student Name:"))
            self.marks=int(input("Enter The Marks Of the Student:"))
        except ValueError:
            print("Don't Enter Alnums,Stars And Symbols:")
        except spaceNameError:
            print("Don't Enter The Space IN the Name:")
        except  InvalidNumberError:
            print("Don't Enter Inavlid Number:")
        except zeroLengthError:
            print("Enter The Charter:")
        else:
            self.displayStudData()

    def displayStudData(self):
        print(f"Student Number ={self.sno}")
        print(f"Student Name ={self.name}")
        print(f"Student Marks ={self.marks}")
        self.savestuddata()

    def savestuddata(self) :
        try:
            conn=mysql.connector.connect(host="localhost",
                                         user="root",
                                         passwd="12345",
                                         database="mydb2")
            cur=conn.cursor()
            iq="insert into student values(%d,'%s',%d)"
            cur.execute(iq %(self.sno,self.name,self.marks))
            conn.commit()
            print("Daata inserted In Table Successfully--Verify")
        except mysql.connector.DatabaseError as db:
            print("Problem in mysql is ",db) 

s1 =student()
s1.readstuddata()


        