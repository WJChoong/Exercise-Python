def menu():
    print("1: Monthly fund")
    print("2: Part time salary")
    print("3: End Program")
    
menu()
choice = input("Your choice: ")
while choice != "3":
    if choice == "1":
        amount = input("Amount of your money; ")
        print("-"*30)
        if amount.isdigit() == True:
            amount = int(amount)
            print("Daily: " + str(amount*0.55))
            print("Self: " + str(amount*0.1))
            print("Investment: " + str(amount*0.1))
            print("Travel: " + str(amount*0.05))
            print("Long: " + str(amount*0.1))
            print("gf: " + str(amount*0.05))
            print("Dream: " + str(amount*0.05))
            print()
            menu()
            choice = input("Your choice: ")  
            
        elif amount.isdigit() ==  False:        
            print("Not a valid input! Program ends")
            print()
        
    elif choice == "2":
        print("Please choose the amount of money:")
        print("1: >RM1000")
        print("2: <RM1000")
        
        money = input("How much is the money: ")
        if money.isdigit() == True:
            if money == "1":
                amount = input("Amount of your money; ")
                print("-"*30)
                if amount.isdigit() == True:
                    amount = int(amount)
                    long = amount//2
                    print("Long: " + str(long))
                    print("Daily: " + str(long*0.2))
                    print("Self: " + str(long*0.2))
                    print("Investment: " + str(long*0.2))
                    print("Travel: " + str(long*0.2))
                    print("gf: " + str(long*0.1))
                    print("Dream: " + str(long*0.1))                    
                    print()
                    menu()
                    choice = input("Your choice: ")  
                    
                elif amount.isdigit() ==  False:
                    print("Not a valid input! Program ends")
                    print()
                    
            elif money == "2":
                amount = input("Amount of your money: ")
                print("-"*30)
                if amount.isdigit() == True:
                    amount = float(amount)
                    print("Long: " + str(amount*0.2))
                    print("Daily: " + str(amount*0.1))
                    print("Self: " + str(amount*0.1))
                    print("Investment: " + str(amount*0.2))
                    print("Travel: " + str(amount*0.2)) 
                    print("gf: " + str(amount*0.1))
                    print("Dream: " + str(amount*0.1)) 
                    print()
                    menu()
                    choice = input("Your choice: ")  
                    
                elif amount.isdigit() ==  False:
                    print("Not a valid input! Program ends") 
                    print()
            else:
                print("worng choice!")
                print()
        else: 
            print("Please enter a number")
            print()
    else: 
        print("Invalid input")
        print()
        menu()
        choice = input("Your choice: ")        
            