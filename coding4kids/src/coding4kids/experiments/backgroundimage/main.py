import tkinter as tk

app = tk.Tk()
app.title("Het speelveld")
foto = tk.PhotoImage(file="sky.png")
canvas = tk.Canvas(app, width=400, height=300)
canvas.create_image(0, 0, image=foto, anchor="nw")
canvas.pack()
app.mainloop()