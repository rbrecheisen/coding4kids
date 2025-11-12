import tkinter as tk

app = tk.Tk()
app.title("Bewegende speler")
sky = tk.PhotoImage(file="sky.png")
dude = tk.PhotoImage(file="dude_front.png")
canvas = tk.Canvas(app, width=sky.width(), height=sky.height())
canvas.pack()
canvas.create_image(0, 0, image=sky, anchor="nw")
speler = canvas.create_image(50, 50, image=dude)
		
def beweeg_speler(event):
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
canvas.bind("<KeyPress>", beweeg_speler)
app.mainloop()