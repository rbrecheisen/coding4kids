import tkinter as tk

app = tk.Tk()
app.title("Het speelveld")
sky = tk.PhotoImage(file="sky.png")
dude = tk.PhotoImage(file="dude_front.png")
canvas = tk.Canvas(app, width=sky.width(), height=sky.height())
canvas.create_image(0, 0, image=sky, anchor="nw")
speler = canvas.create_image(50, 50, image=dude)
canvas.pack()

def move_dude(event):
    if event.keysym == 'Right':
        canvas.move(speler, 10, 0)

canvas.focus_set()
canvas.bind('<KeyPress>', move_dude)
app.mainloop()