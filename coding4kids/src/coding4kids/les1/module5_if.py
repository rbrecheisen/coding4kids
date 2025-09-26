import time


def main():
    print_tekst = True
    if print_tekst:
        print('Hallo, wereld!')
    else:
        print('')

    print_tekst = False
    if print_tekst:
        print('Hallo, wereld!')
    else:
        print('')

    hoogte = 10
    if hoogte == 10:
        print('Hoogte is 10')
    else:
        print('Hoogte is NIET 10')

    if hoogte > 10:
        print('Hoogte is groter dan 10')

    if hoogte >= 10:
        print('Hoogte is groter dan of gelijk aan 10')

    if 3 < hoogte < 12:
        print('Hoogte ligt tussen de 3 en 12')
    else:
        print('Hoogte is kleiner/gelijk aan 3 of groter/gelijk aan 12')


if __name__ == '__main__':
    main()