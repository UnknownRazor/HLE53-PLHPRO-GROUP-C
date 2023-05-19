array = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         ]

def print_board(board):
    for row in board:
        print(row)

def findpos(user_choice, player):
    for row in reversed(array):
        if row[user_choice] == 0:
            row[user_choice] = player
            return True
    return False

player = 1

while True:
    # Player 1's turn
    while True:
        try:
            print_board(array)
            user_choice = int(input("Player 1, enter column (1-7): ")) - 1
            if user_choice>=0 and user_choice<=6:
                break
            else:
                print ("\n invalid column play again \n")
        except ValueError:
            print ("\n invalid input, play again \n")
    if findpos(user_choice, player):
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        print("Invalid move. Try again.")
        continue
    print ("\n \n")
    # Έλεγχος για νίκη
    # (code to check for four in a row in any direction)

    # Player 2's turn
    import random
    while True:
        user_choice = random.randint(0,6)
        if findpos(user_choice, player):
            print(f"player's 2 move is in column no{user_choice+1}")
            break
        else:
            continue
    if player == 1:
        player = 2
    else:
        player = 1
    print ("\n \n")
    
    # Έλεγχος για νίκη
    # (code to check for four in a row in any direction)
