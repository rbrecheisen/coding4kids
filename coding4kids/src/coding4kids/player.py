import tkinter as tk


class Player:
    def __init__(self, player_field, start_x, start_y):
        self.player_field = player_field
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='resources/dude_front.png')
        self.icon = player_field.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.breedte = self.image.width()
        self.hoogte = self.image.height()