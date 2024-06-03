let input = prompt()*1;
let numbers = input.split(' ').map(Number);
let sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum);