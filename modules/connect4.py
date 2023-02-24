from random import randrange

player = 1
player2 = 2
array = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         ]
def findpos(user_choice):
    counter = 0
    for arrays in array:
        if(arrays[user_choice] == 1 or arrays[user_choice] == 2):
            break
        else:
            counter+=1
            print(counter)
    if counter == 0:
        counter = - 1
    return counter

def choice(change, player):
    if change == - 1:
        print("Column is full make another choice")
    if change != - 1:
        array[change-1][user_choice] = player

for i in range(5):
    user_choice = randrange(0, 7)
    change = findpos(user_choice)
    choice(change, player)
    user_choice = randrange(0, 7)
    change = findpos(user_choice)
    choice(change, player2)
for arrays in array:
    print(arrays)
