import tkinter as tk

KLEUREN_NEDERLANDS_NAAR_ENGELS = {
    'wit': 'white',
    'rood': 'red',
    'blauw': 'blue',
    'groen': 'green',
    'zwart': 'black',
}


class Canvas:
    def __init__(self, root, breedte, hoogte, achtergrondkleur):
        self.root = root
        self.breedte = breedte
        self.hoogte = hoogte
        self.achtergrondkleur = achtergrondkleur
        self.canvas = tk.Canvas(self.root, width=breedte, height=hoogte, bg=self.achtergrondkleur)
        self.canvas.pack()


def main():
    root = tk.Tk()
    achtergrondkleur = KLEUREN_NEDERLANDS_NAAR_ENGELS['wit']
    canvas = Canvas(root, breedte=800, hoogte=600, achtergrondkleur=achtergrondkleur)
    print(f'Canvas breedte: {canvas.breedte}')
    print(f'Canvas hoogte: {canvas.hoogte}')
    print(f'Canvas achtergrondkleur: {canvas.achtergrondkleur}')
    root.mainloop()


if __name__ == '__main__':
    main()