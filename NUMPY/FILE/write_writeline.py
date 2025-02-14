#perform write operation ---by using write()--w
# with open("aniket.data","w")as fp:
#      fp.write(str(100)+"  ")
#      fp.write("rossum" + "   ")
#      fp.write(str(12.34))
#      print("Data Written to the file ---varify")

#overlapped the data if we enter agian in the file
# with open("aniket.data","w")as fp:
#      fp.writelines(str(200)+"  ")
#      fp.write("raj rossum" + "   ")
#      fp.write(str(12.349))
#      print("Data Written to the file ---varify")

#no-overlapping
# with open("aniket.data","a")as fp:
#      fp.write("/n" + str(100)+"  ")
#      fp.write("rossum" + "   ")
#      fp.write(str(12.34))
#      print("Data Written to the file ---varify")

#--------------------------------------------
#               writeline
#-------------------------------------------------
# x=[10,"sagu",44,"aniket","hyd","emfjf"]
# with open("aniket.data",'w') as p:
#     p.write(str(x))
#     print("Data Written to the File--Verify")


#
# empno=int(input("Enter a employee Number: "))
# empname=input("Enter a employee Name: ")
# empsal=float(input("Enter a Employee salary:"))

# with open("aniket.data",'+a')as fp:
#     fp.write(str(empno)+"/t")
#     fp.write((empname)+"/t")
#     fp.write(str(empsal)+"/t")
#     print("data written to the file successfully--verify")