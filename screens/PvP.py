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
    counter = 0
    for row in reversed(array):
        if row[user_choice] == 0:
            row[user_choice] = player
            return True
    return False

player = 1

while True:
    # Player 1's turn
    print_board(array)
    user_choice = int(input("Player 1, enter column (1-7): ")) - 1
    if findpos(user_choice, player):
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        print("Invalid move. Try again.")

    # Έλεγχος για νίκη
    # (code to check for four in a row in any direction)

    # Player 2's turn
    print_board(array)
    user_choice = int(input("Player 2, enter column (1-7): ")) - 1
    if findpos(user_choice, player):
        if player == 1:
            player = 2
        else:
            player = 1
    else:
        print("Invalid move. Try again.")