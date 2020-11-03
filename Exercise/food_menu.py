def menu():
    print("Press 1: Big Mac Meal- $6.75")
    print("Press 2: McNuggets Meal- $5.85")
    print("Press 3: Filet-O-Meal- $5.25")
    print("Press 4: McChicken Meal- $5.65")
    print("Press 5: McSpicy Meal- $6.35")
    print("Press 0: Exit")
    print("***********************************************************")

def output(food,price):
    orderList.append(food)
    print("You have ordered "+ food+"- "+str(price))

orderList=[]
total=0
menu()
order= input("Enter meal code: ")
while order!="0":
    if order=="1":
        total=total+6.75
        output("Big Mac Meal",6.75)
    elif order=="2":
        total= total+5.85
        output("McNuggets Meal",5.85)
    elif order=="3":
        total= total+5.25
        output("Filet-O-Meal",5.25)
    elif order=="4":
        total= total+5.65
        output("McChicken", 5.65)
    elif order=="5":
        total= total+6.35
        output("McSpicy Meal",6.35)
    print("")
    menu()
    order= input("Enter meal code: ")
    
print('\n')
print("Thank you.")    
print("You have ordered: "+ str(orderList))
print(f'Please pay: ${total}')
