import time


def main():

    print_tekst = True
    if print_tekst:
        print('Hallo, wereld!')
    else:
        print('Hoi')

    print_tekst = False
    if print_tekst:
        print('Hallo, wereld!')
    else:
        print('Hoi')

    hoogte = 10
    if hoogte == 10:
        print('Hoogte is 10')
    else:
        print('Hoogte is NIET 10')

    if hoogte > 10:
        print('Hoogte is groter dan 10')
    else:
        print('Hoogte is kleiner dan of gelijk aan 10')

    if hoogte >= 10:
        print('Hoogte is groter dan of gelijk aan 10')
    else:
        print('Hoogte is kleiner dan 10')

    if 3 < hoogte < 6:
        print('Hoogte is groter dan 3 maar kleiner dan 6')
    else:
        print('Hoogte is kleiner dan of gelijk aan 3 OF groter dan of gelijk aan 6')


if __name__ == '__main__':
    main()