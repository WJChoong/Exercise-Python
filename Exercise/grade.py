result=[]
score=[]


for grade in range(1,14):
    result_inp=input("Enter your CA grade for week "+ str(grade)+ " <A/B/C/D/F/X/LOA> : ")
    result.append(result_inp)
    if result_inp=="A":
        score.append(4.0)
    elif result_inp=="B":
        score.append(3.0)
    elif result_inp=="C":
        score.append(2.0)
    elif result_inp=="D":
        score.append(1.0)
    elif result_inp=="F":
        score.append(0.0)
    elif result_inp=="X":
        score.append(0.0)        
    elif result_inp=="LOA":
        score.append("LOA")    
print("Your CA grade for 13 weeks: "+ str(result))
print(str(score))

