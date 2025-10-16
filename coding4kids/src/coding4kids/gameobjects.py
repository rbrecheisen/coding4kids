import random
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
    def __init__(self, canvas, start_x, start_y, richting):
        self.canvas = canvas
        self.x = start_x
        self.y = start_y
        self.snelheid = random.choice([7, 7.25, 7.5, 7.75, 8])
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/bomb.png')
        self.icon = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.breedte = self.image.width()
        self.hoogte = self.image.height()
        self.dx = self.snelheid * richting
        self.dy = self.snelheid

    #=================================================================================
    def move(self, richting_x, richting_y):
        self.dx *= richting_x
        self.dy *= richting_y
        self.canvas.move(self.icon, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy

    #=================================================================================
    def hit_by(self, object):
        return not (
            object.x + object.breedte < self.x or
            object.x > self.x + self.breedte or
            object.y + object.hoogte < self.y or
            object.y > self.y + self.hoogte
        )

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


class Wall:

    #=================================================================================
    def __init__(self, canvas, x1, y1, x2, y2):
        self.canvas = canvas
        self.x = x1
        self.y = y1
        self.breedte = x2 - x1
        self.hoogte = y2 - y1
        self.rectangle = self.canvas.create_rectangle(x1, y1, x2, y2, fill='green', outline='')