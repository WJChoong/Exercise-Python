def menu():
    print("1: Binary To Decimal and Octal");
    print("2: Decimal To Binary and Octal");
    print("Enter 'x' for exit.");

menu();
choice = input("Your Choice: ");

while choice != 'x':
    
    #chooses 1
    if choice == "1":
        binary = input("Enter any number in Binary Format: ");
        
        #if the input is not a digit
        if binary.isdigit() == False:
            print("Invalid Input! Please enter again");
            print("");
         
        else:
            
            #if input is a binary
            p = set(binary);
            s = {"0", "1"};
            if s == p or p == {'0'} or p == {'1'}: 
                    decimal = int(binary, 2);
                    print(binary,"in Octal =",oct(decimal)[2:]);
                    print(binary,"in Decimmal =",decimal);
                    print("");
                    
                    #choice request
                    menu();
                    choice = input("Your Choice: ");    
           
            #if input is not binary       
            else : 
                print("It's not a binary! Please enter again");    
                print("");   
     
    #chooses 2           
    elif choice == "2":
        decimal = input("Enter any number: "); 
        
        #if the input is not a digit
        if decimal.isdigit() == False:
            print("Invalid Input! Please enter again");
            print("");
         
        else:
            
            #if input is a digit   
            decimal = int(decimal)
            print(decimal,"in Octal =",oct(decimal)[2:]);
            print(decimal,"in binary =",bin(decimal)[2:]);
            print("");
            
            #choice request
            menu();
            choice = input("Your Choice: ");      
                
    #if input of choice is not valid     
    else: 
        print("Please enter a valid choice.");
        print("");
        menu();
        choice = input("Your Choice: ");        
       