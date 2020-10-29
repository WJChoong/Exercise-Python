# 1st-5th station is 0.70
# after= 0.30

station_inp= int(input("Enter the number of stations: "))
amount_input= float(input("Enter the amount in your ezlink card: "))

def calc_mrt_fare(station_inp):
    if station_inp<6:
        total= station_inp*0.7
    else:
        total= ((station_inp-5)*0.3)+(5*0.7)
    return total

if amount_input<calc_mrt_fare(station_inp):
    status= "Please top up your card."
else:
    status= "You have sufficient funds in your card."

print("You  have to pay $"+ str(calc_mrt_fare(station_inp))+ " for your MRT ride.")
print(status)