import tkinter as tk

app = tk.Tk()
app.title("Bewegende speler")
sky = tk.PhotoImage(file="sky.png")
dude = tk.PhotoImage(file="dude_front.png")
canvas = tk.Canvas(app, width=sky.width(), height=sky.height())
canvas.pack()
canvas.create_image(0, 0, image=sky, anchor="nw")
speler = canvas.create_image(50, 100, image=dude)
muur_links = canvas.create_rectangle(0,40,20,600,fill="red")
muur_boven = canvas.create_rectangle(20,40,780,60,fill="red")
muur_onder = canvas.create_rectangle(20,580,780,600,fill="red")
muur_rechts = canvas.create_rectangle(780,40,800,600,fill="red")
		
def move_speler(event):
    if event.keysym == "Right":
        canvas.move(speler, 10, 0)
    elif event.keysym == "Left":
        canvas.move(speler, -10, 0)
    elif event.keysym == "Up":
        canvas.move(speler, 0, -10)
    elif event.keysym == "Down":
        canvas.move(speler, 0, 10)
    else:
        print("Onbekende toets!")

canvas.focus_set()
canvas.bind("<KeyPress>", move_speler)
app.mainloop()