class Dude:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def spring(self):
        print('Ik spring omhoog!')

    def geraakt(self, x, y):
        if x == self.x and y == self.y:
            return True
        else:
            return False


def main():
    speler = Dude(0, 0)
    speler.spring()
    if speler.geraakt(5, 5):
        print('Dude is geraakt!')
    if speler.geraakt(0, 0):
        print('Dude is geraakt!')


if __name__ == '__main__':
    main()