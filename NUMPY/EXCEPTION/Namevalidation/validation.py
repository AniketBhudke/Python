from nameexcept import LengthZeroError,InvalidNameError,SpaceError
def validationName(name):
    if (len(name)==0):
        raise LengthZeroError
    elif (name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        res=True
        for word in words:
            if (not word.isalpha()):
                res=False
                break
        if (res):
            return name 
        else:
            raise  InvalidNameError   
    