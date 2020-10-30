week_inp = input("Choose Weekday or Weekend Pass (WD/WE): ")
month_inp = input("Is today in the month of May (Y/N): ")
ticket_inp= int(input("Number of ticket you want: "))

price=0
child=0
adult=0
senior=0
for i in range (ticket_inp):
    print("Ticket "+str(i+1))
    age_inp = int(input("Enter your age: "))
    express_inp = input("Upgrade to Express Pass (Y/N): ")
    if age_inp <= 12:
        child =child +1
        if week_inp == "WD":
            if month_inp == "Y":
                price =price + 34
            else:
                price =price + 40
            if express_inp == "Y":
                price = price + 20
        else:
            if month_inp == "Y":
                price =price + 42
            else:        
                price =price + 50
            if express_inp == "Y":
                price = price + 33
    
    elif age_inp >= 65:
        senior =senior +1
        if week_inp == "WD":
            if month_inp == "Y":
                price =price + 17
            else:        
                price =price + 20
            if express_inp == "Y":
                price = price + 20
        else:
            if month_inp == "Y":
                price = price + 29
            else:        
                price = price + 35
            if express_inp == "Y":
                price = price + 33
    
    else:
        adult =adult+1
        if week_inp == "WD":
            if month_inp == "Y":
                price =price +  46
            else:        
                price =price + 55
            if express_inp == "Y":
                price = price + 20
        else:
            if month_inp == "Y":
                price =price + 55
            else:        
                price =price + 65
            if express_inp == "Y":
                price = price + 33    
               
print("Total ticket for child is "+ str(child))
print("Total ticket for adult is "+ str(adult))
print("Total ticket for senior is "+ str(senior))
print("The total cost is $"+str(price))