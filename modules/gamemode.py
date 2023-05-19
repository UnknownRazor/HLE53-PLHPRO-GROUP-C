import screens.end_screen as end
import modules.connect4 as c4
import tkinter as tk
from tkinter import PhotoImage
from modules.game import Game

class PVEMode:
    def __init__(self, button_array, canvas, difficulty=False):
        self.difficulty = difficulty
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
            row = self.game.player_turn(self.turn, user_choice)
            if row != -1:
                self.animate(row, user_choice)
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
            if self.can_play == False:
                if self.difficulty == True:
                    bot_row, bot_col = self.game.computer_turn("3")
                    self.animate(bot_row, bot_col)
                else:
                    bot_row, bot_col = self.game.computer_turn("1")
                    self.animate(bot_row, bot_col)
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
                for row in self.game.grid:
                    print(row)
                print("-----------------------")
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
            row = c4.choice(self.grid, self.turn, user_choice, self.button_array, self.img_array)
            if row == 0:
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

