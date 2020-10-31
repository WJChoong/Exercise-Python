#Compute the taxt and tip for a restaurant meal
cost = input("Enter the cost of the meal: ")

#validate input
while cost.isdigit() == False:
    print("Invalid input, Please enter a valid input")
    cost = input("Enter the cost of the meal: ")
    
cost = int(cost)            #change data type

tax = cost*0.3              #calculate tax
tip = cost* 0.18            #calculate tip
total = cost + tax + tip    #calculate total 

#Output
print("The amount of tax is $%.2f" %(tax))
print("The amount of tip is $%.2f" %(tip))
print("The grand total of the meal is $%.2f"%(total))