import tkinter as tk


def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=400, height=300, bg="white")
    canvas.pack()
    root.mainloop()


if __name__ == '__main__':
    main()