import tkinter as tk
import random

from gameobjects import Player, Bomb, Star, Brick
from layouts import LEVELS

SNELHEID_PLAYER = 10
SNELHEID_BOMB = 5


class Game:

    #=================================================================================
    def __init__(self, title):
        # Maak root object wat game gaat uitvoeren straks
        self.root = tk.Tk()
        self.root.title = title

        # Maak achtergrond
        self.achtergrond = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/sky.png')
        self.breedte = self.achtergrond.width()
        self.hoogte = self.achtergrond.height()
        self.canvas = tk.Canvas(self.root, width=self.breedte, height=self.hoogte)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.achtergrond, anchor='nw')

        # Maak een nieuwe speler aan en verplaats hem naar het midden van het scherm.
        # Het midden bereken je door de helft van het speelveld te nemen en daar de 
        # helft van de speler vanaf te trekken. Dat wordt je x positie. Hetzelfde doe
        # je voor de y positie.
        self.player = Player(self.canvas, 0, 0)
        x = self.breedte / 2 - self.player.breedte / 2 - 100
        y = self.hoogte / 2 - self.player.hoogte / 2
        self.player.move(x, y)

        # Maak een lijstje met bommen aan. We beginnen in het 1e level met 1 bom op 
        # positie (0, 0). Dat is helemaal links bovenin
        self.aantal_bombs = 1
        self.bombs = self.create_bombs(self.aantal_bombs)

        # Maak een lijstje met sterren die je moet verzamelen. We geven iedere ster
        # een willekeurige positie op het scherm. Dat doe je met de functie 
        # random.randint(begin, einde)
        self.aantal_stars = 10
        self.stars = self.create_stars(self.aantal_stars)

        # Begin bij het 1e level and laat dit zien op het scherm
        self.level = 1
        self.level_text_id = -1
        self.update_level(self.level)

        # Maak blokken aan waar de speler en bommen tegenaan kunt lopen. Ieder level heeft 
        # andere blokken waardoor het steeds anders is hoe je moet rondlopen!
        self.bricks = self.create_layout(self.level)

        # Laat de score zien op het scherm. Op het begin is de score nul. Voor 
        # iedere ster die je verzameld score je 10 punten
        self.score = 0
        self.score_text_id = -1
        self.update_score(self.score)

        # Houd bij welke toetsen je heb ingedrukt (meestal maar 1tje tegelijkertijd)
        self.keys_pressed = set()

        # Zorg ervoor dat het canvas pijltjes toetsen detecteert
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress>', self.key_pressed)
        self.canvas.bind('<KeyRelease>', self.key_released)

    #=================================================================================
    def create_bombs(self, aantal):
        bombs = []
        for i in range(aantal):
            x = random.randint(40, self.breedte-40)
            y = 0
            bombs.append(Bomb(self.canvas, x, y))
        return bombs
    
    #=================================================================================
    def create_stars(self, aantal):
        stars = []
        for i in range(aantal):
            x = random.randint(40, self.breedte-40)
            y = random.randint(60, self.hoogte-40)
            stars.append(Star(self.canvas, x, y))
        return stars

    #=================================================================================
    def create_layout(self, level):
        bricks = []
        layout = LEVELS[level]
        for i in range(len(layout)):
            rij = layout[i]
            for j, char in enumerate(rij):
                if char == '1':
                    brick = Brick(self.canvas, i, j)
                    bricks.append(brick)
        return bricks

    #=================================================================================
    def move_player(self):
        if 'Left' in self.keys_pressed:
            self.player.move(-SNELHEID_PLAYER, 0)
        elif 'Right' in self.keys_pressed:
            self.player.move(SNELHEID_PLAYER, 0)
        elif 'Down' in self.keys_pressed:
            self.player.move(0, SNELHEID_PLAYER)
        elif 'Up' in self.keys_pressed:
            self.player.move(0, -SNELHEID_PLAYER)

    #=================================================================================
    def key_pressed(self, event):
        # Voeg de ingedrukte toets toe aan de lijst van ingedrukte toetsen
        self.keys_pressed.add(event.keysym)

    #=================================================================================
    def key_released(self, event):
        # Verwijder de pijltjes toets uit de lijst van ingedrukte toetsen
        self.keys_pressed.discard(event.keysym)

    #=================================================================================
    def display_game_over(self):
        # Bepaal x positie van het midden van het scherm, en de y positie een stukje
        # onder de bovenkant van het scherm. Teken dan de tekst "GAME OVER" op het
        # scherm op de positie (x, y) in rode kleur en grote letters
        x = self.breedte / 2 - self.player.breedte / 2
        y = 200
        self.canvas.create_text(
            x, y, text='GAME OVER', fill='red', font=('Helvetica', 32, 'bold'))
        
    #=================================================================================
    def update_level(self, level):
        # Maak de nieuwe level tekst en bepaal de (x, y) positie van de tekst
        level_text = 'Level ' + str(level)
        x = self.breedte - 60
        y = 20

        # Als dit de eerste keer is dat je het level laat zien, dan maak de nieuwe
        # tekst aan en onthoud het ID van de tekst (self.level_text_id). Dit ID is
        # altijd groter dan 0
        if self.level_text_id < 0:
            self.level_text_id = self.canvas.create_text(
                x, y, text=level_text, fill='white', font=('Helvetica', 16, 'bold'))
        else:
            # Als het text ID groter is dan 0, maak dan geen nieuwe tekst aan maar
            # wijzig de bestaande tekst
            self.canvas.itemconfig(self.level_text_id, text=level_text)
        
    #=================================================================================
    def update_score(self, score):
        # Maak de nieuwe score tekst en bepaal de (x, y) positie van de tekst
        score_text = 'Score: ' + str(score)
        x = self.breedte / 2 - self.player.breedte / 2
        y = 20

        # Als dit de eerste keer is dat je de score laat zien, dan maak de nieuwe
        # tekst aan en onthoud het ID van de tekst (self.score_text_id). Dit ID is
        # altijd groter dan 0
        if self.score_text_id < 0:
            self.score_text_id = self.canvas.create_text(
                x, y, text=score_text, fill='yellow', font=('Helvetica', 16, 'bold'))
        else:
            # Als het text ID groter is dan 0, maak dan geen nieuwe tekst aan maar
            # wijzig de bestaande tekst
            self.canvas.itemconfig(self.score_text_id, text=score_text)

    #=================================================================================
    def all_stars_collected(self):
        # Als het lijstje met sterren leeg is, d.w.z., de lengte van het lijstje
        # is nul dan heb je ze allemaal verzameld
        return len(self.stars) == 0

    #=================================================================================
    def game_loop(self):
        # Beweeg de speler indien nodig (als je een pijltjes toets hebt ingedrukt)
        self.move_player()

        # Beweeg alle bommen in de lijst schuin door het spelerveld
        for bomb in self.bombs:
            bomb.move(SNELHEID_BOMB, SNELHEID_BOMB)

        # Check of de speler is geraakt 1 van de bommen. Zo ja, 
        # dan is het game over
        for bomb in self.bombs:
            if self.player.hit_by(bomb):
                self.display_game_over()
                return
            
        # Check of de speler een ster heeft geraakt. Zo ja, dan scoort hij 10
        # punten en voegen we de ster toe aan de lijst
        for star in self.stars:
            if self.player.hit_by(star):
                self.score += 10
                self.update_score(self.score)
                self.stars.remove(star)
                break
        
        # Check of alle sterren zijn verzameld. Zo ja, dan beginnen we met het volgende
        # level maar dan met een extra bom om het moeilijker te maken!
        if self.all_stars_collected():
            self.level += 1
            self.update_level(self.level)
            self.stars = self.create_stars(10)
        
        # Wacht heel even (16ms) en roep de functie game_loop nog eens aan. Hierdoor ontstaat
        # er een loop waarin de functie game_loop ongeveer 60x per seconde wordt 
        # aangeroepen
        self.root.after(16, self.game_loop)

    #=================================================================================
    def start(self):
        self.game_loop()
        self.root.mainloop()