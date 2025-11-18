"use strict";

// viittaus id
const OutputElement1 =
    document.getElementsByClassName("output");

console.log(OutputElement1)
// viittaus
const OutputElement2 =
    document.getElementById("output");

console.log(OutputElement2)

const outputElement3 = document.querySelectorAll("p")
console.log(outputElement3)

const body = document.querySelector("body");
body.querySelector("#output");

console.log(body.querySelector("#output"));

const ulElement = (document.querySelector("ul"));
const newLi = document.createElement("li");
ulElement.appendChild(newLi);
newLi.textContent = "4"

//toimii myös innerHTML
// ulElement.innerHTML = "<li>uusi itemi</li><li>toinen lista </li>";

// haetaan viittaus kaikkiin li-elementteihin listan sisällä
const liElems = ulElement.querySelectorAll("li");
for (let i=0; i<liElems.length; i++) {
    liElems[i].textContent = `${i+1}, itemi`;

}

//lisätään sisältö js taulukosta
const inventory = ["kynä", "kumi", "läppäri", "penaali"]
const inventoryOLElem = document.createElement("ol");
for (const item of inventory) {
    const liElem = document.createElement("li")
    liElem.textContent = item
    inventoryOLElem.appendChild(liElem)
}

// lisätään luoto lista DOMiin käyttäen aiemmin hauttua yläviittausta
const inventoryHeader = document.createElement("h2")
inventoryHeader.textContent = "Inventaario";
body.appendChild(inventoryHeader)
body.appendChild(inventoryOLElem);
inventoryHeader.classList.add("red")


//sidotaan tapahtuma ja tapahtumakäsittelijä yhteen
const button = document.querySelector("button")
//erillinen tapahtumankäsittelyfunktio

function buttonClick() {
    console.log("Nappulaa klikattu")
}
button.addEventListener("click", buttonClick)


inventoryHeader.addEventListener("click", function () {
    console.log("otsikko klikattua");
    inventoryHeader.classList.toggle("red");
})

let inputString = "";
document.addEventListener("keypress", function () {
    console.log("näpäin painetu")
    inputString += event.key;
    if (event.key === "Enter") {
        outputElement3.classList.remove("blue");
        outputElement3.classList.add("red");
    }
    outputElement3.classList.add("blue")
    outputElement3.textContent = "nappia painettu:" + event.key;
});

document.addEventListener("mousemove", function () {
    //console.log("hiiri liikkuu", event);
    outputElement3[0].textContent = `Hiiren sijainti: ${event.clientX}, ${event.clientY}`
})

document.querySelector("a",).addEventListener("click", function(event) {
    event.preventDefault();
    console.log("klikattu, mutta sivu ei päivity")
})



//lomakkeen käsittely
const addForm = document.querySelector("form")
const inputText = addForm.querySelector("input")
addForm.addEventListener("submit", function (event) {
    event.preventDefault();
    if (inputText.value.length < 2) {
        return;
    }
    const liElem = document.createElement("li")
    liElem.textContent = inputText.value;
    //lisätään myös js taulukkoon, ei kuitenkaan hyödyllinen tässä
    inventory.push(inputText.value);
    console.log("muistissa oleva inventaario", inventory)
    inventoryOLElem.appendChild(liElem)
    inputText.value = "";


})