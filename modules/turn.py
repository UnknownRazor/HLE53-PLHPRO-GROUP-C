import math
import copy
from winner import *
from random import randrange

EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2
COMPUTER = 2


# Επιστρέφει την κατώτερη κενή θέση (γραμμή)
# Αν είναι γεμάτες όλες οι θέσεις, επιστρέφει -1
def find_position(grid, user_choice):
    counter = 0
    for row in grid:
        if row[user_choice] == 1 or row[user_choice] == 2:
            break
        else:
            counter += 1
    return counter - 1


# Επιλογή στήλης που θα αφήσει το πιόνι ο παίκτης
def choose_column(grid):
    # η στήλη πρέπει να είναι ακέραιος αριθμός (0-6)
    while True:
        try:
            column = int(input("Choose a Column: "))-1
            # αν πληκτρολόγησε αριθμό που δεν αντιστοιχεί σε στήλη
            if column not in range(len(grid[0])):
                print("This Column doesn't exist!")
                continue
        except ValueError:
            # δεν πληκτρολόγησε ακέραιο
            print("Wrong input!")
            continue
        return column


# Βρίσκει όλες τις πιθανές στήλες που μπορεί να τοποθετηθεί πιόνι
# επιστρέφει μια λίστα των στηλών
def possible_cols(grid):
    cols = []
    # αν υπάρχει κενή θέση στην πρώτη(επάνω) γραμμή
    # την προσθέτει στη λίστα
    for col in range(len(grid[0])):
        if grid[0][col] == 0:
            cols.append(col)
    return cols


# Μετράει πόσα όμοια πιόνια βρίσκονται σε σειρά
# και υπολογίζει το score
def calculate(boxes):
    score = 0
    # maximazing (αύξηση score ανάλογα με τα πιόνια)
    if boxes.count(2) == 4:
        score += 100
    elif boxes.count(2) == 3:
        score += 50
    elif boxes.count(2) == 2:
        score += 10
    # minimizing (μείωση score ανάλογα με τα πιόνια)
    if boxes.count(1) == 4:
        score -= 100
    elif boxes.count(1) == 3:
        score -= 50
    elif boxes.count(1) == 2:
        score -= 10

    return score


# ελέγχει ολόκληρο το ταμπλό και υπολογίζει το score
# δημιουργώντας τετράδες
def evaluate(grid):
    score = 0

    # οριζόντια
    for row in range(len(grid)):
        for column in range(len(grid[0]) - 3):
            boxes = [grid[row][column], grid[row][column + 1], grid[row][column + 2], grid[row][column + 3]]
            score += calculate(boxes)
    # κάθετα
    for column in range(len(grid[0])):
        for row in range(len(grid)-3):
            boxes = [grid[row][column], grid[row+1][column], grid[row+2][column], grid[row+3][column]]
            score += calculate(boxes)
    # διαγώνια
    for row in range(len(grid)-3):
        for column in range(len(grid[0])-3):
            boxes = [grid[row][column], grid[row+1][column + 1], grid[row+2][column + 2], grid[row+3][column + 3]]
            score += calculate(boxes)
    # αντιδιαγώνια
    anti_grid = [[grid[row][column] for column in range(len(grid[0]) - 1, -1, -1)] for row in range(len(grid))]
    for row in range(len(anti_grid) - 3):
        for column in range(len(anti_grid[0]) - 3):
            boxes = [anti_grid[row][column], anti_grid[row + 1][column + 1], anti_grid[row + 2][column + 2],
                    anti_grid[row + 3][column + 3]]
            score += calculate(boxes)

    return score


# Αλγόριθμος minimax
def minimax(grid, depth, maximizing_player):
    valid_locations = possible_cols(grid)
    is_terminal = game_over(grid)
    if depth == 0 or is_terminal:
        return evaluate(grid)

    if maximizing_player:   # υπολογιστής
        value = -math.inf
        for col in valid_locations:
            row = find_position(grid, col)
            b_copy = copy.deepcopy(grid)
            b_copy[row][col] = COMPUTER
            new_score = minimax(b_copy, depth-1, False)
            value = max(value, new_score)
        return value
    else:   # minimazing player (παίκτης)
        value = math.inf
        for col in valid_locations:
            row = find_position(grid, col)
            b_copy = copy.deepcopy(grid)
            b_copy[row][col] = PLAYER1
            new_score = minimax(b_copy, depth-1, True)
            value = min(value, new_score)
        return value


# Επιλογή θέσης(στήλης) βάση Minimax από τον υπολογιστή για τοποθέτηση του πιονιού
def hard(grid):
    computer_column = None
    depth = 4    # επίπεδο δυσκολίας Minimax
    best_score = -float('inf')  # αρχικοποίηση στο μείον άπειρο
    # βρίσκει την καταλληλότερη στήλη για να τοποθετήσει το πιόνι
    for col in range(len(grid[0])):
        computer_row = find_position(grid, col)
        if computer_row != -1:
            new_grid = copy.deepcopy(grid)
            new_grid[computer_row][col] = COMPUTER
            score = minimax(new_grid, depth, False)
            if score > best_score:
                best_score = score
                computer_column = col
    return computer_column


# Επιλογή τυχαίας θέσης από τον υπολογιστή και τοποθέτηση του πιονιού
def easy(grid):
    while True:
        # ο υπολογιστής διαλέγει μια τυχαία στήλη
        computer_column = randrange(len(grid[0]))
        # εύρεση κενής θέσης (γραμμής)
        computer_row = find_position(grid, computer_column)
        # αν υπάρχει κενή θέση
        if computer_row != -1:
            break
    # ο υπολογιστής καταλαμβάνει την κενή θέση
    # grid[computer_row][computer_column] = player
    return computer_column




# Επιλογή θέσης από τον υπολογιστή και τοποθέτηση του πιονιού
def computer_turn(grid, level):
    # ο υπολογιστής επιλέγει level (easy ή hard)
    if level == '1':
        computer_column = easy(grid)
    else:
        computer_column = hard(grid)
    # εύρεση κενής θέσης (γραμμής)
    computer_row = find_position(grid, computer_column)
    # ο υπολογιστής καταλαμβάνει την κενή θέση
    grid[computer_row][computer_column] = COMPUTER
    return


# Επιλογή θέσης από τον παίκτη και τοποθέτηση του πιονιού
def player_turn(grid, player):
    # ο παίκτης επιλέγει στήλη
    player_column = choose_column(grid)
    # εύρεση κενής θέσης (γραμμής)
    player_row = find_position(grid, player_column)
    # αν η στήλη είναι γεμάτη, διαλέγει άλλη στήλη
    while player_row == -1:
        print("This Column is Full!")
        player_column = choose_column(grid)
        player_row = find_position(grid, player_column)
    # ο παίκτης καταλαμβάνει την κενή θέση
    grid[player_row][player_column] = player
    return