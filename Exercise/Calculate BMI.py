#menu
def choice():
    print("1: Height in inches")
    print("2: Height in meters")
    print("3: Exit")

#error message
class error():
    def both(): # for both invalid input
        print("Both input are invalid. Please enter a valid input.")
    def height(): # for height invalid input
        print("Your height is invalid.Please enter a valid input.")
    def weight(): # for weight invalid input
        print("Your weight is invalid.Please enter a valid input.")
        
#display menu + request for choice
choice()
unit = input("Please enter your choice: ")

#loop so that the system no need to rerun again
while unit != "3":
    
    #if the user's input is 1
    if unit == "1":
        
        #request for inputs
        weight = input("Please enter your weight: ")
        height = input("Please enter your height: ")
        status = "fail"           #initial value to run the loop
        
        while status != "pass":
            
            #validate inputs
            #if all the inputs are numbers
            if weight.isdigit() == True and height.isdigit() == True:
                BMI = (int(weight) / pow(int(height),2))*703   #calculation
                print(f"Your BMI is {BMI:.2f}")
                print("")
                status = "pass"   #to stop the "status" while loop
        
                choice()
                unit = input("Please enter your choice: ")      
            
            #if both inputs are not numbers
            elif weight.isdigit() == False and height.isdigit() == False:
                error.both()
                weight = input("Please enter your weight: ")
                height = input("Please enter your height: ") 
            
            #if height's input is not number
            elif height.isdigit() == False:
                error.height()
                height = input("Please enter your height: ")   
             
            #if weight's input is not number  
            elif weight.isdigit()  == False:
                error.weight()
                weight = input("Please enter your weight: ")
                
    # if the user input is 2       
    elif unit == "2":
        
        #request for inputs
        weight = input("Please enter your weight: ")
        height = input("Please enter your height: ")
        status = "fail"     #initial value to run the loop
        
        while status != "pass":
            
            #validate inputs
            #if all the inputs are numbers            
            if weight.isdigit() == True and height.isdigit() == True:
                BMI = int(weight) / pow(int(height),2)   #calculation
                print(f"Your BMI is {BMI:.2f}")
                print("")
                status = "pass"        #to stop the "status" while loop
                
                choice()
                unit = input("Please enter your choice: ")      
            
            #if both inputs are not numbers    
            elif weight.isdigit() == False and height.isdigit() == False:
                error.both()
                weight = input("Please enter your weight: ")
                height = input("Please enter your height: ") 
            
            #if height's input is not number    
            elif height.isdigit() == False:
                error.height()
                height = input("Please enter your height: ")   
              
            #if weight's input is not number    
            elif weight.isdigit()  == False:
                error.weight()
                weight = input("Please enter your weight: ")
     
    #if the user enters other inputs      
    else:
        print("Invalid input! Please enter again.")
        print("")
        
        #request for correct input
        choice()
        unit = input("Please enter your choice: ")        
        