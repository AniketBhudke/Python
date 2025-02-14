from StudentMenu import menu
from  StudentAdd  import savestuddata
from StudentViews import getallrecords,getrecord
from StudentDelete import deleterecord
from StudentUpdate import updaterecord
from StudentSearch import searchrecord
menu()
try:
    ch=int(input("Enter A choice:"))
    match(ch):
        case 1:
           savestuddata()
        case 2:
            getallrecords()
        case 3:
            getrecord()
        case 4:
            deleterecord()
        case 5:
            updaterecord()
        case 6:
            searchrecord()
        case 7:
            print("Thnx For Using These App")
        case _:
            print("Ur Selection Of Operation IS Wrong")    
except ValueError:
    print("Dont Enter Alnums,Str or Number")