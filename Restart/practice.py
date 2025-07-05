while True:
    try:
        while True:
            current_price=int(input("Enter The Current Price:"))
            last_price=int(input("Enter The Last Price:"))
            Buy_price=int(input("Enter The Buy Price:"))
            if (current_price>last_price):
                print("Buy")
                break
            elif  current_price<last_price>Buy_price:
                print("sell") 
                break
            else:
                print("Enter Price Correctly:") 
                continue
    except ValueError:
        print("Please Enter the values In Numbers Only:")





