import tkinter as tk


root = tk.Tk()
root.title('Working with events')
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()
square = canvas.create_rectangle(180, 130, 220, 170, fill='red')


def move_square(e):
    key = e.keysym
    if key == 'Left':
        canvas.move(square, -10, 0)
    elif key == 'Right':
        canvas.move(square, 10, 0)
    elif key == 'Up':
        canvas.move(square, 0, -10)
    elif key == 'Down':
        canvas.move(square, 0, 10)

canvas.focus_set()
canvas.bind('<KeyPress>', move_square)

root.mainloop()