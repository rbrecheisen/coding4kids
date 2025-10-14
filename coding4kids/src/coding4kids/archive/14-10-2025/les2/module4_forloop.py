import time


def main():

    for i in range(5):
        print('Hallo, wereld!')
        time.sleep(1)

    x = 5
    for i in range(x):
        print('Hallo, wereld!')
        time.sleep(1)

    y = [1, 2, 3, 4, 5]
    for i in range(len(y)):
        print(y[i])
        time.sleep(1)

    z = {'a': 1, 'b': 2, 'c': 3}
    for k in z.keys():
        print(z[k])
    for k, v in z.items():
        print(v)


if __name__ == '__main__':
    main()