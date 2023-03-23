// CALENADR
const date = new Date();

let current_year = date.getFullYear();
let today_date = date.getDate();
let today_day = date.getDay();

console.log(today_date);
console.log(today_day);

const isLeapYear = (year) => {
    return (
        (year % 4 === 0 && year % 100 !== 0 && year % 400 !== 0) ||
        (year % 100 === 0 && year % 400 === 0)
    );
};
const getFebDays = (year) => {
    return isLeapYear(year) ? 29 : 28;
};

let days_of_month = [
    31,
    getFebDays(current_year),
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
];

const month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
];

const week_days = [
    'M',
    'T',
    'W',
    'T',
    'F',
    'S',
    'S'
];

let calendar_date = document.querySelector('#calendar-date');
let calendar_month = document.querySelector('#calendar-month');
let calendar_year = document.querySelector('#calendar-year');

calendar_month.innerHTML = `${month_names[date.getMonth()]}`;
calendar_year.innerHTML = date.getFullYear();


let date_div = document.querySelector('#date');
let children = date_div.children;

for (let i = 0; i < children.length; i++) {
    let weekday_date = today_date - today_day + (i + 1);
    if (weekday_date >= 1 && weekday_date <= days_of_month[date.getMonth() - 1]) {
        children[today_day - 1].classList.add("week-date-active");
        if (weekday_date < 10) {
            children[i].innerHTML = "0" + weekday_date;
        }
        else {
            children[i].innerHTML = weekday_date;
        }
    }
    else {
        children[i].innerHTML = "  ";
    }
}