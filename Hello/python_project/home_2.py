import random
from getpass import getpass


print([i for i in range(11) if i % 2 != 0]) # 1.Вывести числа от 1 до 10 кроме четных

for i in range(1, 21): # 2.Выведите все числа от 1 до 20 но остановитесь как только дойдет до 7

    print(i)
    i += 1
    break


print([i for i in range(1, 16) if i % 3 == 0]) # 3.Выведите числа от 1 до 15 пропуская те что делятся на 3 без остатка


l = [12,34,78,5,90,23] # 4.Пройдите по списку [12,34,78,5,90,23] и выведите первое число больше 50 затем остановитесь

for i in l:
    if i > 50:
        print(i)
        break

def password_verification(): # 5.Запрашивайте пароль пока пользователь не введет "pyton" максимум 3 попытки потом выход"

    password = getpass("Введите пароль: ")
    count = 3

    while password != 'pyton':
        if count > 1:
            password = getpass(f'Не верная попытка ввода пароля, осталось попыток {count - 1}: ')
            count -= 1
        else:
            print("Вы ввели 3 раза неправильно, повторите позднее")
            break
    else:
        print("Ввели правильный пароль")
password_verification()


l = 0 # 6.Запрашивайте числа пока не введен 0 считайте сумму если введено отрицательное пропустите его

n = int(input('Дай мне циферку'))
while n != 0:
    if n > 0:
        l += n
        n = int(input('Дай мне циферку'))
    else:
        n = int(input('Дай мне циферку'))
print(l)


# names = ["Алексей", "Мария", "Дмитрий", "Оля", "Иван", "Анна", "оля", "Сергей"] # 7.Дан список имен найдите есть ли в нем "Оля" если есть выведите "Нашли" если нет то "Нет в списке" 

search_name = "Оля"
status = "Нет в списке"
names = ["Алексей", "Мария", "Дмитрий", "Иван", "Анна", "Сергей", "Екатерина"]
for i in names:
    if i.lower() == search_name.lower():
        status = "Нашли"
        break      
print(status)


l = [3, -1, 5, -7, 2, -4, 8] # 8.дан список [3, -1, 5, -7, 2, -4, 8] Выведите только положительные числа
print([i for i in l if i > 0])


r = random.randint(1, 20) # 9.Программа загадывает число от 1 до 20 пользователь угадывает но у него максимум 5 попыток есть подсказки больше/меньше если не угадал то проигрыш
attempt = 4

while attempt >= 0:
    n = int(input("Введи число от 1 до 20: "))
    # print(r, n, attempt)
    if n < 1 or n >20:
        print("Ты ввел число вне диапазона, но я сохраню твою попытку так уж и быть")
        
    elif n == r:
        print("Ты выиграл")
        break
    elif attempt == 0:
        print("Извини не в этот раз")
        attempt -= 1
    else:
        print(f'Осталось попыток {attempt}')
        attempt -= 1
        if n > r:
            print("Неправильно, но я даю тебе подсказку: Твоё число больше чем загаданное")
        else:
            print("Неправильно, но я даю тебе подсказку: Твоё число меньше чем загаданное")
            


l = [1, 2, 3, 4, 3, 5, 6] # 10.Дан список [1, 2, 3, 2, 5, 6] Идите по нему и остановитесь как только встретите число которе уже было раньше 
l_prov = []

for i in l:
    if i in l_prov:
        break
    else:
        l_prov.append(i)
    print(i)
    
    

n = 9
def prime_numbers(n): # 1. Выведите все простые числа от 2 до N используя вложенные циклы и break
    
    l= []
    for i in range(2, n+1):
        status = True
        for j in range(2, i):
            if i % j == 0:
                status = False
                break
            # else:
            #     status = True
        if status == True:
            l.append(i)
    return l

print(prime_numbers(n))


def pyramids (h): # 2. Запросите высоту h и нарисуйте пирамиду
    
	spaces = h - 1
	for i in range (1, h + 1):
		print (' ' * spaces, end = '')
		print ('*' * (2 * i - 1))
		spaces -= 1

pyramids (5)


def multiplication_table(): # 3.Выведите таблицу умножения от 1 до 9 но пропустите строки где первый множитель четный и остановитесь когда первый множитель равен 8 
    
    for i in range(1, 10):
        if i ==8 :
            break
        elif i % 2 == 0:
            continue
        else:
            for j in range(1, 10):
                print(i * j, end = ' ')
            print(" ")
        
multiplication_table()


def count_vowels(s):# 4. Запросите строку и идите по символам если символ это цифра остановитесь если гласная то увеличте счетчик остальные пропускайте выведите колличество гласных до первой цифры 

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for i in s:
        if i.lower() in vowels:
            count += 1
        elif i.isdigit():
            break
    return count

print(count_vowels('AEIOU7'))


def ATM_machine(): # 5.Банкомат где начальная сумма 1000 есть меню где 1- пополнить 2-снять 3-показать баланс 0-выход при снятии больше баланса отказ при неверной команде пропустить при 0 выйти и показать итоговый баланс

    balance = 1000
    n = int(input("Введи команду: "))
    while n != 0:
        if n == 1:
            x = int(input("Сколько необходимо внести на баланс: "))
            balance += x
        elif n == 2:
            x = int(input("Сколько необходимо снять с баланса: "))
            if x > balance:
                print ("На вашем балансе не достаточно средств")
            else:
                balance -= x
        elif n == 3:
            print(f'Ваше баланс составляет: {balance} рублей')
        else: 
            print("Не верная команда")
        n = int(input("Введи команду: "))
    print(f'Ваше баланс составляет: {balance} рублей')
ATM_machine()



