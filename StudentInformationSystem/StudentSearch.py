import pickle
def searchrecord():
    try:
        with open("NIT.data","rb") as fp:
            records=[]
            while(True):
                try:
                    record=pickle.load(fp)
                    records.append(record)
                except EOFError:
                    break
            #Get Student Number from KBD to get Other Details from File
            try:
                sno=int(input("Enter Student Number to get Other Details:"))
                found=False
                for record in records:
                    if(sno==record[0]):
                        found=True
                        break
                if(found):
                    print("\tStudent Number:{}".format(record[0]))
                    print("\tStudent Name:{}".format(record[1]))
                    print("\tStudent Marks:{}".format(record[2]))
                else:
                    print("Student Record Does Not Exist ")
            except ValueError:
                print("Don't enter Alnums,strs and symbols for sno--try again")

    except FileNotFoundError:
        print("File Does not Exist")