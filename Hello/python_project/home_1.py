import operator

def calc():

	a = input("Введи данные для расчета . Пример 125 * 8: ").split()
	num = []
	operators = {
		"+": operator.add,
		"-": operator.sub,
		"*": operator.mul,
		"/": operator.truediv,
		"//": operator.floordiv,
		"**": operator.pow,
		"%": operator.mod
	}

	for i in a:
		if i.isdigit():
			num.append(int(i))
		elif i in operators:
			op = operators[i]

	try:
		res = op(num[0], num[1])
	except ZeroDivisionError:
		res = "Делить на ноль нельзя"
	except KeyError:
		res = "Не правильный оператор"
	except UnboundLocalError:
		res = "Введите два значения и оператор через пробел"

	return res

print(calc())