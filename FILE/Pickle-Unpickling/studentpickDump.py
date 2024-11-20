import pickle
def studentData():
    with open("pick.data",'+ab')as fp:
        studentName=input("Enter A Name Of The Student")   
        studentSno=int(input("Enter A Student Number:"))
        StudentMrk=float(input("Enter A Mark Of The Student: "))
        l=list()
        l.append(studentName)
        l.append(studentSno)
        l.append(StudentMrk)
        pickle.dump(l,fp)
        
studentData()
