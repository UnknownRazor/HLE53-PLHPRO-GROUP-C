from random import randrange
from winner import game_over
from player import Player


# Δημιουργία και αρχικοποίηση ταμπλό
def create_grid():
    # 6 γραμμές x 7 στήλες, αρχικοποίηση σε 0
    empty_grid = [[0 for column in range(7)] for row in range(6)]
    return empty_grid


# Εμφάνιση ταμπλό παιχνιδιού
def print_grid(grid):
    # εμφάνιση γραμμών, η μία κάτω από την άλλη
    for row in grid:
        print(row)


def find_position(array, user_choice):
    counter = 0
    for arrays in array:
        if arrays[user_choice] == 1 or arrays[user_choice] == 2:
            break
        else:
            counter += 1
    return counter-1


# Επιλογή στήλης που θα αφήσει το πιόνι ο παίκτης
def choose_column():
    # η στήλη πρέπει να είναι ακέραιος αριθμός (0-6)
    while True:
        try:
            column = int(input("Choose a Column: "))-1
            # αν πληκτρολόγησε αριθμό που δεν αντιστοιχεί σε στήλη
            if column not in range(7):
                print("This Column doesn't exist!")
                continue
        except ValueError:
            # δεν πληκτρολόγησε ακέραιο
            print("Wrong input!")
            continue
        return column


# Επιλογή θέσης από τον παίκτη και τοποθέτηση του πιονιού
def player_turn(grid, player):
    # ο παίκτης επιλέγει στήλη
    player_column = choose_column()
    # εύρεση κενής θέσης (γραμμής)
    player_row = find_position(grid, player_column)
    # αν η στήλη είναι γεμάτη, διαλέγει άλλη στήλη
    while player_row == -1:
        print("This Column is Full!")
        player_column = choose_column()
        player_row = find_position(grid, player_column)
    # ο παίκτης καταλαμβάνει την κενή θέση
    grid[player_row][player_column] = player
    return


# Επιλογή τυχαίας θέσης από τον υπολογιστή και τοποθέτηση του πιονιού
def easy(grid, player):
    while True:
        # ο υπολογιστής διαλέγει μια τυχαία στήλη
        computer_column = randrange(0, 7)
        # εύρεση κενής θέσης (γραμμής)
        computer_row = find_position(grid, computer_column)
        # αν υπάρχει κενή θέση
        if computer_row != -1:
            break
    # ο υπολογιστής καταλαμβάνει την κενή θέση
    grid[computer_row][computer_column] = player
    return


# Παίκτης εναντίον παίκτη
def pvp(grid, pl_1, pl_2):
    print_grid(grid)
    # όσο υπάρχουν κενές θέσεις στο ταμπλό
    while not game_over(grid, pl_1, pl_2):
        # παίζει ο παίκτης 1
        print(f"---{pl_1.name}---")
        player_turn(grid, pl_1.code)
        print_grid(grid)
        # έλεγχος αν συμπλήρωσε 4 όμοια
        if game_over(grid, pl_1, pl_2):
            return
        # παίζει ο παίκτης 2
        print(f"---{pl_2.name}---")
        player_turn(grid, pl_2.code)
        print_grid(grid)


# Παίκτης εναντίον υπολογιστή
def pve(grid, pl_1, pl_2):
    print_grid(grid)
    # όσο υπάρχουν κενές θέσεις στο ταμπλό
    while not game_over(grid, pl_1, pl_2):
        # παίζει ο παίκτης 1
        print(f"---{pl_1.name}---")
        player_turn(grid, pl_1.code)
        print_grid(grid)
        # έλεγχος αν συμπλήρωσε 4 όμοια
        if game_over(grid, pl_1, pl_2):
            return
        # παίζει ο υπολογιστής
        print(f"---{pl_2.name}---")
        easy(grid, pl_2.code)
        print_grid(grid)


# Επιλογή είδους παιχνιδιού
def mode():
    while True:
        try:
            game_mode = int(input("Choose Game Mode| PVP (1) / PVE (2): "))
            if game_mode != 1 and game_mode != 2:
                print("For PVP 1, for PVE 2!")
                continue
        except ValueError:
            # δεν πληκτρολόγησε ακέραιο
            print("Wrong input!")
            continue
        return game_mode


# Κυρίως παιχνίδι
def play():
    while True:
        grid = create_grid()
        if mode() == 1:
            # εισαγωγή ονομάτων
            new_name = input("Player 1! Insert name: ")
            player_1 = Player(new_name, 1)
            new_name = input("Player 2! Insert name: ")
            player_2 = Player(new_name, 2)
            pvp(grid, player_1, player_2)
        else:
            # εισαγωγή ονομάτων
            new_name = input("Insert name: ")
            player_1 = Player(new_name, 1)
            player_2 = Player("Computer", 2)
            pve(grid, player_1, player_2)
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
    print(f"{'Name':<20}{'Score':<7}{'Win':<7}{'Loss':<7}{'Draw':<7}")
    for player in Player.player_list:
        print(Player.get_att(player))
    print("-------------------------------------")


# Main
print("------------- CONNECT 4 -------------")
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
