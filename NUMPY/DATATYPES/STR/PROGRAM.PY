                    # 0     1       2       3       4       5

                    # P     Y       T       H       O       N

                    #-6     -5      -4     -3       -2     -1

s="PYTHON"
print(s)

# print(s[0:4])
# print(s[4:0])
# print(s[::-1])
# print(s[0:1000:])
# print(s[-1:-50:-1])


# in string have five syntax to slicing
# 1-   strobj[Begin:End]  # ++ -- +- -+
# 2-   strobj[Begin: ]
# 3-   strobj[:End]
# 4-   strobj[:]
# 5--- strobj[Begin:End:Step]--- R-1  R-2  R-3  R-4  R-5

                    # 0     1       2       3       4       5

                    # P     Y       T       H       O       N

                    #-6     -5      -4     -3       -2     -1

# 1-   strobj[Begin:End]
# Examples: if  +VE BEGIN : +VE END  then BEGIN<END is Considered
# print(s[0:6])
# print(s[6:1000])
# print(s[0:23])

# if  -VE BEGIN : -VE END  then BEGIN<END is Considered
# print(s[-6:-1])
# print(s[-5:-3])
# print(s[-1:-4]) # -1+1=0 condition not satisfy
# print(s[-1:-3])

# if +VE BEGIN : -VE END   then BEGIN<END is Ignored
# print(s[1:-4])  #-------------Y
# print(s[5:-3])
# print(s[3:-5])
# print(s[4:-5])

#if -VE BEGIN : +VE END   then BEGIN<END is Ignored
# print(s[-2:100:])  #-2+1=-1   -1+1=0  0-1=-1 -1+1=0

                    # 0     1       2       3       4       5

                    # P     Y       T       H       O       N

                    #-6     -5      -4     -3       -2     -1

# 2-   strobj[Begin: ]
# print(s[0:]) #------------PYTHON
# print(s[3:]) #------------HON
# print(s[-1:]) #-----------N
# print(s[-3:]) #----------HON
# print(s[-5:]) #----------YTHON
# print(s[-1000:]) #-------PYTHON
# print(s[::-1])  #--------NOHTYP

# 3-   strobj[:End]
# print(s[:5])
# print(s[:100])
# print(s[:-1])
# print(s[:-100]) #------''

# 4-   strobj[:]
# print(s[:])

# 5--- strobj[Begin:End:Step]--- R-1  R-2  R-3  R-4  R-5

#predefined function in string----
#1) capitalize()
# 2) title()
# 3) swapcase()
# 4) lower()
# 5) upper()
# 6) count()
# 7) islower()
# 8) isupper()
# 9) isdigit()
# 10) isalpha()
# 11) isalnum()
# 12) split()   OR  split("delimeter")
# 13) join(Iterable Object)
# 14) index()
# 15) lstrip()
# 16) rstrip()
# 17) strip()
# 18) startswith()
# 19) endswith()

#------------------------------------------------------------------------------
#Note: we can modify,update the string but at different memory address as shown following.
#--------------------------------------------------------------------------------------------

#1) capitalize()
# a="python"
# b="programming"
# print(a,id(a))  #--------------python 2306097188464
# c=a.capitalize()
# print(c,id(c)) #---------------Python 2306101050864

# 2) title()
# a="python programming "
# print(a,id(a))  #--------------python programming  2001696391216
# c=a.title()
# print(c,id(c)) #---------------Python Programming  2001696391456

# 3) swapcase()-----convert uppercase into and lower into upper
# a="Python programming "
# print(a,id(a))  #--------------Python programming  2145534804016
# c=a.swapcase()
# print(c,id(c)) #---------------pYTHON PROGRAMMING  2145534804096

# # 4) lower()
# a="Python programming "
# print(a,id(a))  #--------------Python programming  2174402101296
# c=a.lower()
# print(c,id(c)) #---------------python programming  2174402101376

#5.upper
# a="Python programming "
# print(a,id(a))  #--------------Python programming  2957915914288
# c=a.upper()
# print(c,id(c)) #---------------PYTHON PROGRAMMING  2957915914368

#6.count
# a="PythonProgramming "
# print(a,id(a))  
# print(a.count('P'))  #-----2

#7.islower
# a="python programming "
# print(a,id(a))  #--------------Python programming  2957915914288
# print(a.islower())  #----False  

# #8.isupper
# a="PYTHON abc "
# print(a,id(a))  #--------------Python programming  2957915914288
# print(a.isupper())  #----False

#9.isdigit()  -----purily digit then true otherwise false
# a='23lqjf'
# print(a.isdigit())

#10.isalpha()----purily alphabhet then it is return true otherwise false
# a="python"
# print(a.isalpha()) 

# # 11.isalnum()----alphabhet and number present it return true otherwise false
# a="%$#"
# print(a.isalnum())  #----False

