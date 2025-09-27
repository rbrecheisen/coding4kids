def main():

    bericht = 'Welkom bij Coding4Kids!'
    print(bericht)
    print(type(bericht))

    nummer = 5
    print(nummer)
    print(type(nummer))
    print(f'Het nummer is: {nummer}')

    nummer = 23.451
    print(nummer)
    print(type(nummer))

    x = False
    print(x)
    print(type(x))

    y = [1, 2, 3, 4]
    print(y)
    print(type(y))
    print(y[0])
    print(y[3])

    z = {'a': 1, 'b': 2, 'c': 3}
    print(z)
    print(type(z))
    print(z['a'])
    print(z['c'])
    print(z.keys())
    print(z.values())


if __name__ == '__main__':
    main()