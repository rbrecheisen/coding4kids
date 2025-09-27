import tkinter as tk


class Canvas:
    def __init__(self, root):
        self.root = root
        self.achtergrondplaatje = tk.PhotoImage(file='resources/sky.png')
        self.breedte = self.achtergrondplaatje.width()
        self.hoogte = self.achtergrondplaatje.height()
        self.canvas = tk.Canvas(self.root, width=self.breedte, height=self.hoogte)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.achtergrondplaatje, anchor='nw')


def main():
    root = tk.Tk()
    canvas = Canvas(root)
    print(f'Canvas: breedte = {canvas.breedte}, hoogte = {canvas.hoogte}')
    root.mainloop()


if __name__ == '__main__':
    main()