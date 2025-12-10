let numbers = new Set();

while (true) {
    let input = prompt("Enter a number:");
    let num = Number(input);
    if (numbers.has(num)) {
        break;
    } else {
        numbers.add(num);
    }
}


let numbers1 = Array.from(numbers).sort((a, b) => a - b);

console.log("annetut numerot");
console.log(numbers1);