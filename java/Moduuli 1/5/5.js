`use strict`;
const year = prompt(`Insert a year to find out if it is a leap year or not`)

if (year % 4 !== 0 || year % 400 !== 0 && year % 100 === 0) {
  document.querySelector('#target').innerHTML = `The year is not a leap year.`;
}
else {
  document.querySelector('#target').innerHTML = `The year is a leap year.`;
}