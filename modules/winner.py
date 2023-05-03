# len(grid)    : αριθμός γραμμών
# len(grid[0]) : αριθμός στηλών

# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις οριζόντια
def horizontal_four(grid):
    # για κάθε γραμμή (0 έως και την τελευταία)
    # ελέγχει τις θέσεις των στηλών (0 έως 3),(1 έως 4),(2 έως 5),(3 έως 6),...
    for row in range(len(grid)):
        #  η αρχική στήλη της τετράδας column
        for column in range(len(grid[0])-3):
            # αν 4 διαδοχικές θέσεις μιας γραμμής είναι ίδιες
            four_same = (grid[row][column] == grid[row][column + 1]) and \
                        (grid[row][column + 1] == grid[row][column + 2]) and \
                        (grid[row][column + 2] == grid[row][column + 3])
            # αν οι 4 θέσεις δεν είναι κενές
            if four_same and grid[row][column] != 0:
                # επιστρέφει το νικητή
                winner = grid[row][column]
                return winner
    return None  # δε βρέθηκε νικητής


# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις κάθετα
def vertical_four(grid):
    # για κάθε στήλη (0 έως και την τελευταία)
    # ελέγχει τις θέσεις των γραμμών (0 έως 3),(1 έως 4),(2 έως 5),...
    for column in range(len(grid[0])):
        # η αρχική γραμμή της τετράδας row
        for row in range(len(grid)-3):
            # αν 4 διαδοχικές θέσεις μιας στήλης είναι ίδιες
            four_same = (grid[row][column] == grid[row + 1][column]) and \
                        (grid[row + 1][column] == grid[row + 2][column]) and \
                        (grid[row + 2][column] == grid[row + 3][column])
            # αν οι 4 θέσεις δεν είναι κενές
            if four_same and grid[row][column] != 0:
                # επιστρέφει το νικητή
                winner = grid[row][column]
                return winner
    return None  # δε βρέθηκε νικητής


# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις στις κυρίως διαγώνιους
def diagonal_four(grid):
    # για κάθε γραμμή που μπορεί να ξεκινήσει διαγώνιος (0 έως και 3 πριν το τέλος)
    # ελέγχει τις διαδοχικές διαγώνιες θέσεις
    for row in range(len(grid)-3):
        for column in range(len(grid[0])-3):
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


# Αντιστρέφει το ταμπλό (ως προς τις στήλες)
# η τελευταία στήλη γίνεται πρώτη, η προτελευταία δεύτερη κτλ.
# Ελέγχει αν υπάρχουν 4 όμοιες θέσεις στις κυρίως διαγώνιους
def anti_diagonal_four(grid):
    anti_grid = [[grid[row][column] for column in range(len(grid[0])-1, -1, -1)] for row in range(len(grid))]
    return diagonal_four(anti_grid)


# Ελέγχει αν υπάρχει νικητής και τον επιστρέφει
def check_winner(grid):
    # οριζόντια
    winner = horizontal_four(grid)
    if winner:
        return winner
    # κάθετα
    winner = vertical_four(grid)
    if winner:
        return winner
    # διαγώνια
    winner = diagonal_four(grid)
    if winner:
        return winner
    # αντιδιαγώνια
    winner = anti_diagonal_four(grid)
    if winner:
        return winner


# Ελέγχει αν έχουμε ισοπαλία(γεμάτο ταμπλό) και επιστρέφει True/False
def is_draw(grid):
    # ελέγχει αν υπάρχουν κενές θέσης την πάνω γραμμή
    for column in range(7):
        # εφόσον υπάρχει μία κενή θέση το πλέγμα δεν έχει γεμίσει
        if grid[0][column] == 0:
            return False
    # έχει γεμίσει και η πάνω γραμμή, άρα ολόκληρο το πλέγμα
    # δεν υπήρξε νικητής, Ισοπαλία
    print("---Draw---")
    print("---Game Over---")
    return True


# Παίρνει ως όρισμα το ταμπλό και τους παίκτες
# Ελέγχει αν υπάρχει νικητής/ισοπαλία και επιστρέφει True/False
def game_over(grid):
    winner = check_winner(grid)

    if winner == 1:  # κέρδισε ο παίκτης 1
        return winner
    elif winner == 2:  # κέρδισε ο παίκτης 2
        return winner
    elif is_draw(grid):  # ισοπαλία
        return 0
    # δεν υπάρχει νικητής/ισοπαλία
    return False


# Ενημέρωση στατιστικών παικτών
def update_stats(winner, player1, player2):
    if winner == 1:
        player1.win()
        player2.lose()
    elif winner == 2:
        player2.win()
        player1.lose()
    elif winner == 0:
        player2.draw()
        player1.draw()


# Εμφάνιση νικητή
def print_winner(winner, player1, player2):
    if winner == 1:
        print(f"---{player1.name} Wins---")
    elif winner == 2:
        print(f"---{player2.name} Wins---")
    elif winner == 0:
        print(f"------ Draw ------")
