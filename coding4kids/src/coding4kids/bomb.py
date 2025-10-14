import tkinter as tk


class Bomb:
    def __init__(self, player_field, start_x, start_y):
        # Bewaar connectie naar spelerveld
        self.player_field = player_field

        # Bewaar startpositie van de bom
        self.x = start_x
        self.y = start_y

        # Maak een icoontje voor het afbeelden van de bom
        self.image = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/bomb.png')
        self.icon = self.player_field.canvas.create_image(self.x, self.y, anchor="nw", image=self.image)

        # Bewaar de breedte en hoogte van het bom icoontje
        self.breedte = self.image.width()
        self.hoogte = self.image.height()

    def move(self, x, y):
        # Beweeg de bom naar de nieuwe positie (x, y)
        self.player_field.canvas.move(self.icon, x, y)

        # Bewaar de nieuwe positie van de bom
        self.x = x
        self.y = y