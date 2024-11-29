from AddStudentData import insertStudentData
from viewAllStudentData import selectAllreacords
from viewSingleRecord import viewSingleRecored
from deleteStudentData import deleteStudentData
from updateStudentData import updateStudentData
from searchStudent import searchData
from menu import menu
def studentMenu():
    try:
        while(True):
            menu()
            print("===================================================")
            ch=int(input("Enter a choice:"))
            print("===================================================")
            match(ch):
                case 1:
                    insertStudentData()
                case 2:
                    selectAllreacords()
                case 3:
                    viewSingleRecored()
                case 4:
                    deleteStudentData()
                case 5:
                    updateStudentData()
                case 6:
                    searchData()
                case 7:
                    print("Thnx For Using This Program")
                    exit
                case _:
                    print("Your Selction Of Operation Is Wrong--Try Again")    
    except ValueError:
        print("Don't Enter Alnums,Stars and Symbols,Enter a correct value")
studentMenu()