import tkinter as tk
import random

from gameobjects import Player, Bomb, Star, Wall

SNELHEID_PLAYER = 10
SNELHEID_BOMB = 5


class Game:

    #=================================================================================
    def __init__(self, title):

        # Maak app object wat de game gaat uitvoeren
        self.app = self.create_app(title)

        # Laad achtergrond plaatje en bewaar de afmetingen in een variabele. Dat is 
        # dus de breedte en de hoogte van het plaatje
        self.background = tk.PhotoImage(file='coding4kids/src/coding4kids/resources/sky.png')

        # Maak het speelveld. We noemen dit een canvas (net als een schilderijg) waarop
        # je dingen kunt tekenen.
        self.canvas = self.create_canvas(self.app, self.background)

        # Het achtergrond plaatje bepaald hoe groot het canvas (speelveld) is. We bewaren
        # de breedte (width) en hoogte (height) in twee variabelen omdat we ze later nodig
        # hebben, b.v. om het midden van het speelveld te bepalen
        self.width = self.background.width()
        self.height = self.background.height()

        # Maak een nieuwe speler aan en verplaats hem naar het midden van het scherm.
        # Het midden bereken je door de helft van het speelveld te nemen en daar de 
        # helft van de speler vanaf te trekken. Dat wordt je x positie. Hetzelfde doe
        # je voor de y positie.
        self.player = self.create_player()

        # Maak een variabele voor het aantal bommen in je game. We beginnen met 1 bom
        # in het eerste level
        self.nr_bombs = 1

        # Maak de bommen. De variabele self.nr_bombs geeft aan hoeveel bommen we willen
        self.bombs = self.create_bombs(self.nr_bombs)

        # Maak een variabele voor het aantal sterren dat je moet verzamelen. We pakken
        # hier tien sterren maar je kunt ook een ander getal kiezen
        self.nr_stars = 10

        # Maak de sterren. De variabele self.nr_stars geeft aan hoeveel sterren
        self.stars = self.create_stars(self.nr_stars)

        # Maak een variabele voor het level waarin je zit. We beginnen bij het eerste level
        self.level = 1

        # Het level wordt in de game weergegeven door tekst. Deze tekst wordt bovenin het
        # scherm afgebeeld. De eerste keer, maken we de tekst nieuw aan. We krijgen dan 
        # een nummer, ook ID genoemd, waarmee we de tekst later kunnen aanpassen (b.v., 
        # als we naar het volgende level gaan). Het ID dat we krijgen bij het maken van de
        # tekst is altijd groter dan nul.
        # We maken dus een variabele aan voor het ID van de tekst en we roepen een functie
        # aan om de tekst te maken. Deze functie geeft het ID terug van de tekst.
        self.level_text_id = self.create_text(
            'Level ' + str(self.level), 
            self.width - 60,
            20,
            'white',    # Tekst wit
            16,         # Grootte van de letters
        )

        # Maak een variabele voor de score
        self.score = 0

        # De score wordt in het game ook als tekst weergegeven
        self.score_text_id = self.create_text(
            'Score: ' + str(self.score),
            self.width / 2 - self.player.width / 2,
            20,
            'yellow',
            16,
        )

        # Maak de vier muren aan die het speelveld omringen. De muren zijn 20 pixels breed.
        # De positie van de muren wordt bepaald door de positie (x0,y0) van de linker 
        # bovenhoek en de positie (x1,y1) van de rechter onderhoek op het canvas. Dit is 
        # hieronder aangegeven:
        #
        # (x0,y0)----------+
        #    |             |
        #    |             |
        #    |             |
        #    |             |
        #    |             |
        #    +----------(x1,y1)
        #
        # Eerst maken we de linker muur
        self.wall_left = self.create_wall(
            0, 
            40, 
            20, 
            self.height,
        )

        # Dan maken we de rechter muur
        self.wall_right = self.create_wall(
            self.width-20, 
            40, 
            self.width, 
            self.height,
        )

        # Dan maken we de bovenste muur
        self.wall_top = self.create_wall(
            20,
            40,
            self.width-20,
            60,
        )

        # En als laatste de onderste muuur
        self.wall_bottom = self.create_wall(
            20,
            self.height-20,
            self.width-20,
            self.height,
        )

        # Houd een lijstje bij met de toetsen die je heb ingedrukt (meestal maar 
        # 1tje tegelijkertijd). 
        self.keys_pressed = set()

        # Zorg ervoor dat het canvas pijltjes toetsen detecteert
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress>', self.key_pressed)
        self.canvas.bind('<KeyRelease>', self.key_released)

    #=================================================================================
    def create_app(self, title):
        app = tk.Tk()
        app.title = title
        return app
    
    #=================================================================================
    def create_canvas(self, app, background):
        canvas = tk.Canvas(
            app, width=background.width(), height=background.height())
        canvas.pack()
        canvas.create_image(0, 0, image=background, anchor='nw')
        return canvas

    #=================================================================================
    def create_text(self, text, x, y, color, size):
        text_id = self.canvas.create_text(
            x, y, text=text, fill=color, font=('Helvetica', size, 'bold'))
        return text_id

    #=================================================================================
    def create_wall(self, x0, y0, x1, y1):
        return Wall(self.canvas, x0, y0, x1, y1)
    
    #=================================================================================
    def create_player(self):
        player = Player(self.canvas, 0, 0)
        x = self.width / 2 - player.width / 2 - 100
        y = self.height / 2 - player.height / 2
        player.move(x, y)
        return player

    #=================================================================================
    def create_bombs(self, aantal):
        bombs = []
        for i in range(aantal):
            # Maak een willekeurige x positie aan bovenin het scherm
            x = random.randint(40, self.width-40)
            y = 80
            # Maak een willekeurige horizontale richting aan. Deze kan 1 of -1 zijn
            richting = random.choice([-1, 1])
            bombs.append(Bomb(self.canvas, x, y, richting))
        return bombs
    
    #=================================================================================
    def create_stars(self, aantal):
        stars = []
        for i in range(aantal):
            x = random.randint(40, self.width-40)
            y = random.randint(60, self.height-40)
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
        if self.player.hit_by(self.wall_left):
            return True
        if self.player.hit_by(self.wall_right):
            return True
        if self.player.hit_by(self.wall_top):
            return True
        if self.player.hit_by(self.wall_bottom):
            return True
        return False

    #=================================================================================
    def display_game_over(self):
        # Bepaal x positie van het midden van het scherm, en de y positie een stukje
        # onder de bovenkant van het scherm. Teken dan de tekst "GAME OVER" op het
        # scherm op de positie (x, y) in rode kleur en grote letters
        x = self.width / 2 - self.player.width / 2
        y = 200
        self.create_text('GAME OVER', x, y, 'red', 32)
        
    #=================================================================================
    def update_text(self, text_id, text):
        self.canvas.itemconfig(text_id, text=text)
        
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
            if bomb.hit_by(self.wall_left) or bomb.hit_by(self.wall_right):
                bomb.move(-1, 1)
            elif bomb.hit_by(self.wall_top) or bomb.hit_by(self.wall_bottom):
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
                self.update_text(self.score_text_id, 'Score: ' + str(self.score))
                self.stars.remove(star)
                break
        
        # Check of alle sterren zijn verzameld. Zo ja, dan beginnen we met het volgende
        # level maar dan met een extra bom om het moeilijker te maken! We maken ook een
        # nieuwe set sterren aan en een nieuwe player
        if self.all_stars_collected():
            self.level += 1
            self.update_text(self.level_text_id, 'Level ' + str(self.level))
            self.stars = self.create_stars(10)
            self.nr_bombs += 1
            self.bombs = self.create_bombs(self.nr_bombs)
            self.player = self.create_player()
        
        # Wacht heel even (16ms) en roep de functie game_loop nog eens aan. Hierdoor ontstaat
        # er een loop waarin de functie game_loop ongeveer 60x per seconde wordt 
        # aangeroepen
        self.app.after(16, self.game_loop)

    #=================================================================================
    def start(self):
        self.game_loop()
        self.app.mainloop()