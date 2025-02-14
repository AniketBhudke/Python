from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError,WithdrawError,InSuffFundError


while(True):
    try:
        ch=int(input("Enter a choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("Enter Valid Amount")
                else:
                    print("deposit Operation Successfully:")
            case 2:
                try:
                    withdraw()
                except WindowsError:
                    print("Please Enter the withdraw amount") 
                except InSuffFundError:
                    print("Ensufficient Fund to WithDraw")
                except ValueError:
                        print("Don't try to Withdraw alnums,strs and symbols")     
            case 3:
                    balenq ()
            case 4:
                print("thnx for these application")
            case _:
                    print("Ur Selection of Operation is wrong--try again")
    except ValueError:
        print("Don't enter alnums,strs and symbols for Choice-try again")                                                
