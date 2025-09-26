import tkinter as tk


def main():
    root = tk.Tk()
    w = 800
    h = 600
    canvas = tk.Canvas(root, width=w, height=h, bg='white')
    canvas.pack()
    image = tk.PhotoImage(file='resources/dude_front.png')
    x = w/2-image.width()/2
    y = h/2-image.height()/2
    canvas.create_image(x, y, anchor="nw", image=image)
    root.mainloop()


if __name__ == '__main__':
    main()