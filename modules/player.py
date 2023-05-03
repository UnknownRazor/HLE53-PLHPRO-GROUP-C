class Player:
    player_list = []    # λίστα με όλους τους παίκτες

    def __init__(self, name):
        self.name = name    # όνομα
        self.games = 0      # αριθμός παιχνιδιών
        self.wins = 0       # νίκες
        self.loss = 0       # ήττες
        self.draws = 0      # ισοπαλίες
        self.score = 0      # δείκτης αξιολόγησης επίδοσης(νίκη+1/ήττα-1/ισοπαλία 0)
        Player.player_list.append(self)    # προσθήκη παίκτη στη λίστα

    # Ο παίκτης κερδίζει
    def win(self):
        # οι νίκες αυξάνονται κατά 1
        self.wins += 1
        # αύξηση αριθμού παιχνιδιών
        self.games += 1
        # ο δείκτης αξιολόγησης αυξάνεται κατά 1
        self.score += 1

    # Ο παίκτης χάνει
    def lose(self):
        # οι ήττες αυξάνονται κατά 1
        self.loss += 1
        # αύξηση αριθμού παιχνιδιών
        self.games += 1
        # ο δείκτης αξιολόγησης μειώνεται κατά 1
        self.score -= 1

    # Ισοπαλία
    def draw(self):
        # οι ισοπαλίες αυξάνονται κατά 1
        self.draws += 1
        # αύξηση αριθμού παιχνιδιών
        self.games += 1
        # ο δείκτης αξιολόγησης δεν αλλάζει (0)

    # παρουσίαση παίκτη
    def __str__(self):
        return f"{self.name:<20}{self.score:<7}{self.games:<7}{self.wins:<7}{self.loss:<7}{self.draws:<7}"

    # Επιστρέφει tuple με τα στοιχεία του παίκτη
    def get_att(self):
        return self.name, self.games, self.wins, self.loss, self.draws, self.score

