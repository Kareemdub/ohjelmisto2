"use strict"
let program = true
let number = 0
const numbers = []
while(true) {
    let number = parseInt(prompt("give a number:"))
    numbers.push(number)
    if (number === 0) {
        console.log(numbers)
        break


    }
}


document.querySelector("#number").innerHTML = numbers


