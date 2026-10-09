import random
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
# 	print("Нужная сумма собрана! Собираем чемоданы")1

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