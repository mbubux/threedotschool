// GREET ADMIN
function greetAdmin() {

    let greet = document.querySelector('#greet');

    const new_dt = new Date();
    let hour = new_dt.getHours();

    if (hour <= 12) {
        greet.innerHTML = "Good Morning!";
    }

    else if (hour > 12 && hour < 15) {
        greet.innerHTML = "Good Afternoon!";
    }

    else {
        greet.innerHTML = "Good Evening!";
    }
}


// FOOTER COPYRIGHT YEAR UPDATE
function CopyrightYearUpdate() {

    let copyright_year = document.querySelector('#copyright-year');

    const new_date = new Date();
    console.log(typeof(new_date));
    copyright_year.innerHTML = new_date.getFullYear();
}


// Time
function time() {
    const hr = document.querySelector('.hour');
    const min = document.querySelector('.minute');
    const sec = document.querySelector('.second');

    const d = new Date();
    let hour = d.getHours();
    let minute = d.getMinutes();
    let second = d.getSeconds();

    (hour < 10) ? hr.innerHTML = "0" + hour : hr.innerHTML = hour;
    (minute < 10) ? min.innerHTML = "0" + minute : min.innerHTML = minute;
    (second < 10) ? sec.innerHTML = "0" + second : sec.innerHTML = second;
}
var interval = setInterval(time, 1000);

// ==================================================

