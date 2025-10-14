from game import Game
from playerfield import PlayerField


def main():
    # Maak een nieuwe game
    game = Game()
    game.title('Coding4Kids')

    # Maak een spelerveld
    player_field = PlayerField(game)

    # Maak de speler en een bom
    player_field.create_player()
    player_field.create_bomb()
    
    # Start game
    game.start(player_field)


if __name__ == '__main__':
    main()