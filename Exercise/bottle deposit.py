def choices():
    print("""1: Calculate the price of bottle
2: Exit""")

def invalid(inp):
    print("Invalid Input for"+ inp)
    print("")
    
choices()
choice_inp = input("Please Choose An Option: ")
while choice_inp != "2":
    if choice_inp != "1":
        invalid("choice!")
        choices()
        choice_inp = input("Please Choose An Option: ")        
    else:
        small_bottle = input("Numbers of bottle holding 1 liter or less: ")#first input
        #let user enter first correct input
        if small_bottle.isdigit() == False:        
            invalid(" the first input!")
        else:
            big_bottle = input("Numbers of bottle holding more than 1 liter: ")#second input
            #let user enter first correct input
            while big_bottle.isdigit() == False:
                invalid(" the second input!")
                big_bottle = input("Numbers of bottle holding more than 1 liter: ")
                
             #calculate the price
            small_bottle = int(small_bottle)*0.10
            big_bottle = int(big_bottle)*0.25
            total = small_bottle + big_bottle 
            
            #print the exact output with correct format
            print("Total cost is ${:.2f}".format(total))
            print("")
            choices()
            choice_inp = input("Please Choose An Option: ")                
