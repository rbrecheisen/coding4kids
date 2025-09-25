import tkinter as tk


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack()
    image = tk.PhotoImage(file="resources/dude_front.png")
    canvas.create_image(50, 50, anchor="nw", image=image)
    root.mainloop()


if __name__ == '__main__':
    main()