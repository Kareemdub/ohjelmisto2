'use strict'

let num1
let num2
let num3
num1 = prompt("Give 1st number");
num2 = prompt("Give 2nd number");
num3 = prompt("Give 3rd number");

num1 = parseInt(num1)

num2 = parseInt(num2)
num3 = parseInt(num3)

document.querySelector('#number').innerHTML = `Sum of numbers is ${num1+num2+num3}, Product of numbers is ${num1 * num2 * num3}, Average of numbers is ${(num1 + num2 + num3)/ 3}`;
