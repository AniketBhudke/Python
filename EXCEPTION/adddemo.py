from NumberwrongError import DivisionByZeroError
def addop(a,b):
    if a==0 or b==0:
        raise DivisionByZeroError
    else:
        c=a/b
        return c