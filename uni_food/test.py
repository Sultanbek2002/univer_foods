from random import random, randint

arg = ''
for i in range(0, 6):
    arg += f'{randint(0, 10)}'
print('er' * 20)
print(type(arg))
