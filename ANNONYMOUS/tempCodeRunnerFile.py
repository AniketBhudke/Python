    if val%2==0:
        return True
    else:
        return False


lst=[int(val) for val in input("Enter a list of values:").split()]
obj=filter(sum,lst)

print(list(obj))
