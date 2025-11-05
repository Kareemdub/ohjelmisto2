//taulukko eli array

let emptyArray = []

let items = [1, 2, 3, 4, {name: "Ulla"}, [0, 5], "merkkijono"]

console.log(items);

console.log(items[3]); // alkioon viittaan indexillä

// alkion arvoa muuttaa indexin avulla

items[2] = 10
console.log(items);

items[9] = "olen uusi alkio"
//välissä on nyt määrittelemätömmiä alkioita "undefined"
console.log(items);

let fruits = ["Banaani", "Mango", "Omena"]

console.log(fruits);
console.log("Taulukon pituuuus", fruits.length)

let elem = document.querySelector("#heading");

console.log(elem);
console.dir(elem);
elem.innerText = "Mod 2 esimerkitsss";

//taulukon looppaus eritavoin

//perinteinen
console.log("--------------")





for (let i = 0; i < fruits.length ; i++) {
    console.log(`hedelmä ${i+1} on: ${fruits[i]}`);

}

console.log("---------------");
//for of
for (let fruit of fruits) {

    console.log(fruit);
}



//for in, harvemmin käytetään taulukoiden kanssa

for (let index in fruits) {
    console.log(index);
}

fruits.sort();
console.log(fruits);
fruits.reverse();
console.log(fruits);

const ages = [2300, 23, 55, 12]
ages.sort();

ages.sort((a, b) => a - b);

console.log(ages);
ages.sort((a, b) => b - a);
console.log(ages);

// poistetaan taulukon eka arvo ja otetaan muuttuja talteen
let hedelmat = ["Banaani", "Mango", "Omena"]


const hedelma = hedelmat.shift();
console.log("poistettiin",hedelma);
console.log(hedelmat);
//unshift lisää listan ensimmäiseksi
hedelmat.unshift("Kiwi");
console.log(hedelmat);

const vika = hedelmat.pop()
console.log(hedelmat)

hedelmat.push("Satsuma", "Mandariini", "Bansku")
console.log(hedelmat)

console.log(hedelmat.includes(vika))
console.log(vika)

const duck = {
    name: "Aku",
    age: 313
}
//object literal, olio
//samanlainen sanakirja kuin pythonissa
console.log(duck);
console.log(duck["name"]);

//muutetaan arvoja

duck["name"] = "Aku Ankka";
console.log(duck);

//haetaan ja muutetaan nimi

console.log(duck.name)
duck.name = "Akun Anak";
console.log(duck);

duck.profession = "Working like a duck";
duck.profession = "Swimming like a duck";
console.log(duck);

let sayHello = `Heippa ${duck.name}`;
console.log(sayHello)

delete duck.profession;
console.log(duck)

let duck2 = {
    name: "Roope Ankka",
    age: 69,

    getInfo: function () {
        return this.name + " on " + this.age + "-vuotias"
    }
}
let info = duck2.getInfo()

console.log(info)

//js funktiot

//ns perinteinen funktion määrittely

function greet (name) {
    const greeting = (`Moikka ${name}`)
    console.log(greeting)
    return greeting
}

console.log(greet("Ulla"));

const nuoliFunktio = () => {
    console.log("Ollaan nuolifunktiossa")
}
nuoliFunktio()

const quadraticSum = (a, b) => (a + a + b + b);
console.log(quadraticSum(3,5))

const numerot = [12,23,34,4,6,7,889,4];
numerot.forEach((num, index) => {
    console.log(`Indeksi on ${index}, arvo on ${num}`)
})

console.log(numerot)