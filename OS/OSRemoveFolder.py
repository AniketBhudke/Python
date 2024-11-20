import os
try:
    os.rmdir("osfiles\\a")
    print("Filed Removed Successfully")
except FileNotFoundError:
    print("File Not Found--Try Again") 
except OSError:
    print("Ensure Ur Folder Must Be Empty") #---------jr smja folder chya andaar folder asl aani amhi aapn direct root folder ch delete kru tevha he error yete      