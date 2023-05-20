import sys

sys.path.append('../modules/')
sys.path.append('../screens/')

import end_screen as end
import connect4 as c4
from tkinter import PhotoImage
from game import Game
from data import DataBase
import threading


class PVPMode:
    def __init__(self, button_array, canvas, username, username2, root):
        self.turn = 1
        self.button_array = button_array
        self.canvas = canvas
        self.can_play = True
        self.white = PhotoImage(file="../assets/white.png")
        self.red = PhotoImage(file="../assets/red.png")
        self.yellow = PhotoImage(file="../assets/yellow.png")
        self.img_array = [self.white, self.red, self.yellow]
        self.username = username
        self.username2 = username2
        self.game = Game(self.username, self.username2)
        self.grid = self.game.grid
        self.root = root
        self.db = DataBase()

    def play(self, user_choice):
        if self.can_play:
            self.can_play = False
            row = self.game.player_turn(self.turn, user_choice)
            if row != -1:
                self.animate(row, user_choice)
                if self.turn == 1:
                    self.turn = 2
                else:
                    self.turn = 1
            else:
                self.can_play = True
            self.check_won()
            self.can_play = True

    def check_won(self):
        won = self.game.game_over()
        if won:
            if won == 1:
                self.upd_db()
                End = end.end_screen(self.canvas, self.root, self.username, self.username)
                self.root.mainloop()
            elif won == 2:
                self.upd_db()
                if self.username2 == None:
                    self.upd_db()
                    End = end.end_screen(self.canvas, self.root, self.username, "Computer")
                    self.root.mainloop()
                else:
                    End = end.end_screen(self.canvas, self.root, self.username, self.username2)
                    self.root.mainloop()
            elif won == 3:
                self.upd_db()
                End = end.end_screen(self.canvas, self.root, self.username, won)
                self.root.mainloop()

    def upd_db(self):
        self.db.insert_table(self.game.player1)
        self.game.update_stats()
        self.db.update_table(self.game.player1)
        if self.username2 != None:
            self.db.insert_table(self.game.player2)
            self.db.update_table(self.game.player2)

    def animate(self, row, col):
        if row != 0:
            for buttons in range(0, row - 1):
                button = self.button_array[buttons][col]
                if self.turn == 1:
                    button.config(image=self.img_array[1])
                else:
                    button.config(image=self.img_array[2])
                c4.tksleep(0.15)
                button.config(image=self.img_array[0])
            for buttons in range(0, row - 1):
                button = self.button_array[buttons][col]
                if self.grid[buttons][col] == self.turn:
                    # button.config(text=str(player))
                    if self.turn == 1:
                        button.config(image=self.img_array[1])
                    else:
                        button.config(image=self.img_array[2])
        button = self.button_array[row][col]
        if self.turn == 1:
            button.config(image=self.img_array[1])
        else:
            button.config(image=self.img_array[2])


class PVEMode(PVPMode):
    def __init__(self, button_array, canvas, username, root, difficulty=False, username2=None):
        super().__init__(button_array, canvas, username, username2, root)
        self.difficulty = difficulty
        self.username2 = username2

    def play(self, user_choice):
        if self.can_play:
            self.can_play = False
            row = self.game.player_turn(self.turn, user_choice)
            if row != -1:
                self.animate(row, user_choice)
                self.turn = 2
            else:
                self.can_play = True
            self.check_won()
            # bot choice
            thread = threading.Thread(target=self.make_bot_turn)
            thread.start()
            self.check_won()

    def make_bot_turn(self):
        if self.can_play == False:
            if self.difficulty == True:
                bot_row, bot_col = self.game.computer_turn("3")
            else:
                bot_row, bot_col = self.game.computer_turn("1")
            self.animate(bot_row, bot_col)
            self.turn = 1
            self.can_play = True
