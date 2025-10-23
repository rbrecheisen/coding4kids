import tkinter as tk


root = tk.Tk()
root.title('Working with events')
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

def key_pressed(event):
    print(event.keysym)

canvas.focus_set()
canvas.bind('<KeyPress>', key_pressed)
root.mainloop()