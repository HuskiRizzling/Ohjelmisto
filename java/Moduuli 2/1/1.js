`use strict`;
const numbers = [];

numbers[0] = +prompt(`Give me a number:`);
numbers[1] = +prompt(`Give me a second number:`);
numbers[2] = +prompt(`Give me a third number:`);
numbers[3] = +prompt(`Give me a fourth number:`);
numbers[4] = +prompt(`Give me a fifth number:`);

for (let i = 4; i >= 0; i--) {
  console.log(numbers[i]);
}
