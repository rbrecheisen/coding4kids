import tkinter as tk

app = tk.Tk()
app.title("Het speelveld")
canvas = tk.Canvas(app, width=400, height=300)
canvas.pack()
canvas.create_rectangle(50, 50, 100, 100, fill="red")
app.mainloop()