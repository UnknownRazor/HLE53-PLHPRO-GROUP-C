import sqlite3
from player import Player


# Δημιουργία πίνακα παικτών
def create_table():
    try:
        connection = sqlite3.connect('connect4.db')
        cursor = connection.cursor()

        sql_query = '''CREATE TABLE IF NOT EXISTS users (
                        name TEXT PRIMARY KEY NOT NULL,
                        games INTEGER DEFAULT 0,
                        wins INTEGER DEFAULT 0,
                        losses INTEGER DEFAULT 0,
                        draws INTEGER DEFAULT 0,
                        elo INTEGER DEFAULT 0)'''

        cursor.execute(sql_query)
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


# Εισαγωγή παίκτη στον πίνακα αν δεν υπάρχει
# Η' ενημέρωση στοιχείων παίκτη από τον πίνακα
def insert_table(pl):
    try:
        connection = sqlite3.connect('connect4.db')
        cursor = connection.cursor()

        sql_query = """SELECT * FROM users WHERE name = ?"""
        cursor.execute(sql_query, (pl.name,))
        user = cursor.fetchall()

        if not user:
            sql_query = """INSERT INTO users (games, wins, losses, draws, elo, name) VALUES (?,?,?,?,?,?);"""
            attributes = pl.get_att()
            cur = connection.cursor()
            cur.execute(sql_query, attributes)
        else:
            for att in user:
                pl.games = att[1]
                pl.wins = att[2]
                pl.losses = att[3]
                pl.draws = att[4]
                pl.elo = att[5]
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


# Ενημέρωση στοιχείων παίκτη στον πίνακα
def update_table(pl):
    try:
        connection = sqlite3.connect('connect4.db')
        cursor = connection.cursor()
        sql_query = """UPDATE users SET games = ?, wins = ?, losses = ?, draws = ?, elo = ? WHERE name = ?;"""

        attributes = pl.get_att()
        cursor.execute(sql_query, attributes)

        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


# Δημιουργία λίστας ταξινομημένων παικτών βάση ELO
def ranking_table():
    users = []
    try:
        connection = sqlite3.connect('connect4.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        users.sort(key=lambda user: user[5], reverse=True)

        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

    return users





