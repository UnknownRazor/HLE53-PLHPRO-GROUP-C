import screens.end_screen as end
import modules.connect4 as c4
import tkinter as tk
from tkinter import PhotoImage
from modules.game import Game

class PVEMode:
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

    def play(self, user_choice, root):
        if self.can_play:
            self.can_play = False
            is_valid = c4.choice(self.grid, self.turn, user_choice, self.button_array, self.img_array)
            if is_valid == 0:
                self.turn = 2
            else:
                self.can_play = True
            won = self.game.game_over()
            if won:
                if won == 1:
                    print(won)
                    end.end_screen(self.canvas, root)
                    pass
                elif won == 0:
                    print(won)
                    end.end_screen(self.canvas, root)
                    pass
            # bot choice
            bot_col = self.game.computer_turn("1")
            is_valid = c4.choice(self.grid, self.turn, bot_col, self.button_array, self.img_array)
            self.turn = 1
            won = self.game.game_over()
            if won:
                if won == 2:
                    print(won)
                    end.end_screen(self.canvas, root)
                    pass
                elif won == 0:
                    end.end_screen(self.canvas, root)
                    pass
            self.can_play = True

class PVPMode:
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

    def play(self, user_choice, root):
        if self.can_play:
            self.can_play = False
            is_valid = c4.choice(self.grid, self.turn, user_choice, self.button_array, self.img_array)
            if is_valid == 0:
                if self.turn == 1:
                    self.turn = 2
                    self.can_play = True
                else:
                    self.turn = 1
                    self.can_play = True
            else:
                self.can_play = True
            won = self.game.game_over()
            if won:
                if won == 1:
                    print(won)
                    end.end_screen(self.canvas, root)
                    pass
                elif won == 2:
                    print(won)
                    end.end_screen(self.canvas, root)
                    pass
                elif won == 3:
                    print(won)
                    end.end_screen(self.canvas, root)
                    pass

