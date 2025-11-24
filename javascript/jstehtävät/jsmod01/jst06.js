"use strict"

let ask = confirm("Should I calculate the square root?")

if (ask === true){
    let number = prompt("Give number to calculate")
    number = parseFloat(number)
    document.querySelector("#calculate").innerHTML = "The Square root of " + number + " is " + Math.sqrt(number)
}
else{
    document.querySelector("#nocalculate").innerHTML = "The square root is not calculated"
}
