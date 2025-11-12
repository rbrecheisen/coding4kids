import tkinter as tk

app = tk.Tk()
app.title("Speelveld met achtergrond")
foto = tk.PhotoImage(file="sky.png")
canvas = tk.Canvas(app, width=foto.width(), height=foto.height())
canvas.pack()
canvas.create_image(0,0,image=foto,anchor="nw")
app.mainloop()