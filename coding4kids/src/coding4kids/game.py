import tkinter as tk
import random

from gameobjects import Player, Bomb, Star, Wall

SNELHEID_PLAYER = 10
SNELHEID_BOMB = 5


class Game:

    #=================================================================================
    def __init__(self, title):
        # Maak app object wat de game gaat uitvoeren
        self.app = tk.Tk()
        self.app.title = title        

        # Maak achtergrond        
        self.achtergrond = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/sky.png')
        self.breedte = self.achtergrond.width()
        self.hoogte = self.achtergrond.height()
        self.canvas = tk.Canvas(self.app, width=self.breedte, height=self.hoogte)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.achtergrond, anchor='nw')

        # Maak een nieuwe speler aan en verplaats hem naar het midden van het scherm.
        # Het midden bereken je door de helft van het speelveld te nemen en daar de 
        # helft van de speler vanaf te trekken. Dat wordt je x positie. Hetzelfde doe
        # je voor de y positie.
        self.player = self.create_player()

        # Maak een lijstje met bommen aan. We beginnen in het 1e level met 1 bom
        self.aantal_bombs = 1
        self.bombs = self.create_bombs(self.aantal_bombs)

        # Maak een lijstje met sterren die je moet verzamelen. We geven iedere ster
        # een willekeurige positie op het scherm. Dat doe je met de functie 
        # random.randint(begin, einde)
        self.aantal_stars = 10
        self.stars = self.create_stars(self.aantal_stars)

        # Begin bij het 1e level and laat dit zien op het scherm. Omdat we de level tekst
        # later moeten aanpassen, moeten we ook het ID van de tekst bewaren. Dat is de
        # variabele self.level_text_id. Die zetten we eerst op -1. Later krijgt deze een
        # waarde > 0
        self.level = 1
        self.level_text_id = -1
        self.update_level(self.level)

        # Maak de muren aan de randen van het speelveld. De bommen stuiteren hier tegenaan
        self.muur_links = Wall(self.canvas, 0, 40, 20, self.hoogte)
        self.muur_rechts = Wall(self.canvas, self.breedte-20, 40, self.breedte, self.hoogte)
        self.muur_boven = Wall(self.canvas, 20, 40, self.breedte-20, 60)
        self.muur_onder = Wall(self.canvas, 20, self.hoogte-20, self.breedte-20, self.hoogte)

        # Laat de score zien op het scherm. Op het begin is de score nul. Voor 
        # iedere ster die je verzameld score je 10 punten. Ook de score tekst moeten we 
        # later aanpassen dus we bewaren ook het ID van de tekst (self.score_text_id)
        self.score = 0
        self.score_text_id = -1
        self.update_score(self.score)

        # Houd een lijstje bij met de toetsen die je heb ingedrukt (meestal maar 
        # 1tje tegelijkertijd). 
        self.keys_pressed = set()

        # Zorg ervoor dat het canvas pijltjes toetsen detecteert
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress>', self.key_pressed)
        self.canvas.bind('<KeyRelease>', self.key_released)

    #=================================================================================
    def create_player(self):
        player = Player(self.canvas, 0, 0)
        x = self.breedte / 2 - player.breedte / 2 - 100
        y = self.hoogte / 2 - player.hoogte / 2
        player.move(x, y)
        return player

    #=================================================================================
    def create_bombs(self, aantal):
        bombs = []
        for i in range(aantal):
            # Maak een willekeurige x positie aan bovenin het scherm
            x = random.randint(40, self.breedte-40)
            y = 80
            # Maak een willekeurige horizontale richting aan. Deze kan 1 of -1 zijn
            richting = random.choice([-1, 1])
            bombs.append(Bomb(self.canvas, x, y, richting))
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
    def move_player(self):
        dx = 0
        dy = 0

        # Afhankelijk van welke toets was ingedrukt bepalen we de verplaatsing (dx, dy)
        # van de speler.
        if 'Left' in self.keys_pressed:
            dx = -SNELHEID_PLAYER
            dy = 0
        elif 'Right' in self.keys_pressed:
            dx = SNELHEID_PLAYER
            dy = 0
        elif 'Down' in self.keys_pressed:
            dx = 0
            dy = SNELHEID_PLAYER
        elif 'Up' in self.keys_pressed:
            dx = 0
            dy = -SNELHEID_PLAYER
        
        # Verplaats de speler en check dan of er een botsing is met een muur. Zo ja,
        # verplaats de speler terug.
        self.player.move(dx, dy)
        if self.player_has_hit_wall():
            self.player.move(-dx, -dy)

    #=================================================================================
    def key_pressed(self, event):
        # Voeg de ingedrukte toets toe aan de lijst van ingedrukte toetsen
        self.keys_pressed.add(event.keysym)

    #=================================================================================
    def key_released(self, event):
        # Verwijder de pijltjes toets uit de lijst van ingedrukte toetsen
        self.keys_pressed.discard(event.keysym)

    #=================================================================================
    def player_has_hit_wall(self):
        if self.player.hit_by(self.muur_links):
            return True
        if self.player.hit_by(self.muur_rechts):
            return True
        if self.player.hit_by(self.muur_boven):
            return True
        if self.player.hit_by(self.muur_onder):
            return True
        return False

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

        # Beweeg alle bommen in de lijst schuin door het spelerveld. Als een bom een
        # muur raakt moet de bom er vanaf stuiteren. Je geeft dat aan door de richting
        # van de bom om te draaien. Als de bom tegen de zijmuren bots dan draai je de
        # X richting om. Bots de bom tegen de boven of ondermuur, dan draai je de Y
        # richting om
        for bomb in self.bombs:
            if bomb.hit_by(self.muur_links) or bomb.hit_by(self.muur_rechts):
                bomb.move(-1, 1)
            elif bomb.hit_by(self.muur_boven) or bomb.hit_by(self.muur_onder):
                bomb.move(1, -1)
            else:
                bomb.move(1, 1)

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
        # level maar dan met een extra bom om het moeilijker te maken! We maken ook een
        # nieuwe set sterren aan en een nieuwe player
        if self.all_stars_collected():
            self.level += 1
            self.update_level(self.level)
            self.stars = self.create_stars(10)
            self.aantal_bombs += 1
            self.bombs = self.create_bombs(self.aantal_bombs)
            self.player = self.create_player()
        
        # Wacht heel even (16ms) en roep de functie game_loop nog eens aan. Hierdoor ontstaat
        # er een loop waarin de functie game_loop ongeveer 60x per seconde wordt 
        # aangeroepen
        self.app.after(16, self.game_loop)

    #=================================================================================
    def start(self):
        self.game_loop()
        self.app.mainloop()