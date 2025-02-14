from nameexcept import InvalidNameError,LengthZeroError,SpaceError
from validation import validationName

try:
    name=input("enter A name:")
    res=validationName(name)
except InvalidNameError:
    print("Please Enter Valid Name")  
except LengthZeroError:
    print("Enter The character")
except SpaceError:
    print("Please dont Enter the space")   
else:
    print(f"{res} is a valid Name")           