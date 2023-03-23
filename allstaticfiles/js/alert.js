let alertCloseIcon = document.querySelector('#alert-close-icon');
alertCloseIcon.addEventListener("click", () => {
    console.log("This btn is clicked!");
    let alert = document.querySelector('.alert');
    // $('.alert').css({ "display": "none" });
    alert.style.display = "none";
});