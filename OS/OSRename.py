import os
try:
    os.rename("osfiles\\a\\abc.data","osfiles\\a\\abcd.data")
    print("Folder Names Verify Successfully")
except FileNotFoundError:
    print("File does not found")    