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
    
    breedte = 800
    hoogte = 600
    canvas = Canvas(root, breedte=breedte, hoogte=hoogte, achtergrondkleur='white')

    dude_breedte = 32
    dude_hoogte = 48
    x = canvas.breedte / 2 - dude_breedte / 2
    y = canvas.hoogte / 2 - dude_hoogte / 2
    dude = Dude(x, y)

    canvas.voeg_dude_toe(dude)
    root.mainloop()


if __name__ == '__main__':
    main()
    
    
# import tkinter as tk


# def main():
#     root = tk.Tk()
#     w = 800
#     h = 600
#     canvas = tk.Canvas(root, width=w, height=h, bg='white')
#     canvas.pack()
#     image = tk.PhotoImage(file='resources/dude_front.png')
#     x = w/2-image.width()/2
#     y = h/2-image.height()/2
#     canvas.create_image(x, y, anchor="nw", image=image)
#     root.mainloop()


# if __name__ == '__main__':
#     main()