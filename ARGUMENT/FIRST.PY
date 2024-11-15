# #POSITIONAL ARGUMENTS
# def info(sname,sid,sclass):
#     print(f"student Name={sname}")
#     print(f"student Id={sid}")
#     print(f"student Class={sclass}")
    

# info("sagr",34,"BCA")    
# #Program for Demonstrating Positional arguments
# #PossArgsEx1.py
# def dispstudinfo(sno,sname,marks):
# 	print("\t{}\t{}\t{}".format(sno,sname,marks))

# #Main Program
# print("*"*50)
# print("\tSNO\tNAME\tMARKS")
# print("*"*50)
# dispstudinfo(100,"RS",45.67) # Function Call with Pos Args
# dispstudinfo(200,"TR",75.67) # Function Call with Pos Args
# dispstudinfo(300,"KV",15.67) # Function Call with Pos Args
# dispstudinfo(sname="JH",marks=34.56,sno=400) # Function Call with Key word args
# dispstudinfo(500,marks=56.78,sname="DR") # Function Call with Pos Args and Key word args
# #dispstudinfo(marks=56.78,600,sname="SS") ---SyntaxError: positional argument follows keyword argument
# dispstudinfo(marks=56.78,sno=600,sname="SS") # Function Call with Key word args
# #dispstudinfo(700,"RD")---TypeError: dispstudinfo() missing 1 required positional argument: 'marks'
# print("*"*50)

#DEFAULT AGGUMENT
# def student(sname,sid,course='PYTHON'):
#     print(f"{sname} \t {sid} \t {course} ")

# student("sagar",89)

#Keyword variable length argument
def student(sname,sid,sclass,city="HYD",*values,**param):
    s=0
    print("------------------------------")
    print(f"Name of the student ={sname} ")
    print(f"Id of the Student ={sid}")
    print(f"Class of the Student ={sclass}")
    print(f"City of the Student={city}")
    for value in values:
        s=s+value
    print(f"Total marks of the student={s}")
    for key,value in param.items():
        print(key,value)
    
student("sagar",1,"BCA",34,56,66,89) 
student("HARSH",2,"BSC",34,56,66,89,56,physics=44,math=44,bio=100) 

