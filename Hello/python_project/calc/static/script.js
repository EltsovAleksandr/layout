const screen = document.getElementById("display");
const buttons = document.querySelectorAll(".keyboard");
let justCalculated = false;
buttons.forEach((button) => {
    button.addEventListener("click", () => {
        if (justCalculated) {
            if ("1234567890".includes(button.textContent)) {
                screen.value = "";
            }
            justCalculated = false;
        }
        if (button.textContent == "AC") {
            screen.value = "";
            justCalculated = false;
        } else if (button.textContent === "+/-") {
            let end_elem = screen.value.split(" ");
            let elem = end_elem[end_elem.length - 1];
            if (Number.isFinite(Number(elem))) {
                if (elem.startsWith("-")) {
                    elem = elem.slice(1)
                } else {
                    elem = "-" + elem
                }
                end_elem[end_elem.length - 1] = elem
                screen.value = end_elem.join(" ")
            }
        } else if (button.textContent === "=") {
            fetch("/calculate", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    expression: screen.value,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    /*получает ответ Flask в формате JSON.*/
                    screen.value = data.result;
                    justCalculated = true;
                    console.log(
                        "Вычисление завершено:",
                        justCalculated,
                    ); /*сообщает калькулятору, что вычисление завершено*/
                });
        } else {
            if ("+-*/%".includes(button.textContent)) {
                screen.value += " " + button.textContent + " ";
            } else {
                screen.value += button.textContent;
            }
        }
        console.log(screen.value);
    });
});

console.log(screen);
