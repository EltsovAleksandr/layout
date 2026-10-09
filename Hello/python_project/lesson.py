#
#
# mounth = "Февраль";
# budet = 100000;
# def vacation(mounth, budet):
#
# 	message = ""
# 	if mounth in ["Январь", "Февраль"]:
# 		if budet >= 450000:
# 			message = "Выбираем Хоккайдо! Бюджет позволяет арендовать отличное жилье прям у подъемника"
# 		elif budet >= 300000:
# 			message = "Отличный вариант - курорты Нагано. Оптимальное соотношение цены и качества"
# 		else:
# 			message = "Для пикового сезона денег маловато"
#
# 	elif mounth == "Март":
# 		message = "В марте начинается весенее катание. Снега чуть меньше, но погода солнечная, а цены на ски-пассы приятнее!"
# 	else:
# 		message = "Это не самый популярный сезон для сноуборда. возможно стоит перенести даты"
#
# 	return message
#
# print(vacation(mounth, budet))
#
# def proverka():
# 	for i in range(10):
# 		while i <= 5:
# 			print(i)
# 			i += 1
# 		else:
# 			break
#
# print(proverka())
#
#
# target_amount = 1500;
# current_amount = 0;
#
# while current_amount < target_amount:
# 	current_amount += int(input("Введи сколько положить в копилку"))
# 	print(f'Осталось еще накопить {target_amount - current_amount}')
# else:
# 	print("Нужная сумма собрана! Собираем чемоданы")




# def num(n):
# 	if n < 2:
# 		return False
# 	else:
# 		for i in range(2, n):
# 			if n % i == 0:
# 				return False
# 		return True
#
# def list(n):
# 	l = []
# 	for i in range(1, n + 1):
# 		if num(i):
# 			l.append(i)
# 	return l
# print(list(30))

# def count_vowels(s):
#
# 	vowels = ['a', 'e', 'i', 'o', 'u']
# 	count = 0
#
# 	for i in s:
# 		while not i.isdigit():
# 			if i.lower() in vowels:
# 				count += 1
# 				break
# 			else:
# 				break
# 		else:
# 			break
# 	return count
#
# print(count_vowels('he23llo'))

# def pyramids (h):
# 	spaces = h - 1
# 	for i in range (1, h + 1):
# 		print (' ' * spaces, end = '')
# 		print ('*' * (2 * i - 1))
# 		spaces -= 1
#
#
# pyramids (5)
