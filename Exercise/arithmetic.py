import math

#Both inputs
a = input("Please enter the first input: ")
b = input("Please enter the second input: ")

#validate inputs
while a.isdigit() !=True or b.isdigit() != True:
    if a.isdigit() != True and b.isdigit() != True:
        print("Both input are invalid! Please enter again.")
        a = input("Please enter the first input: ")
        b = input("Please enter the second input: ")        
    elif a.isdigit() != True:
        print("The first input is invalid! Please enter again.")
        a = input("Please enter the first input: ")        
    elif b.isdigit() != True:
        print("The second input is invalid! Please enter again.")
        b = input("Please enter the second input: ")    
        
# change data type 
a = int(a)
b = int(b)

#process data to output
print("The sum is " + str(a + b))
print("The difference is " + str(b - a))
print("The product is " + str(a * b))
print("The quotient when a divided by b is " + str(a // b))
print("The remainder when a is divided by b " + str(a % b))
print("The result of log a is " + str(math.log(a, 10)))
print("The result of a to the power of b is " + str(pow(a,b)))