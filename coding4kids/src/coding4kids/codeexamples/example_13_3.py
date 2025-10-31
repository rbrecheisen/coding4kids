import tkinter as tk

def key_pressed(event):
	print("Toets ingedrukt!")

app = tk.Tk()
canvas = tk.Canvas(app, width=400, height=200) 
canvas.bind("<KeyPress>", key_pressed)
canvas.pack()
app.mainloop()