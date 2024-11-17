import pickle
def deleterecord():
    try:
        with open("NIT.data","rb") as rp:
            records=list()#declare one list to append the data
            while(True):
                try:
                    record=pickle.load(rp)#we read the data stored in one obj
                    records.append(record)
                except EOFError:   #End Of File
                    break
        #Out-off 'with open() as ' Indentation
        #for record in records:
        #    print(record[0])
        #Accept the student Number and remove
        sno=int(input("Enter Student Number to Remove the Record:"))#we can insert a record you want to delete
        found=False
        for record in records:#records is list
            if(record[0]==sno):#records[0] eka element betate jo edit krya ch aahe toh
                found=True
                delrec=record #jo delete krya ch aahe toh found zala trr toh store krya ch eka object mde
                break
        if(found):
            records.remove(delrec)#records madun toh delete krya ch
            print("Student Record Deleted Sucessfully")
            with open("NIT.data","wb") as wp:
                for record in records:#for record in records:#
                    pickle.dump(records,wp)#write
        else:
            print("Record Does not Exist")
    except FileNotFoundError:
        print("File Does not Exist")