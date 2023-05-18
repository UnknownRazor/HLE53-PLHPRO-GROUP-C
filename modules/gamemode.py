import sqlite3
from sqlite3 import *
import screens.end_screen as end
import modules.connect4 as c4
import modules.winner as winner
from tkinter import PhotoImage
from modules.game import Game

class pve_mode():
    def __init__(self, button_array, canvas):
        self.turn = 1
        self.button_array = button_array
        self.can_play = True
        self.canvas = canvas
        self.white = PhotoImage(file="../assets/white.png")
        self.red = PhotoImage(file="../assets/red.png")
        self.yellow = PhotoImage(file="../assets/yellow.png")
        self.img_array = [self.white, self.red, self.yellow]
        self.game = Game()
        self.grid = self.game.grid
    def play(self, user_choice, username, root):
        if self.can_play == True:
            self.can_play = False
            isValid = c4.choice(self.grid, self.turn, user_choice, self.button_array, self.img_array)
            if isValid == 0:
                self.turn = 2
            else:
                self.can_play = True
            won = self.game.game_over()
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
            bot_col = self.game.computer_turn("1")
            isValid = c4.choice(self.grid, self.turn, bot_col, self.button_array, self.img_array)
            self.turn = 1
            won = self.game.game_over()
            if won != False:
                if won == 2:
                    print(won)
                    end_scr = end.end_screen(self.canvas, root)
                    pass
                elif won == 0:
                    end_scr = end.end_screen(self.canvas, root)
                    pass
            self.can_play = True

class pvp_mode():
    def __init__(self, button_array, canvas):
        self.turn = 1
        self.button_array = button_array
        self.canvas = canvas
        self.can_play = True
        self.white = PhotoImage(file="../assets/white.png")
        self.red = PhotoImage(file="../assets/red.png")
        self.yellow = PhotoImage(file="../assets/yellow.png")
        self.img_array = [self.white, self.red, self.yellow]
        self.game = Game()
        self.grid = self.game.grid
    def play(self, user_choice, username, root):
        if self.can_play == True:
            self.can_play = False
            isValid = c4.choice(self.grid, self.turn, user_choice, self.button_array, self.img_array)
            if isValid == 0:
                if self.turn == 1:
                    self.turn = 2
                    self.can_play = True
                else:
                    self.turn = 1
                    self.can_play = True
            else:
                self.can_play = True
            won = self.game.game_over()
            if won != False:
                if won == 1:
                    print(won)
                    end_scr = end.end_screen(self.canvas, root)
                    pass
                elif won == 2:
                    print(won)
                    end_scr = end.end_screen(self.canvas, root)
                    pass
                elif won == 3:
                    print(won)
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