import tkinter as tk

app = tk.Tk()
app.title("Het speelveld")
canvas = tk.Canvas(app, width=400, height=300)
canvas.pack()
app.mainloop()