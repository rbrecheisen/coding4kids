import tkinter as tk


class Game(tk.Tk):
    def start(self, player_field):
        player_field.game_loop()
        self.mainloop()