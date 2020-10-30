average=[]
descending_order=[]
average2=[]

print("-"*10+" Bowling Scores Statistics for each player "+"-"*10)
for p in range (3):
    score=[]
    highest_score= 0
    print("Player "+str(p+1))
    for game in range(5) :
        mark= input("Enter score for the game "+ str(game+1)+": ")
        score.append(mark)
    
    for i in range(5):
        if int(score[i])>highest_score:
            highest_score= int(score[i])
    lowest_score=int(score[0])
    for i in range(5):
        lowest_score= int(score[i])
            
    average_score=int(score[0])+int(score[1])+int(score[2])+int(score[3])+int(score[4])/5
    average.append(average_score)
    average2.append(average_score)
            
    print("Scores (5 games): "+ str(score))
    print("Average Score: "+str(average_score))
    print("Highest score: "+str(highest_score))
    print("Lowest score: "+ str(lowest_score))
  

print("")
print("-"*10+" Average scores of player in descending order "+"-"*10)

while len(average) > 0:
    highScore = average[0]
    for i in average:
        if i > highScore:
            highScore = i
    descending_order.append(highScore)
    average.remove(highScore)



'''
i= 3
while i > 0: 
    larger_num= 0
    p = len(average)
    while p > 0:
        if average[p-1]> larger_num:
            larger_num = average[p-1]   
            p = p - 1
    average.remove(larger_num)
    descending_order.append(larger_num)    
    i = i -1
'''


print("Average scores of player is descending order: "+str(descending_order))
print(" ")
print("-"*10+" Player's Ranking "+"-"*10)
for i in range(3):
    print("Player " + str(i+1) + "'s average score [" + str(average2[i]) + "] is ranked " + str(descending_order.index(average2[i]) + 1))