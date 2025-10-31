import tkinter as tk

app = tk.Tk()
app.title("Speelveld")
canvas = tk.Canvas(app, width=400, height=200)
canvas.create_rectangle(50, 50, 100, 100, fill="red")
canvas.pack()
app.mainloop()