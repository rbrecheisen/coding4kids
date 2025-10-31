import tkinter as tk

def key_pressed(event):
	print(event.keysym)

app = tk.Tk()
canvas = tk.Canvas(app, width=400, height=200) 
canvas.focus_set()
canvas.bind("<KeyPress>", key_pressed)
canvas.pack()
app.mainloop()