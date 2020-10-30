hours= int(input("Enter number of hours: "))

def display_pay(hours):
    if hours<4:
        pay= hours*6  
    elif hours>6:
        pay= ((hours-6)*8)+(3*6)+(3*7)
    else:
        pay= ((hours-3)*7)+(3*6)
    return pay
    
print("Total pay for "+ str(hours)+ "(s): "+str(display_pay(hours)))