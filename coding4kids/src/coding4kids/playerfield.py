import tkinter as tk
from coding4kids.player import Player
from coding4kids.bomb import Bomb


class PlayerField:
    def __init__(self, game):
        # Bewaar een connectie met de game
        self.game = game
        
        # Maak achtergrond
        self.achtergrond = tk.PhotoImage(file='resources/sky.png')
        self.breedte = self.achtergrond.width()
        self.hoogte = self.achtergrond.height()
        self.canvas = tk.Canvas(self.game, width=self.breedte, height=self.hoogte)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.achtergrond, anchor='nw')
        
        # Maak lege variabelen voor speler, etc.
        self.player = None
        self.player_snelheid = 10
        self.bomb = None
        self.bomb_snelheid = 5

        # Zorg ervoor dat het spelerveld pijltjes toetsen detecteert
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress>', self.move_player)

    def create_player(self):        
        # Maak een nieuwe speler aan en verplaats hem naar het midden van het scherm
        self.player = Player(self, 0, 0)
        x = self.breedte / 2 - self.player.breedte / 2 - 100
        y = self.hoogte / 2 - self.player.hoogte / 2
        self.canvas.move(self.player.icon, x, y)
        return self.player
    
    def create_bomb(self):
        self.bomb = Bomb(self, 0, 0)
        return self.bomb

    def move_player(self, event):
        key = event.keysym
        if key == 'Left':
            # Beweeg speler naar links
            self.canvas.move(self.player.icon, -self.player_snelheid, 0)
        elif key == 'Right':
            # Beweeg speler naar rechts
            self.canvas.move(self.player.icon, self.player_snelheid, 0)
        elif key == 'Down':
            # Beweeg speler naar beneden
            self.canvas.move(self.player.icon, 0, self.player_snelheid)
        elif key == 'Up':
            # Beweeg speler naar boven
            self.canvas.move(self.player.icon, 0, -self.player_snelheid)

    def game_loop(self):
        # Deze code wordt ongeveer 60x per second uitgevoerd
        self.canvas.move(self.bomb.icon, self.bomb_snelheid, self.bomb_snelheid)
        self.game.after(16, self.game_loop)