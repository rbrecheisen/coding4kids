class Dude:

    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def spring(self):
        print('Ik spring')

    def geraakt(self, x, y):
        return True


def main():
    speler = Dude(0, 0)
    speler.spring()
    if speler.geraakt():
        print('Dude is geraakt!')


if __name__ == '__main__':
    main()