import math

height = input("Please enter the height: ") #input
status = 0 #initial statement

#validate data
while status == 0:
    if height.isdigit() == False :
        print("""Invalid Input! Please enter a number.
        """)
        height = input("Please enter the height: ")
    else: 
        status = 1

height = int(height) #change data type
accel = 9.8
velocity = 0
result = math.sqrt(math.pow(velocity, 2) + (2 * accel * height))
print(f"The final velocity is {result:.2f} m/s. ")