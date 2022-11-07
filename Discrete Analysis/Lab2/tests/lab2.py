import random

COMMANDS = ['+', '-', '']
MAX_LEN = 256
MAX_NUM = 2 ** 64 - 1
ALPHABET = [chr(k) for k in range(ord('a'), ord('z') + 1)] \
           + [chr(k) for k in range(ord('A'), ord('Z') + 1)]

kol_of_tests = int(input())

with open('input.txt', 'w') as file:

    for i in range(kol_of_tests):
        string = ''
        choice = random.choice(COMMANDS)
        string += choice
        if choice == '+' or choice == '-':
            string += ' '
        length = random.randrange(MAX_LEN)
        for _ in range(length):
            string += random.choice(ALPHABET)
        if choice == '+':
            string += '\t'
            string += str(random.randrange(MAX_NUM))
        string += '\n'

        file.write(string)
    



