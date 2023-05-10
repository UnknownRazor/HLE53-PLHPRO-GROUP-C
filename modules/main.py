from player import Player
from winner import game_over
from turn import *
from data import *

EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2
COMPUTER = 2
MAX_COL = 10
MAX_ROW = 10

# Δημιουργία και αρχικοποίηση ταμπλό σε 0
def create_grid():
    # default 6 γραμμές - 7 στήλες
    col_input = 7
    row_input = 6
    # επιλογή μεγέθους ταμπλό
    while True:
        table_size = input(f"Choose Table size| Classic[6x7] (1) / Custom[5x5 - {MAX_ROW}x{MAX_COL}] (2): ")
        if table_size not in ['1', '2']:
            print("For Classic 1, for Custom 2!")
            continue
        break
    # αλλαγή μεγέθους
    if table_size == '2':
        # έλεγχος αριθμού στηλών
        while True:
            try:
                col_input = int(input("Give Number of Columns: "))
                if col_input not in range(5, MAX_COL+1):
                    print(f"Columns number between 5 to {MAX_COL}")
                    continue
                break
            except ValueError:
                # δεν πληκτρολόγησε ακέραιο
                print("Wrong input!")
                continue
        # έλεγχος αριθμού γραμμών
        while True:
            try:
                row_input = int(input("Give Number of Rows: "))
                if row_input not in range(5, MAX_ROW+1):
                    print(f"Rows number between 5 to {MAX_ROW}")
                    continue
                break
            except ValueError:
                # δεν πληκτρολόγησε ακέραιο
                print("Wrong input!")
                continue
    # δημιουργία ταμπλό
    empty_grid = [[EMPTY for column in range(col_input)] for row in range(row_input)]
    return empty_grid

# Εμφάνιση ταμπλό παιχνιδιού
def print_grid(grid):
    # εμφάνιση γραμμών, η μία κάτω από την άλλη
    for row in grid:
        print(row)


# Παίκτης εναντίον παίκτη
def pvp(grid, pl_1, pl_2):
    print_grid(grid)
    # όσο υπάρχουν κενές θέσεις στο ταμπλό
    while not game_over(grid):
        # παίζει ο παίκτης 1
        print(f"---{pl_1.name}---")
        player_turn(grid, PLAYER1)
        print_grid(grid)
        # έλεγχος αν συμπλήρωσε 4 όμοια
        if game_over(grid):
            break
        # παίζει ο παίκτης 2
        print(f"---{pl_2.name}---")
        player_turn(grid, PLAYER2)
        print_grid(grid)
    return game_over(grid)


# Παίκτης εναντίον υπολογιστή
def pve(grid, pl_1, pl_2, level):
    print_grid(grid)
    # όσο υπάρχουν κενές θέσεις στο ταμπλό
    while not game_over(grid):
        # παίζει ο παίκτης 1
        print(f"---{pl_1.name}---")
        player_turn(grid, PLAYER1)
        print_grid(grid)
        # έλεγχος αν συμπλήρωσε 4 όμοια
        if game_over(grid):
            break
        # παίζει ο υπολογιστής
        print(f"---{pl_2.name}---")
        computer_turn(grid, level)
        print_grid(grid)
    return game_over(grid)


# Επιλογή είδους παιχνιδιού
def mode():
    while True:
        game_mode = input("Choose Game Mode| PVP (1) / PVE (2): ")
        if game_mode not in ['1', '2']:
            print("For PVP 1, for PVE 2!")
            continue
        return game_mode


# Επιλογή επιπέδου δυσκολίας παιχνιδιού
def lvl():
    while True:
        game_lvl = input("Choose Game Level| Easy (1) / Normal (2) / Hard (3): ")
        if game_lvl not in ['1', '2', '3']:
            print("For Easy 1, for Normal 2 and for Hard 3!")
            continue
        return game_lvl


# Κυρίως παιχνίδι
def play():
    while True:
        grid = create_grid()
        if mode() == '1':   # pvp
            # εισαγωγή ονομάτων
            new_name = input("Player 1! Insert name: ")
            player_1 = Player(new_name)
            insert_table(player_1)
            new_name = input("Player 2! Insert name: ")
            player_2 = Player(new_name)
            insert_table(player_2)
            winner = pvp(grid, player_1, player_2)
            update_stats(winner, player_1, player_2)
            print_winner(winner, player_1, player_2)
        else:   # pve
            # εισαγωγή ονόματος
            new_name = input("Insert name: ")
            player_1 = Player(new_name)
            insert_table(player_1)
            player_2 = Player("Computer")
            insert_table(player_2)
            winner = pve(grid, player_1, player_2, lvl())
            update_stats(winner, player_1, player_2)
            print_winner(winner, player_1, player_2)
        # παίζει ξανά
        while True:
            print("-------------------------------------")
            play_again = input("Play again? (Y/N):")
            print("-------------------------------------")
            # ελέγχει το Input
            if play_again not in ['Y', 'y', 'N', 'n']:
                print("Wrong Input!")
                continue
            break
        # τερματίζει το παιχνίδι
        if play_again in ['N', 'n']:
            return


# Εμφάνιση στατιστικών παικτών
def show_stats():
    print("--------------- RANK ----------------")
    print(f"{'Name':<20}{'Games':<7}{'Wins':<7}{'Losses':<7}{'Draws':<7}{'ELO':<7}")
    for user in ranking_table():
        print(f"{user[0]:<20}{user[1]:<7}{user[2]:<7}{user[3]:<7}{user[4]:<7}{user[5]:<7}")
    print("-------------------------------------")


# Main
print("------------- CONNECT 4 -------------")
create_table()
main_menu = "------------- Main Menu -------------\n1. Play\n2. Rank\n3. Settings\n4. Exit\nInsert Choice: "
while True:
    choice = input(main_menu)
    if choice == '1':
        # Παίζει
        play()
    elif choice == '2':
        # Στατιστικά
        show_stats()
    elif choice == '3':
        # Ρυθμίσεις
        pass
    elif choice == '4':
        # Τερματισμός
        print("Bye Bye!")
        break
    else:
        # Λανθασμένη επιλογή
        print("Wrong Input! Choose between 1 to 4!\n")

