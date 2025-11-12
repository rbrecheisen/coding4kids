import tkinter as tk

class Speler:
    def __init__(self,canvas,x,y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = tk.PhotoImage(file="dude_front.png")
        self.rect = self.canvas.create_image(
            self.x, self.y, image=self.image, anchor="nw")
        self.breedte = self.image.width()
        self.hoogte = self.image.height()

    def move(self,dx,dy):
        self.canvas.move(self.rect,dx,dy)
        self.x += dx
        self.y += dy

class Muur:
    def __init__(self,canvas,x,y,breedte,hoogte,kleur):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.breedte = breedte
        self.hoogte = hoogte
        self.rect = self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x+self.breedte,
            self.y+self.hoogte,
            fill=kleur
        )

    def geraakt_door_hoekpunt(self, x,y):
        a = x > self.x
        b = x < self.x + self.breedte
        c = y > self.y
        d = y < self.y + self.hoogte
        if a and b and c and d:
            return True
        else:
            return False

    def geraakt(self, object):
        a = self.geraakt_door_hoekpunt(object.x, object.y)
        b = self.geraakt_door_hoekpunt(
            object.x+object.breedte, 
            object.y
        )
        c = self.geraakt_door_hoekpunt(
            object.x+object.breedte, 
            object.y+object.hoogte
        )
        d = self.geraakt_door_hoekpunt(
            object.x, 
            object.y+object.hoogte
        )
        if a or b or c or d:
            return True
        else:
            return False

app = tk.Tk()
app.title("Collision detection")
sky = tk.PhotoImage(file="sky.png")
canvas = tk.Canvas(app, width=sky.width(), height=sky.height())
canvas.create_image(0, 0, image=sky, anchor="nw")
canvas.pack()

speler = Speler(canvas, 20, 50)
muur = Muur(canvas, 100, 50, 120, 200, "red")

def move_speler(event):
    speler.move(dx=1, dy=0)
    if muur.geraakt(speler):
        print("Muur geraakt door speler!!!")

canvas.focus_set()
canvas.bind("<KeyPress>", move_speler)

app.mainloop()
