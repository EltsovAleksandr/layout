fetch("header.html")
    .then((response) => response.text())
    .then((data) => {
        document.getElementById("header-placeholder").innerHTML = data;
        const loginButton = document.getElementById("btn_lk");
        const loginPanel = document.getElementById("login-panel");
        loginButton.addEventListener("click", () => {
            loginPanel.classList.toggle("open");
        });
    });

loginButton.addEventListener("click", () => {
    loginPanel.classList.toggle("open");
});
