(() => {
  "use strict";

  const forms = document.querySelectorAll(".needs-validation");
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );
  });
})();

/*Toast Animations */
document.addEventListener("DOMContentLoaded", (event) => {
  var myToastEl = document.getElementById("myToast");
  var myToast = new bootstrap.Toast(myToastEl, {
    animation: true,
    autohide: true,
    delay: 5000,
  });
});
/*Theme Toggle */
$(document).ready(() => {
  const body = document.querySelector("body");
  const checkbox = document.getElementById("theme");
  loadTheme();
  checkbox.addEventListener("change", (e) => {
    const currentTheme = e.target.checked;
    updateTheme(currentTheme);
    updateThemeLocalStorage(currentTheme);
  });
  function loadTheme() {
    window.localStorage.getItem("dark")
      ? (checkbox.checked =
          JSON.parse(window.localStorage.dark) == true ? false : true)
      : updateThemeLocalStorage(checkbox.checked);
    updateTheme(!JSON.parse(window.localStorage.dark));
  }
  function updateTheme(currentTheme) {
    body.setAttribute("data-bs-theme", currentTheme ? "light" : "dark");
  }
  function updateThemeLocalStorage(currentTheme) {
    window.localStorage.dark = !currentTheme;
  }
});
