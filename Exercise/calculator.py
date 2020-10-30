def option():
    print("Press 1: Area of circle")
    print("Press 2: Circumference of circle")
    print("Press 3: Area and Circumference")
    print("Press 9: Exit")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    
option()
choice= input("Enter option: ")
while choice!="9":
    if choice=="1":
        print("Calculate Area")
        radius=float(input("Enter radius: "))
        total= 3.142*radius*radius
        print("Area of circle is "+str(total))
    elif choice=="2":
        print("Calculate Circumference")
        radius=float(input("Enter radius: "))
        total= 2*3.142*radius
        print("Circumference of circle is "+str(total))
    elif choice=="3":
        print("Calculate Area and Circumference") 
        radius=float(input("Enter radius: "))
        total= 3.142*radius*radius
        print("Area of circle is "+str(total))
        total= 2*3.142*radius
        print("Circumference of circle is "+str(total)) 
    else: 
        print("Please enter a valid number")
    print("")
    option()
    choice= input("Enter option: ")
    
print("End of program")