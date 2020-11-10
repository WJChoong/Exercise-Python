#Sum of digit in an Integer. Examples: users enter 3141 , the program should display 3+1+4+1=9

print("Enter x to exit")
number = input("Please enter a number:")

#loop the whole program 
while number != "x":
    
    #if the input is number
    if number.isdigit() == True:
        digit = []   #a blank list to store all digit numbers
        
        #put the digit numbers one by one into the list
        for i in number:
            digit.append(i)
        
        # declare the first value of the variable
        sentence = digit[0]
        total = int(digit[0])
        
        #make the digit's list into sentence and calculate the total
        for i in range(1, len(digit)):
            sentence = sentence + " + " + digit[i]
            total = total + int(digit[i])
            
        #display the output
        print(sentence," = ",total)
        print("")
        
        #request for  input again
        print("Enter x to exit")
        number = input("Please enter a number:")        
        
    else: 
        #error message
        print("Invalid input! Please enter again")
        print("")
        
        #request input again
        print("Enter x to exit")
        number = input("Please enter a number:")        