const num1 = +prompt('Give me an integer:');
const num2 = +prompt('Give me a second integer:');
const num3 = +prompt('Give me a third integer:');

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.querySelector('#target').innerHTML = `The sum is ${sum}, the product is ${product}, and the average is ${average}`;