import screens.end_screen as end
import modules.connect4 as c4
from tkinter import PhotoImage
from modules.game import Game
from modules.data import DataBase

class PVPMode:
    def __init__(self, button_array, canvas, username, username2):
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
        self.db = DataBase()

    def play(self, user_choice, root):
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
            self.check_won(root)
            self.can_play = True
    def check_won(self, root):
        won = self.game.game_over()
        if won:
            if won == 1:
                self.upd_db()
                End = end.end_screen(self.canvas, root, self.username)
            elif won == 2:
                self.upd_db()
                if self.username2 == None:
                    End = end.end_screen(self.canvas, root, "Computer")
                else:
                    End = end.end_screen(self.canvas, root, self.username2)
            elif won == 3:
                self.upd_db()
                End = end.end_screen(self.canvas, root, won)

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
    def __init__(self, button_array, canvas, username, difficulty=False, username2=None):
        super().__init__(button_array, canvas, username, username2)
        self.difficulty = difficulty
        self.username2 = username2

    def play(self, user_choice, root):
        if self.can_play:
            self.can_play = False
            row = self.game.player_turn(self.turn, user_choice)
            if row != -1:
                self.animate(row, user_choice)
                self.turn = 2
            else:
                self.can_play = True
            self.check_won(root)
            # bot choice
            if self.can_play == False:
                if self.difficulty == True:
                    bot_row, bot_col = self.game.computer_turn("2")
                    self.animate(bot_row, bot_col)
                else:
                    bot_row, bot_col = self.game.computer_turn("1")
                    self.animate(bot_row, bot_col)
                self.turn = 1
                self.check_won(root)
                self.can_play = True