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
        self.width = self.image.width()
        self.height = self.image.height()

    #=================================================================================
    def move(self, dx, dy):
        self.canvas.move(self.icon, dx, dy)
        self.x += dx
        self.y += dy

    #=================================================================================
    def hit_by(self, object):
        return not (
            object.x + object.width < self.x or
            object.x > self.x + self.width or
            object.y + object.height < self.y or
            object.y > self.y + self.height
        )
        

class Bomb:

    #=================================================================================
    def __init__(self, canvas, start_x, start_y, direction):
        self.canvas = canvas
        self.x = start_x
        self.y = start_y
        self.speed = random.choice([7, 7.25, 7.5, 7.75, 8])
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/bomb.png')
        self.icon = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.width = self.image.width()
        self.height = self.image.height()
        self.dx = self.speed * direction
        self.dy = self.speed

    #=================================================================================
    def move(self, direction_x, direction_y):
        self.dx *= direction_x
        self.dy *= direction_y
        self.canvas.move(self.icon, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy

    #=================================================================================
    def hit_by(self, object):
        return not (
            object.x + object.width < self.x or
            object.x > self.x + self.width or
            object.y + object.height < self.y or
            object.y > self.y + self.height
        )

class Star:

    #=================================================================================
    def __init__(self, canvas, start_x, start_y):
        self.canvas = canvas
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/star.png')
        self.icon = self.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)
        self.width = self.image.width()
        self.height = self.image.height()


class Wall:

    #=================================================================================
    def __init__(self, canvas, x0, y0, x1, y1):
        self.canvas = canvas
        self.x = x0
        self.y = y0
        self.width = x1 - x0
        self.height = y1 - y0
        self.rectangle = self.canvas.create_rectangle(x0, y0, x1, y1, fill='green', outline='')