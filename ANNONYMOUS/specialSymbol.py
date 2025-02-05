# #Basic program
#filter function only return true value
# def sum(val):
#     if val%2==0:
#         return True
#     else:
#         return False


# lst=[int(val) for val in input("Enter a list of values:").split()]
# obj=filter(sum,lst)

# print(list(obj))
#--------------------------------------------------------------------
#program
lst=[int(val) for val in input("Enter a list of values:").split()]
obj=filter(lambda val:val%2==0,lst)

print(list(obj))
#----------------------------------------------------------------------
#basic program
# sum=lambda val:val%2==0
# lst=[int(val) for val in input("Enter a list of values:").split()]
# obj=filter(sum,lst)

# print(list(obj))
#------------------------------------------------------------------------------

#palindrome line
# sum=lambda word:word==word[::-1]
# lst=[word for word in input("enter A string:").split()]
# lst=filter(sum,lst)
# print(list(lst))
#---------------------------------------------------------

#accept list of numerical value and find the odd number separately by using filter function
# odd=lambda val:val%2==0
# lst=[int(val) for val in input().split()]
# obj=filter(odd,lst)
# c=list(obj)
# print(c)
#------------------------------------------------------------------

#will get those word whose length ranges betweeen 3 to 4
# findfun=lambda word:len(word)==3 or len(word)==4
# lst=[word for word in input().split()]
# obj=filter(findfun,lst)
# print(list(obj))
#--------------------------------------------------------------

#filter whose words whose first & last letter is same but not palindrome like :window
# same=lambda word:word[0]==word[-1] and word!=word[::-1]
# lst=[word for word in input("Enter a words: ").split()]
# fun=filter(same,lst)
# print(list(fun))
#-----------------------------------------------------------------------------------------

# def templet(sno,sname,marks,crs="python"):
#     print("{},{},{},{}".format(sno,sname,marks,crs))
    
# templet (4,"tanu",90)
# templet (5,"manu",80)
# templet (6,"sanu",70)




# print(2==2)
# print(2=="2")
# # print()

