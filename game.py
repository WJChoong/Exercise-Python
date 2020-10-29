import random
highest_num = 100
lowest_num = 0

def check():
    if inp_num < rand_num and inp_num < lowest_num :
        print("Please number within the range! ! !")
    elif inp_num > rand_num and inp_num > highest_num:
        print("Please number within the range! ! !")
        
rand_num = random.randint(1,101)
print(rand_num)

inp_num = int(input("Please enter a number: "))
If inp_num.isdigit() == True:
    inp_num = int(inp_num)
Else:
    print("Enter a number! ! !")
check()

while inp_num != rand_num:
    if inp_num < rand_num and inp_num > lowest_num :
        lowest_num = inp_num
    elif inp_num > rand_num and inp_num < highest_num:
        highest_num = inp_num
    print("Range: " + str(lowest_num) + " - " + str(highest_num))
    inp_num = int(input("Please enter a number: "))
    If inp_num.isdigit() == True:
        inp_num = int(inp_num)
    Else:
        print("Enter a number! ! !")    
    check()
    
print("You have got the correct answer! ! !")