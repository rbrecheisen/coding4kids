import tkinter as tk


class Dude:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='resources/dude_front.png')


class Canvas:
    def __init__(self, root):
        self.root = root
        self.achtergrondplaatje = tk.PhotoImage(file='resources/sky.png')
        self.breedte = self.achtergrondplaatje.width()
        self.hoogte = self.achtergrondplaatje.height()
        self.canvas = tk.Canvas(self.root, width=self.breedte, height=self.hoogte)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.achtergrondplaatje, anchor='nw')

    def voeg_dude_toe(self, dude):
        self.canvas.create_image(dude.x, dude.y, anchor="nw", image=dude.image)


def main():
    root = tk.Tk()    
    canvas = Canvas(root)
    dude_breedte = 32
    dude_hoogte = 48
    x = canvas.breedte / 2 - dude_breedte / 2
    y = canvas.hoogte / 2 - dude_hoogte / 2
    dude = Dude(x, y)
    canvas.voeg_dude_toe(dude)
    root.mainloop()


if __name__ == '__main__':
    main()