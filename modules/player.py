class Player:
    def __init__(self, name):
        self.name = name    # όνομα
        self.games = 0      # αριθμός παιχνιδιών
        self.wins = 0       # νίκες
        self.losses = 0     # ήττες
        self.draws = 0      # ισοπαλίες
        self.elo = 0        # δείκτης αξιολόγησης επίδοσης(νίκη+1/ήττα-1/ισοπαλία 0)

    # Ο παίκτης κερδίζει
    def win(self):
        # οι νίκες αυξάνονται κατά 1
        self.wins += 1
        # αύξηση αριθμού παιχνιδιών
        self.games += 1
        # ο δείκτης αξιολόγησης αυξάνεται κατά 1
        self.elo += 1

    # Ο παίκτης χάνει
    def lose(self):
        # οι ήττες αυξάνονται κατά 1
        self.losses += 1
        # αύξηση αριθμού παιχνιδιών
        self.games += 1
        # ο δείκτης αξιολόγησης μειώνεται κατά 1
        self.elo -= 1

    # Ισοπαλία
    def draw(self):
        # οι ισοπαλίες αυξάνονται κατά 1
        self.draws += 1
        # αύξηση αριθμού παιχνιδιών
        self.games += 1
        # ο δείκτης αξιολόγησης δεν αλλάζει (0)

    # παρουσίαση παίκτη
    def __str__(self):
        return f"{self.name:<20}{self.elo:<7}{self.games:<7}{self.wins:<7}{self.losses:<7}{self.draws:<7}"

    # Επιστρέφει tuple με τα στοιχεία του παίκτη
    def get_att(self):
        return self.games, self.wins, self.losses, self.draws, self.elo, self.name




