# # # set is both mutable & unmutable becoz
# # # mutable becoz in set we can perform add,remove..etc
# # # immutable becoz inn set we can't perform item assignment


# # set1={1,23,4,5,6,7,"sumit","sumit"}
# # print(set1)

# # # pre-defined function
# # # 1.add
# # set1.add(19)
# # print(set1)

# # # 2.remove
# # set1.remove(6)
# # print(set1)

# # #3.discard
# # set1.discard(23)
# # print(set1)

# # # 4.pop
# # set1.pop()
# # print(set1)

# # #5.clear
# # set1.clear()
# # print(set1)



# s1={1,2,3,4}
# # set1.add(12)
# # print(set1)

# s=s1.discard(111)
# print(s)
# print(s1)


# # s1.remove(422)
# # print(s1)






s1={1,2,3,4,5,15}
s2={12,13,14,15}


s3=s1.difference(s2)
print(s3)

# s3=s1.symmetric_difference(s2)
# print(s3)


# s1.difference_update(s2)
# print(s1)

# s1.symmetric_difference_update(s2)
# print(s1)
