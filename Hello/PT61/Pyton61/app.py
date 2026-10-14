name = "Анна"
# str
age = 15
# int
height = 1.70
# float
is_student = True
# bool

print("Привет, мир!")
name = input("Как у вас имя?")

x = 10;
y = 3;

print(x + y)
# сумма
print(x - y)
# разность
print(x * y)
# умножение
print(x / y)
# деление
print(x // y)
# целочисленное деление
print(x % y)
# остаток от деления
print(x ** y)
# степень


age = 18
# If - если
if age >= 18:
    print("Продаем товар")
elif age > 0:
    print("Ребенок")
else:
    print("Не продаем товар")




#  = это присвоение
# == это когда мы сравниваем


    name = "Мама"
    if name == "Мама":
        print("Написана Мама")
    else:
        print("Написан Папа")


        # от 0 до 4
for i in range(5):
    print(i)
# от 1 до 5
for i in range(1, 6):
    print(i)
# по возрастанию с шагом 2
for i in range(0, 10, 2):

    print(i)
# обратный
for i in range(10, 0, -1):
    print(i)


    # fruts = ["яблоко","апельсин","виноград"]

# for frut_po_odnomu in fruts:
#     print(frut_po_odnomu)

# for element_stroki in "Привет":
#     print(element_stroki)

# fruts = ["яблоко","апельсин","виноград"]

# for i, frut_po_odnomu in enumerate(fruts):
#     print(i, frut_po_odnomu)


# person = {"имя": "Иван", "возраст": 30}

# for key in person:
#     print(key)

# for value in person.values():
#     print(value)

# for key, value in person.items():
#     print(key, value)


# n = 0

# Пока n меньше 5 то делай
# while n < 5:
#     print(n)
    # удобнее использовать вот такую запись в место этой n += 1
    # n = n + 1

# break - досрочно выйти из цикла
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue - пропустить итерацию(одно действие) и перейти к следующей

# for i in range(6):
#     if i % 2 == 0:
#         continue #пропускаем четные
#     print(i) 

# задание номер 4 решение 
nums = [12, 34, 78, 5, 98, 23]
for n in nums:
    if n > 50:
        print(n)
        break