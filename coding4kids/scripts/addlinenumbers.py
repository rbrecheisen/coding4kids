import os
import sys


def main(file_name):
    print(os.getcwd())
    file_path = os.path.join(os.getcwd(), f'src/coding4kids/codeexamples/{file_name}')
    if os.path.exists(file_path):
        print(file_path)
        with open(file_path, 'r') as f:
            line_nr = 1
            for line in f.readlines():
                line = line.rstrip('\r\n')
                print(f'{line_nr}\t{line}')
                line_nr += 1


if __name__ == '__main__':
    main(sys.argv[1])