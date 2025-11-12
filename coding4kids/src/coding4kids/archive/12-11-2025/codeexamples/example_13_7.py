import tkinter as tk

class Speler:
    def __init__(self, canvas, x, y):
       self.canvas = canvas
       self.x = x
       self.y = y
       self.image = tk.PhotoImage(file="dude_front.png")
       self.icon = self.canvas.create_image(
            self.x, self.y, image=self.image, anchor="nw")

    def move(self, dx, dy):
        self.canvas.move(self.icon, dx, dy)

app = tk.Tk()
app.title("Speler class")
sky = tk.PhotoImage(file="sky.png")
canvas = tk.Canvas(app, width=sky.width(), height=sky.height())
canvas.create_image(0, 0, image=sky, anchor="nw")
speler = Speler(canvas, 50, 50)
canvas.pack()

def move_speler(event):
    if event.keysym == "Right":
        speler.move(10, 0)
    elif event.keysym == "Left":
        speler.move(-10, 0)
    elif event.keysym == "Up":
        speler.move(0, -10)
    elif event.keysym == "Down":
        speler.move(0, 10)
    else:
        print("Onbekende toets!")

canvas.focus_set()
canvas.bind("<KeyPress>", move_speler)
app.mainloop()