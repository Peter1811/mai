import random

DAYS = 31
MONTHS = 12
YEARS = 9999
MAX_NUM = 2 ** 64 - 1
kol_of_strings = int(input())

with open('input.txt', 'w') as file:
    for i in range(kol_of_strings):
        string = ''
        day = random.randrange(DAYS)
        month = random.randrange(MONTHS)
        year = random.randrange(YEARS)
        string += str(day) + '.' + str(month) + '.' + str(year)
        string += '\t' + str(random.randrange(MAX_NUM))
        string += '\n'
        file.write(string)


