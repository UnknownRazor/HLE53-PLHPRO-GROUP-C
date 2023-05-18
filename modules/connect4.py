from random import randrange
import tkinter as tk

player = 1
player2 = 2
array = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         ]

def array_maker(size):
    array = []
    while True:
        count = 0
        arrays = []
        while count < size:
            arrays.append(0)
            count += 1
        array.append(arrays)
        if len(array) == size:
            break
    return array


def findpos(user_choice, array):
    counter = 0
    for arrays in array:
        if(arrays[user_choice] == 1 or arrays[user_choice] == 2):
            break
        else:
            counter += 1
    if counter == 0:
        counter = - 1
    return counter

def choice(array, player, user_choice, button_array,img_array=[]):
    change = findpos(user_choice, array)
    if change == - 1:
        print("Column is full make another choice")
        return -1
    else:
        array[change-1][user_choice] = player


        button = button_array[change - 1][user_choice]
        if player == 1:
            button.config(image=img_array[1])
        else:
            button.config(image=img_array[2])
        return 0



class Player:
    def __init__(self, name, wins, loss, draws):
        self.name = name
        self.wins = wins
        self.loss = loss
        self.draws = draws
        self.score = wins - loss
    def get_att(self):
        return (self.name, self.score, self.wins, self.loss, self.draws)


def winner(grid):
    win = horizontal_four(grid)
    if(win):
        return win
    win = vertical_four(grid)
    if (win):
        return win
    win = diagonal_four(grid)
    if (win):
        return win
    win = anti_diagonal_four(grid)
    if (win):
        return win


# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις οριζόντια
def horizontal_four(grid):
    # για κάθε γραμμή (0 έως 5)
    # ελέγχει τις θέσεις των στηλών (0 έως 3),(1 έως 4),(2 έως 5),(3 έως 6)
    for row in range(0, 6):
        #  η αρχική στήλη της τετράδας column
        for column in range(0, 4):
            # αν 4 διαδοχικές θέσεις μιας γραμμής είναι ίδιες
            four_same = (grid[row][column] == grid[row][column + 1]) and \
                        (grid[row][column + 1] == grid[row][column + 2]) and \
                        (grid[row][column + 2] == grid[row][column + 3])
            # αν οι 4 θέσεις δεν είναι κενές
            if four_same and grid[row][column] != 0:
                # επιστρέφει το νικητή
                winner = grid[row][column]
                return winner
    return None # δε βρέθηκε νικητής






# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις κάθετα
def vertical_four(grid):
    # για κάθε στήλη (0 έως και 6)
    # ελέγχει τις θέσεις των γραμμών (0 έως 3),(1 έως 4),(2 έως 5)
    for column in range(0, 7):
        # η αρχική γραμμή της τετράδας row
        for row in range(0, 3):
            # αν 4 διαδοχικές θέσεις μιας στήλης είναι ίδιες
            four_same = (grid[row][column] == grid[row + 1][column]) and \
                        (grid[row + 1][column] == grid[row + 2][column]) and \
                        (grid[row + 2][column] == grid[row + 3][column])
            # αν οι 4 θέσεις δεν είναι κενές
            if four_same and grid[row][column] != 0:
                # επιστρέφει το νικητή
                winner = grid[row][column]
                return winner
    return None # δε βρέθηκε νικητής


# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις στις κυρίως διαγώνιους
def diagonal_four(grid):
    # για κάθε γραμμή που μπορεί να ξεκινήσει διαγώνιος (0 έως 2)
    # ελέγχει τις διαδοχικές διαγώνιες θέσεις
    for row in range(0, 3):
        for column in range(0, 4):
            # αν 4 διαδοχικές διαγώνιες θέσεις είναι ίδιες
            four_same = (grid[row][column] == grid[row + 1][column + 1]) and \
                        (grid[row + 1][column + 1] == grid[row + 2][column + 2]) and \
                        (grid[row + 2][column + 2] == grid[row + 3][column + 3])
            # αν οι 4 θέσεις δεν είναι κενές
            if four_same and grid[row][column] != 0:
                # επιστρέφει το νικητή
                winner = grid[row][column]
                return winner
    return None  # δε βρέθηκε νικητής


# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις αντίθετες διαγώνιους
def anti_diagonal_four(grid):
    # για κάθε γραμμή που μπορεί να ξεκινήσει διαγώνιος (3 έως 5)
    # ελέγχει τις αντίθετες διαδοχικές διαγώνιες θέσεις
    for row in range(3, 6):
        for column in range(0, 4):
            # αν 4 διαδοχικές αντίθετες διαγώνιες θέσεις είναι ίδιες
            four_same = (grid[row][column] == grid[row - 1][column + 1]) and \
                        (grid[row - 1][column + 1] == grid[row - 2][column + 2]) and \
                        (grid[row - 2][column + 2] == grid[row - 3][column + 3])
            # αν οι 4 θέσεις δεν είναι κενές
            if four_same and grid[row][column] != 0:
                # επιστρέφει το νικητή
                winner = grid[row][column]
                return winner
    return None  # δε βρέθηκε νικητής
def test(array):
    global player, player2
    for i in range(21):
        user_choice = randrange(0, 7)
        change = findpos(user_choice, array)
        choice(change, player)
        user_choice = randrange(0, 7)
        change = findpos(user_choice, array)
        choice(change, player2)
        won = (winner(array))
        if(won):
            break
    for arrays in array:
        print(arrays)
    if(won == None):
        print("Ισοπαλία")
    else:
        print(won, "is the", "winner")


def tksleep(t):
    'emulating time.sleep(seconds)'
    ms = int(t*1000)
    root = tk._get_default_root()
    var = tk.IntVar(root)
    root.after(ms, lambda: var.set(1))
    root.wait_variable(var)