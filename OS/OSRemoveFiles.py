import os
try:
    os.remove("osfiles\\a\\ab.data")
    print("Ur File Is Deleted")
except FileNotFoundError:
    print("File Not Found --Try Again")
except OSError:
    print("Ensure Ur Selection Operation Is Wrong")        

