import tkinter as tk


class Player:

    #=================================================================================
    def __init__(self, canvas, start_x, start_y):
        self.canvas = canvas
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/dude_front.png')
        self.icon = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.breedte = self.image.width()
        self.hoogte = self.image.height()

    #=================================================================================
    def move(self, dx, dy):
        self.canvas.move(self.icon, dx, dy)
        self.x += dx
        self.y += dy

    #=================================================================================
    def hit_by(self, object):
        return not (
            object.x + object.breedte < self.x or
            object.x > self.x + self.breedte or
            object.y + object.hoogte < self.y or
            object.y > self.y + self.hoogte
        )
        

class Bomb:

    #=================================================================================
    def __init__(self, canvas, start_x, start_y):
        self.canvas = canvas
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/bomb.png')
        self.icon = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.breedte = self.image.width()
        self.hoogte = self.image.height()

    #=================================================================================
    def move(self, dx, dy):
        self.canvas.move(self.icon, dx, dy)
        self.x += dx
        self.y += dy


class Star:

    #=================================================================================
    def __init__(self, canvas, start_x, start_y):
        self.canvas = canvas
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/star.png')
        self.icon = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.breedte = self.image.width()
        self.hoogte = self.image.height()