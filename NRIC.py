NRIC=input("Enter your NRIC: ")
if len(NRIC)==9:
    NRIC.upper()
    if NRIC.startswith("T") and NRIC[8].isupper:
        num= NRIC[1:8]
        if num.isdigit():
            num= int(num)
            total= (NRIC[1]*2)+(NRIC[2]*7)+(NRIC[3]*6)+(NRIC[4]*5)+(NRIC[5]*4)+(NRIC[6]*3)+(NRIC[7]*2)
            remain=(total+4)%11     
            if remain==0 and NRIC.endswith("J"):
                print("Valid NRIC.")
            elif remain==1 and NRIC.endswith("Z"):
                print("Valid NRIC.")                
            elif remain==2 and NRIC.endswith("I"):
                print("Valid NRIC.")            
            elif remain==3 and NRIC.endswith("H"):
                print("Valid NRIC.")
            elif remain==4 and NRIC.endswith("G"):
                print("Valid NRIC.")
            elif remain==5 and NRIC.endswith("F"):
                print("Valid NRIC.")
            elif remain==6 and NRIC.endswith("E"):
                print("Valid NRIC.")
            elif remain==7 and NRIC.endswith("D"):
                print("Valid NRIC.")
            elif remain==8 and NRIC.endswith("C"):
                print("Valid NRIC.")
            elif remain==9 and NRIC.endswith("B"):
                print("Valid NRIC.")
            elif remain==10 and NRIC.endswith("A"):
                print("Valid NRIC.")  
            else:
                print("Invalid NRIC.")            
        else:
            print("Invalid NRIC")
    else:
        print("Invalid NRIC")
else:
    print("Invalid NRIC")