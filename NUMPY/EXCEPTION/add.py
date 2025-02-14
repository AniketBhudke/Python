from adddemo import addop
from numberwrongError import DivisionByZeroError

try:
    a=int(input("Enter A 1st Number: "))
    b=int(input("Enter A 2nd Number: "))
    d=addop(a,b)
except DivisionByZeroError:
    print("Please Enter non zero value:")  
else:
    print(f"sum={d}")
    
