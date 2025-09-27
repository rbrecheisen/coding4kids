import tkinter as tk


class Dude:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.image = tk.PhotoImage(file='resources/dude_front.png')


class Canvas:
    def __init__(self, root, breedte, hoogte, achtergrondkleur):
        self.root = root
        self.breedte = breedte
        self.hoogte = hoogte
        self.achtergrondkleur = achtergrondkleur
        self.canvas = tk.Canvas(self.root, width=breedte, height=hoogte, bg=self.achtergrondkleur)
        self.canvas.pack()

    def voeg_dude_toe(self, dude):
        self.canvas.create_image(dude.x, dude.y, anchor="nw", image=dude.image)


def main():
    root = tk.Tk()
    canvas = Canvas(root, breedte=800, hoogte=600, achtergrondkleur='white')
    dude = Dude(0, 0)
    canvas.voeg_dude_toe(dude)
    root.mainloop()


if __name__ == '__main__':
    main()