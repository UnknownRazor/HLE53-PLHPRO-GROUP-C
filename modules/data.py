import sqlite3

class DataBase:
    def __init__(self):
        self.connection = None
        self.connect_to_db()
        if self.connection is not None:
            self.create_table()


    # Σύνδεση στο Database
    def connect_to_db(self):
        try:
            self.connection = sqlite3.connect('..\\db\\connect4_PythonDB.db')
        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

    # Δημιουργία πίνακα παικτών
    def create_table(self):
        cursor = self.connection.cursor()

        sql_query = """CREATE TABLE IF NOT EXISTS users (
                        name TEXT PRIMARY KEY NOT NULL,
                        games INTEGER DEFAULT 0,
                        wins INTEGER DEFAULT 0,
                        losses INTEGER DEFAULT 0,
                        draws INTEGER DEFAULT 0,
                        elo INTEGER DEFAULT 0)"""
        cursor.execute(sql_query)

        self.connection.commit()

    # Βρίσκει έναν παίκτη στο DataBase
    def get_user(self, player):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name=?", (player,))
        user = cursor.fetchone()
        return user


    # Εισαγωγή παίκτη στον πίνακα αν δεν υπάρχει
    # Η' ενημέρωση στοιχείων παίκτη από τον πίνακα
    def insert_table(self, player):
        cursor = self.connection.cursor()

        sql_query = """SELECT * FROM users WHERE name = ?"""
        cursor.execute(sql_query, (player.name,))
        user = cursor.fetchall()
        if not user:
            sql_query = """INSERT INTO users (games, wins, losses, draws, elo, name) VALUES (?,?,?,?,?,?);"""
            attributes = player.get_att()
            cur = self.connection.cursor()
            cur.execute(sql_query, attributes)
        else:
            for att in user:
                player.games = att[1]
                player.wins = att[2]
                player.losses = att[3]
                player.draws = att[4]
                player.elo = att[5]

        self.connection.commit()

    # Ενημέρωση στοιχείων παίκτη στον πίνακα
    def update_table(self, player):
        cursor = self.connection.cursor()
        sql_query = """UPDATE users SET games = ?, wins = ?, losses = ?, draws = ?, elo = ? WHERE name = ?;"""

        attributes = player.get_att()
        cursor.execute(sql_query, attributes)

        self.connection.commit()

    # Δημιουργία ταξινομημένων παικτών βάση ELO (top 10)
    def ranking(self):
        cursor = self.connection.cursor()
        sql_query = """SELECT * FROM users ORDER BY -elo LIMIT 0,10"""

        top_players = cursor.execute(sql_query)
        self.connection.commit()
        return top_players

    # Κλείνει το database
    def close_db(self):
        self.connection.close()






