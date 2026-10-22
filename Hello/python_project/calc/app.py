import operator
from flask import Flask, request, render_template

app_calc = Flask(__name__)

def calculating (expression):
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

    for i in expression.split():
        try:
            number = float(i)
            num.append(number)
        except ValueError:
            if i in operators:
                op = operators[i]
            

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
    return res
    
    
    
@app_calc.route("/", methods=["POST", "GET"])
def calc():

    if request.method == "POST":
        a = request.form["expression"]
        result = calculating(a)
        return render_template("index.html", result = result)
    else:
        return render_template("index.html")




# print(eval(input('>>>>')))

@app_calc.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    print(data)
    return "Данные получены"

app_calc.run(debug=True)