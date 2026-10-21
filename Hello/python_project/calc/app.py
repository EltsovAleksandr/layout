import operator
from flask import Flask, request, render_template

app_calc = Flask(__name__)

@app_calc.route("/", methods=["POST", "GET"])
def calc():
    if request.method == "POST":
        a = request.form["expression"].split() 
        num = []
        op = None
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
            try:
                number = float(i)
                num.append(number)
            except ValueError:
                if i in operators:
                    op = operators[i]
                
            # if i.isdigit():
            #     num.append(int(i))
            # elif i in operators:
            #     op = operators[i]

        if op is None:
            res = "Неккоректный оператор"
        else:   
            if len(num) != 2:
                res = "Введите два значения и оператор через пробел"
            else:    
                try:
                    res = op(num[0], num[1])
                except ZeroDivisionError:
                    res = "Делить на ноль нельзя"

        return render_template("index.html", result = res)
    else:
            return render_template("index.html")

app_calc.run()


# print(eval(input('>>>>')))

