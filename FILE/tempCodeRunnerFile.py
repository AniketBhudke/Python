try:
    with open("sd.data",'x') as fp:
        print("File created Successsfully..!")
        print(f"Mode of the Files ={fp.mode}")
        print(f"Name of the Files ={fp.name}")
        print(f"Is file open in Writable={fp.writable()}")
        print(f"Is file open in Rritable={fp.readable()}")
except FileExistsError:
    print("File Already Created")
