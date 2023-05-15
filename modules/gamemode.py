import sqlite3
from sqlite3 import *
import screens.end_screen as end
import modules.connect4 as c4
import modules.winner as winner

class pve_mode():
    def __init__(self, array, button_array, canvas):
        self.turn = 1
        self.array = array
        self.button_array = button_array
        self.canvas = canvas

    def play(self, user_choice, username, root):
        isValid = c4.choice(self.array, self.turn, user_choice, self.button_array)
        if isValid == 0:
            self.turn = 2
        won = winner.game_over(self.array)
        if won != False:
            if won == 1:
                print(won)
                end_scr = end.end_screen(self.canvas, root)
                pass
            elif won == 0:
                print(won)
                end_scr = end.end_screen(self.canvas, root)
                pass
        # bot choice
        if isValid == 0:
            self.turn = 1
        won = winner.game_over(self.array)
        if won != False:
            if won == 2:
                print(won)
                end_scr = end.end_screen(self.canvas, root)
                pass
            elif won == 0:
                end_scr = end.end_screen(self.canvas, root)
                pass



#def db_connection(username,elo):
#    try:
        # make sqlite connection
 #       sqliteConnection = sqlite3.connect('..\\db\\connect4_PythonDB.db')
       # cursor = sqliteConnection.cursor()
  #      print("Successfully Connected to SQLite")
   # cursor.execute("SELECT * FROM users WHERE username=?", (username,))
  #  user = cursor.fetchone()
 #   if elo == -1:
 #       user_elo = user[4]
  #      user_losses = user[3]
  #  if user:
        # print("User has beeen found")
   #     cursor.execute("")
        #cursor.execute("UPDATE users SET losses=?,elo=? WHERE username=? VALUES (?, ?, ?, ?)",,
                       #(username, 0, 0, 0))
   #     sqliteConnection.commit()

  #  cursor.close()

  #  except sqlite3.Error as error:
        #tk.messagebox.showerror('Python Error', f'Error while connecting to sqlite {error}')
  #  finally:
        #if sqliteConnection:
            # even if errors occured close the connection
            #sqliteConnection.close()