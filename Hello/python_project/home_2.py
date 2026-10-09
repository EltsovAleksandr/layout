# print([i for i in range(11) if i % 2 != 0])

for i in range(1, 21):
    while i <= 7:
        print(i)
        i += 1
    break

print([i for i in range(1, 16) if i % 3 == 0])


l = [12,34,78,5,90,23]
for i in l:
    if i > 50:
        print(i)
        break


password = input()
count = 0

while password != 'pyton':
    if count < 2:
        password = input()
        count += 1
    else: 
        break


l = 0

n = int(input('Дай мне циферку'))
while n != 0:
    if n > 0:
        l += n
        n = int(input('Дай мне циферку'))
    else:
        n = int(input('Дай мне циферку'))

print(l)


# names = ["Алексей", "Мария", "Дмитрий", "Оля", "Иван", "Анна", "оля", "Сергей"]
search_name = "Оля"
status = "Нет в списке"
names = ["Алексей", "Мария", "Дмитрий", "Иван", "Анна", "Сергей", "Екатерина"]
for i in names:
    if i.lower() == search_name.lower():
        status = "Нашли"
        break
        
print(status)


l = [3, -1, 5, -7, 2, -4, 8]
print([i for i in l if i > 0])


r = random.randint(1, 20)
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
            


l = [1, 2, 3, 4, 3, 5, 6]
l_prov = []

for i in l:
    if i in l_prov:
        break
    else:
        l_prov.append(i)
    print(i)
    
    
# 1. Выведите все простые числа от 2 до N используя вложенные циклы и break
n = 9

def prime_numbers(n):
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



def count_vowels(s):

	vowels = ['a', 'e', 'i', 'o', 'u']
	count = 0

	for i in s:
		while not i.isdigit():
			if i.lower() in vowels:
				count += 1
				break
			else:
				break
		else:
			break
	return count

print(count_vowels('he23llo'))



def pyramids (h):
	spaces = h - 1
	for i in range (1, h + 1):
		print (' ' * spaces, end = '')
		print ('*' * (2 * i - 1))
		spaces -= 1


pyramids (5)