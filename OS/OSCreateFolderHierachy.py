import os
try:
    os.makedirs("D:PYTHON BACKEND\\OSs\\A\\B\\C\\D\\E")
    print("Folder Created Successfully---Verify")
except FileExistsError:
    print('Folder Already Exist--Try Again')    