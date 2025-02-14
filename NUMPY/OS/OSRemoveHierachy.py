import os
try:
    os.removedirs("hyd\\amer\\yellareddyguda\\khan manzil")
except FileNotFoundError:
    print("Folder Does Not Found")
except OSError:
    print("Ensure ur Folder Is empty")        