fetch("header.html")
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("header-placeholder").innerHTML = data;
        const loginButton = document.getElementById("btn_lk");
        const loginPanel = document.getElementById("login-panel");
        document.addEventListener("click", (event) => {
            if (
                !loginPanel.contains(event.target) &&
                !loginButton.contains(event.target)
            ) {
                loginPanel.classList.remove("open");
            }
        });
        document.addEventListener("keydown", (event) => {
            if (event.key === "Escape") {
                loginPanel.classList.remove("open");
            }
        });

        loginButton.addEventListener("click", () => {
            loginPanel.classList.toggle("open");
        });
    });

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        loginPanel.classList.remove("open");
    }
});
