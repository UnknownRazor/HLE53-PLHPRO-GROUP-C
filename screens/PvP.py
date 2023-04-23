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


def play(player):
    while True:
        try:
            print_board(array)
            user_choice = int(input(f"Player {player}, enter column (1-7): ")) - 1
        except ValueError:
            print ("\n Invalid input. Try again. \n")
            continue
        if (user_choice>=0 and user_choice<=6):
            break
        else:
            print ("\n invalid column \n")
            continue
    if findpos(user_choice, player):
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        print("\n Invalid move. Try again. \n")
        return False
    return True

player = 1
while True:
         if play(player):
             player = 2
         if play(player):
             player = 1
         

    # Έλεγχος για νίκη
    # (code to check for four in a row in any direction)
