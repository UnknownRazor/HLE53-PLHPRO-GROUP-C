import copy
from modules.data import *
from random import randrange
from modules.player import Player

EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2
COMPUTER = 2
ROWS = 6
COLUMNS = 7
MAX_COL = 10
MAX_ROW = 10

class Game:
    def __init__(self):
        # δημιουργία κενού ταμπλό
        self.rows = ROWS
        self.columns = COLUMNS
        self.grid = self.create_grid(self.rows, self.columns)
        self.result = None
        self.message = None
        self.player1 = Player("")
        self.player2 = Player("Computer")

    def create_grid(self, rows, columns):
        return [[EMPTY for column in range(columns)] for row in range(rows)]

    # Εύρεση κατώτερης κενής θέσης
    def find_position(self, grid, selected_column):
        # αναζήτηση στις γραμμές για την κατώτερη κενή θέση(0)
        for row in range(len(grid)):
            # αν βρεθεί γεμάτη θέση επιστρέφει την προηγούμενη γραμμή(κενή)
            # αν ολόκληρη η στήλη είναι γεμάτη, επιστρέφει -1
            if grid[row][selected_column] != 0:
                return row-1
        # αν ολόκληρη η στήλη είναι κενή επιστρέφει την τελευταία γραμμή
        return row


    # Επιλογή στήλης που θα αφήσει το πιόνι ο παίκτης
    def choose_column(self):
        # η στήλη πρέπει να είναι ακέραιος αριθμός (0-6)
        while True:
            try:
                column = int(input("Choose a Column: "))-1
                # αν πληκτρολόγησε αριθμό που δεν αντιστοιχεί σε στήλη
                if column not in range(len(self.grid[0])):
                    print("This Column doesn't exist!")
                    continue
            except ValueError:
                # δεν πληκτρολόγησε ακέραιο
                print("Wrong input!")
                continue
            return column


    # Βρίσκει όλες τις πιθανές στήλες που μπορεί να τοποθετηθεί πιόνι
    # επιστρέφει μια λίστα των στηλών
    def possible_cols(self, grid):
        cols = []
        # αν υπάρχει κενή θέση στην πρώτη(επάνω) γραμμή
        # την προσθέτει στη λίστα
        for col in range(len(grid[0])):
            if grid[0][col] == 0:
                cols.append(col)
        return cols


    # Μετράει πόσα όμοια πιόνια βρίσκονται σε σειρά
    # και υπολογίζει το score
    def calculate(self, boxes):
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
    def evaluate(self, grid):
        score = 0

        # οριζόντια
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0]) - 3):
                boxes = [grid[row][column], grid[row][column + 1], grid[row][column + 2], grid[row][column + 3]]
                score += self.calculate(boxes)
        # κάθετα
        for column in range(len(self.grid[0])):
            for row in range(len(self.grid)-3):
                boxes = [grid[row][column], grid[row+1][column], grid[row+2][column], grid[row+3][column]]
                score += self.calculate(boxes)
        # διαγώνια
        for row in range(len(self.grid)-3):
            for column in range(len(self.grid[0])-3):
                boxes = [grid[row][column], grid[row+1][column + 1], grid[row+2][column + 2], grid[row+3][column + 3]]
                score += self.calculate(boxes)
        # αντιδιαγώνια
        anti_grid = [[grid[row][column] for column in range(len(grid[0]) - 1, -1, -1)] for row in range(len(grid))]
        for row in range(len(anti_grid) - 3):
            for column in range(len(anti_grid[0]) - 3):
                boxes = [anti_grid[row][column], anti_grid[row + 1][column + 1], anti_grid[row + 2][column + 2],
                         anti_grid[row + 3][column + 3]]
                score += self.calculate(boxes)

        return score


    # Αλγόριθμος minimax
    def minimax(self, grid, depth, maximizing_player):
        valid_locations = self.possible_cols(grid)
        is_terminal = self.game_over()
        if depth == 0 or is_terminal:
            return self.evaluate(grid)

        if maximizing_player:   # υπολογιστής
            value = -float('inf')
            for col in valid_locations:
                row = self.find_position(grid, col)
                b_copy = copy.deepcopy(grid)
                b_copy[row][col] = COMPUTER
                new_score = self.minimax(b_copy, depth-1, False)
                value = max(value, new_score)
            return value
        else:   # minimazing player (παίκτης)
            value = float('inf')
            for col in valid_locations:
                row = self.find_position(grid, col)
                b_copy = copy.deepcopy(grid)
                b_copy[row][col] = PLAYER1
                new_score = self.minimax(b_copy, depth-1, True)
                value = min(value, new_score)
            return value


    # Επιλογή θέσης(στήλης) βάση Minimax από τον υπολογιστή για τοποθέτηση του πιονιού
    # depth : επίπεδο δυσκολίας
    def hard(self, depth):
        computer_column = None
        best_score = -float('inf')  # αρχικοποίηση στο μείον άπειρο
        # βρίσκει την καταλληλότερη στήλη για να τοποθετήσει το πιόνι
        for col in range(len(self.grid[0])):
            computer_row = self.find_position(self.grid, col)
            if computer_row != -1:
                new_grid = copy.deepcopy(self.grid)
                new_grid[computer_row][col] = COMPUTER
                score = self.minimax(new_grid, depth, False)
                if score > best_score:
                    best_score = score
                    computer_column = col
        return computer_column


    # Επιλογή τυχαίας θέσης από τον υπολογιστή και τοποθέτηση του πιονιού
    def easy(self):
        while True:
            # ο υπολογιστής διαλέγει μια τυχαία στήλη
            computer_column = randrange(len(self.grid[0]))
            # εύρεση κενής θέσης (γραμμής)
            computer_row = self.find_position(self.grid, computer_column)
            # αν υπάρχει κενή θέση
            if computer_row != -1:
                break
        # ο υπολογιστής καταλαμβάνει την κενή θέση
        # grid[computer_row][computer_column] = player
        return computer_column


    # Επιλογή θέσης από τον υπολογιστή και τοποθέτηση του πιονιού
    def computer_turn(self, level):
        # ο υπολογιστής επιλέγει level (easy ή hard)
        if level == '1':
            computer_column = self.easy()
        elif level == '2':
            computer_column = self.hard(1)
        else:   # level = '3'
            computer_column = self.hard(3)
        # εύρεση κενής θέσης (γραμμής)
        computer_row = self.find_position(self.grid, computer_column)
        # ο υπολογιστής καταλαμβάνει την κενή θέση
        self.grid[computer_row][computer_column] = COMPUTER
        return computer_row, computer_column


    # Επιλογή θέσης από τον παίκτη και τοποθέτηση του πιονιού
    def player_turn(self, player, player_column):
        # εύρεση κενής θέσης (γραμμής)
        player_row = self.find_position(self.grid, player_column)
        # αν η στήλη είναι γεμάτη, διαλέγει άλλη στήλη
        if player_row == -1:
            return player_row
        # ο παίκτης καταλαμβάνει την κενή θέση
        self.grid[player_row][player_column] = player
        return player_row

    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις οριζόντια
    def horizontal_four(self):
        # για κάθε γραμμή (0 έως και την τελευταία)
        # ελέγχει τις θέσεις των στηλών (0 έως 3),(1 έως 4),(2 έως 5),(3 έως 6),...
        for row in range(len(self.grid)):
            #  η αρχική στήλη της τετράδας column
            for column in range(len(self.grid[0]) - 3):
                # αν 4 διαδοχικές θέσεις μιας γραμμής είναι ίδιες
                four_same = (self.grid[row][column] == self.grid[row][column + 1]) and \
                            (self.grid[row][column + 1] == self.grid[row][column + 2]) and \
                            (self.grid[row][column + 2] == self.grid[row][column + 3])
                # αν οι 4 θέσεις δεν είναι κενές
                if four_same and self.grid[row][column] != 0:
                    # επιστρέφει το νικητή
                    winner = self.grid[row][column]
                    return winner
        return None  # δε βρέθηκε νικητής

    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις κάθετα
    def vertical_four(self):
        # για κάθε στήλη (0 έως και την τελευταία)
        # ελέγχει τις θέσεις των γραμμών (0 έως 3),(1 έως 4),(2 έως 5),...
        for column in range(len(self.grid[0])):
            # η αρχική γραμμή της τετράδας row
            for row in range(len(self.grid) - 3):
                # αν 4 διαδοχικές θέσεις μιας στήλης είναι ίδιες
                four_same = (self.grid[row][column] == self.grid[row + 1][column]) and \
                            (self.grid[row + 1][column] == self.grid[row + 2][column]) and \
                            (self.grid[row + 2][column] == self.grid[row + 3][column])
                # αν οι 4 θέσεις δεν είναι κενές
                if four_same and self.grid[row][column] != 0:
                    # επιστρέφει το νικητή
                    winner = self.grid[row][column]
                    return winner
        return None  # δε βρέθηκε νικητής

    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις στις κυρίως διαγώνιους
    def diagonal_four(self):
        # για κάθε γραμμή που μπορεί να ξεκινήσει διαγώνιος (0 έως και 3 πριν το τέλος)
        # ελέγχει τις διαδοχικές διαγώνιες θέσεις
        for row in range(len(self.grid) - 3):
            for column in range(len(self.grid[0]) - 3):
                # αν 4 διαδοχικές διαγώνιες θέσεις είναι ίδιες
                four_same = (self.grid[row][column] == self.grid[row + 1][column + 1]) and \
                            (self.grid[row + 1][column + 1] == self.grid[row + 2][column + 2]) and \
                            (self.grid[row + 2][column + 2] == self.grid[row + 3][column + 3])
                # αν οι 4 θέσεις δεν είναι κενές
                if four_same and self.grid[row][column] != 0:
                    # επιστρέφει το νικητή
                    winner = self.grid[row][column]
                    return winner
        return None  # δε βρέθηκε νικητής

    # Αντιστρέφει το ταμπλό (ως προς τις στήλες)
    # η τελευταία στήλη γίνεται πρώτη, η προτελευταία δεύτερη κτλ.
    # Ελέγχει αν υπάρχουν 4 όμοιες θέσεις στις κυρίως διαγώνιους
    def anti_diagonal_four(self):
        anti_grid = [[self.grid[row][column] for column in range(len(self.grid[0]) - 1, -1, -1)] for row in
                     range(len(self.grid))]
        for row in range(len(anti_grid) - 3):
            for column in range(len(anti_grid[0]) - 3):
                # αν 4 διαδοχικές διαγώνιες θέσεις είναι ίδιες
                four_same = (anti_grid[row][column] == anti_grid[row + 1][column + 1]) and \
                            (anti_grid[row + 1][column + 1] == anti_grid[row + 2][column + 2]) and \
                            (anti_grid[row + 2][column + 2] == anti_grid[row + 3][column + 3])
                # αν οι 4 θέσεις δεν είναι κενές
                if four_same and anti_grid[row][column] != 0:
                    # επιστρέφει το νικητή
                    winner = anti_grid[row][column]
                    return winner
        return None  # δε βρέθηκε νικητής

    # Ελέγχει αν υπάρχει νικητής και τον επιστρέφει
    def check_winner(self):
        # οριζόντια
        winner = self.horizontal_four()
        if winner:
            return winner
        # κάθετα
        winner = self.vertical_four()
        if winner:
            return winner
        # διαγώνια
        winner = self.diagonal_four()
        if winner:
            return winner
        # αντιδιαγώνια
        winner = self.anti_diagonal_four()
        if winner:
            return winner

    # Ελέγχει αν έχουμε ισοπαλία(γεμάτο ταμπλό) και επιστρέφει True/False
    def is_draw(self):
        # ελέγχει αν υπάρχουν κενές θέσης την πάνω γραμμή
        for column in range(7):
            # εφόσον υπάρχει μία κενή θέση το πλέγμα δεν έχει γεμίσει
            if self.grid[0][column] == 0:
                return False
        # έχει γεμίσει και η πάνω γραμμή, άρα ολόκληρο το πλέγμα
        # δεν υπήρξε νικητής, Ισοπαλία
        return True

    # Παίρνει ως όρισμα το ταμπλό και τους παίκτες
    # Ελέγχει αν υπάρχει νικητής/ισοπαλία και επιστρέφει True/False
    def game_over(self):
        if self.check_winner() == 1:  # κέρδισε ο παίκτης 1
            self.result = 1
            self.message = "Player 1 Wins"
            return 1
        elif self.check_winner() == 2:  # κέρδισε ο παίκτης 2
            self.result = 2
            self.message = "Player 2 Wins"
            return 2
        elif self.is_draw():  # ισοπαλία
            self.result = 3
            self.message = "Draw"
            return 3
        # δεν υπάρχει νικητής/ισοπαλία
        return False

    # Ενημέρωση στατιστικών παικτών
    def update_stats(self):
        if self.result == 1:
            self.player1.win()
            self.player2.lose()
        elif self.result == 2:
            self.player2.win()
            self.player1.lose()
        elif self.result == 3:
            self.player2.draw()
            self.player1.draw()
