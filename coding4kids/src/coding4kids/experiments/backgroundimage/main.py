import tkinter as tk

app = tk.Tk()
app.title("Het speelveld")
sky = tk.PhotoImage(file="sky.png")
dude = tk.PhotoImage(file="dude_front.png")
print(f'dude: w={dude.width()}, h={dude.height()}')
canvas = tk.Canvas(app, width=sky.width(), height=sky.height())
canvas.create_image(0, 0, image=sky, anchor="nw")
canvas.create_image(50, 50, image=dude)
canvas.pack()
app.mainloop()