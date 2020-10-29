def menu():
    print("Enter 1: Laksa - $3.50")
    print("Enter 2: Nasi Lemak - $3.00")
    print("Enter 3: Popiah - $1.80")
    print("Enter 4: Mee Siam - $2.50")
    print("Enter -9: Exit")

total= 0
order=[ ]
menu()    
choice=input("Enter item code: ")
while choice!="-9":
    if choice== "1":
        total=total+3.50
        order.append("Laksa")
        print("You have ordered Laksa - $3.50")
    elif choice=="2":
        total=total+3.00 
        order.append("Nasi Lemak")
        print("You have ordered Nasi Lemak - $3.00")        
    elif choice=="3":
        total=total+1.80 
        order.append("Popiah")
        print("You have ordered Popiah - $1.80")        
    elif choice=="4":
        total=total+2.50      
        order.append("Mee Siam")
        print("You have ordered Mee Siam - $2.50")        
    menu()
    choice=input("Enter item code: ")
print(order)
print("Total is "+ str(total))
print("Completed. Thank you.")