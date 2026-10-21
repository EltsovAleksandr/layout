import random

x = random.randint(1, 100)
num = int(input("Введите число от 1 до 100: "))

while num != x:
    print(x)
    if num > x:
        print("Ваше число больше загаданного")
        num = int(input())
    elif num < x:
        print("Ваше число меньше загаданного")
        num = int(input())
    elif x < 1 and x > 100:
        print("Вы ввели число вне диапазона")
        num = int(input())
print(f'Урааа вы победили число {x}')
        