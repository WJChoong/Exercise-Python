import math

class error():
    def both():
        print("Both input are invalid! Please enter again.")
        print("")
    def first():
        print("The first input is invalid! Please enter again.")
        print("")
    def sec():
        print("The second input is invalid! Please enter again.")
        print("")

#first input
first_lat = input("Please enter the first latitude: ")
first_long = input("Please enter the first longtitude: ")

#validate inputs
while first_lat.isdigit() !=True or first_long.isdigit() != True:
    
    if first_lat.isdigit() != True and first_long.isdigit() != True:
        error.both()
        first_lat = input("Please enter the first latitude: ")
        first_long = input("Please enter the first longtitude: ")   
        
    elif first_lat.isdigit() != True:
        error.first()
        first_lat = input("Please enter the first latitude: ")     
        
    elif first_long.isdigit() != True:
        error.sec()
        first_long = input("Please enter the first longtitude: ")    

#second input
sec_lat = input("Please enter the second latitude: ")
sec_long = input("Please enter the second longtitude: ")

#validate inputs
while sec_lat.isdigit() !=True or sec_long.isdigit() != True:
    
    if sec_lat.isdigit() != True and sec_long.isdigit() != True:       
        error.both()
        sec_lat = input("Please enter the second latitude: ")
        sec_long = input("Please enter the second longtitude: ")   
        
    elif sec_lat.isdigit() != True:
        error.first()
        sec_lat = input("Please enter the second latitude: ")     
        
    elif sec_long.isdigit() != True:
        error.sec()
        sec_long = input("Please enter the second longtitude: ")
        
#calculation
first_lat = int(first_lat)
first_long = int(first_long)
sec_lat = int(sec_lat)
sec_long = int(sec_long)

distance = 6371.01 * math.acos(math.sin(first_lat)) * math.sin(sec_lat) +\
           math.cos(first_lat) * math.cos(sec_lat) * math.cos(first_long - sec_long)

#display output
print("The distance is {:.3f}km.".format(distance))