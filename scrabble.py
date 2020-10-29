import random
bag = ['A','A','A','A','A','A','A','A','A','B','B','C','C','D','D',
       'D','D','E','E','E','E','E','E','E','E','E','E','E','E','F',
       'F','G','G','G','H','H','I','I','I','I','I','I','I','I','I',
       'J','K','L','L','L','L','M','M','N','N','N','N','N','N','O',
       'O','O','O','O','O','O','O','P','P','Q','R','R','R','R','R',
       'R','S','S','S','S','T','T','T','T','T','T','U','U','U','U',
       'V','V','W','W','X','Y','Y','Z']
score = ['A', 1, 'B', 3, 'C', 3, 'D', 2, 'E', 1, 'F', 4, 'G', 2, 
         'H', 4, 'I', 1, 'J', 8, 'K', 5, 'L', 1, 'M', 3,
         'N', 1, 'O', 1, 'P', 3, 'Q', 10, 'R', 1, 'S', 1,
         'T', 1, 'U', 1, 'V', 4, 'W', 4, 'X', 8, 'Y', 4,
         'Z', 10]
list = []

for i in range(7):
    tile = random.choice(bag)
    list.append(tile)
    bag.remove(tile)

insert = input("Form a word with " + str(list) + "or (-1 to quit): ")
while insert != -1 :
    word = insert.upper()          
    score_list = []
    length = len(word)
    p = 0
    total = 0
    while p < length:
        letter = word[p]
        find_letter = int(score.index(letter))
        letter_score = score[find_letter + 1]
        score_list.append(letter_score)
        print(str(letter) + " - " +  str(letter_score))
        list.remove(letter)
        total = total + letter_score
        p = p + 1        
    print("Score List: " + str(score_list))
    print("Point: " + str(total))
    if 7 - len(list) - len(bag) <= 0:
        if len(list) < 7:
            for s in range(7 - len(list)):
                tile = random.choice(bag)
                list.append(tile)      
                bag.remove(tile)
    else:
        for s in range(len(bag)):
            tile = random.choice(bag)
            list.append(tile)      
            bag.remove(tile)        
    insert = input("Form a word with " + str(list) + "or (-1 to quit): ")