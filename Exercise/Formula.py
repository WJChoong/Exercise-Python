'''
Write a program that reads a positive interger, n, form the user and hen displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula: sum = (n)(n+1)/2
'''
status = 0

#check input
while status == 0:
    try:
        n = int(input("Please enter a number:"))
        if n > 0:
            status = 1
        else:
            print("Please enter a positive value")
    except:
        print("Please enter a number")
        
#calculate
sum = (n*(n+1))/2
print(sum)
