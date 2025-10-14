import tkinter as tk


class Player:
    def __init__(self, player_field, start_x, start_y):
        self.player_field = player_field
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/dude_front.png')
        self.icon = self.player_field.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.breedte = self.image.width()
        self.hoogte = self.image.height()

    def move(self, dx, dy):
        self.player_field.canvas.move(self.icon, dx, dy)
        self.x += dx
        self.y += dy

    def geraakt_door(self, object):
        if object.x > self.x and object.x < self.x + self.breedte and object.y > self.y and object.y < self.y + self.hoogte:
            return True
        else:
            return False