from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500
def deposit():
    amount=int(input("Enter the AMount that you can Deposit:"))
    if (amount<=0):
        raise DepositError
    else:
        global bal
        bal=bal+amount
        print(f"Ur accounnt xxxxx123 Deposit with INR={amount}")
        print(f"Now Ur accounnt xxxxx123 Balance INR={bal}")

def withdraw():
    global bal
    amount=int(input("EEnter the amount thatr you can withdraw:"))
    if (amount<=0):
        raise WithdrawError
    elif ((amount+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-amount
        print(f"your account xxxx123 has been withdraw {amount} ")
        print(f"Your account Balance ={bal}")  

def balenq():
    print("ur account balanace xxx1233 of INR:{bal}")