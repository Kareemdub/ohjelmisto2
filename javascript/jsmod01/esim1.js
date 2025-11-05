'use strict';

//käytä const muuttujan esittelyyn, paitsi jos sen arvoa pitää muuttaa. silloi let

let teksti = "moi maailma!"

console.log("Helo")
console.log(teksti);

teksti = "moi matti"

alert("KUkkuu11121")




let name = "Matti";
let age = 23;
//const greeting = `Moi + ${name}, ${age+2} v!`; //`` sama kuin f stringi pythonissa
//age = prompt("Anna ikäsi:");
name = prompt("Anna nimesi:");
age = parseInt(prompt("Anna ikäsi:"));
if (age > 10) {
  //console.log("Käyttäjän syöte", userInput);
  const greeting = `Moi ${name}, ikäsi vuoden päästä${age+1} v!`
  document.querySelector('.output').textContent = teksti
} else {
  console.log("Olet liian nuori sivulle")
}

const result = Math.ceil(Math.random()*6);
console.log(result)

switch (result) {
  case 1:
    console.log("Tuli ykköne") //jos break niin toimii niinkuin if else
    break;
  case 2:
    console.log("kakkone")
  case 3 || 4:
    console.log("korlmone tai 4")
  case 5 || 6:
    console.log("loput")
}

//while, käytä kun et tiedä täysin monta kertaa toteutetaan
//dowhile aina on alkuehto, ei välttämättä toteuteta kertaakaan

let count = 0;

while (count < 5) {
    console.log("Laskuri", count)
    count++;
}
let number = 0;
do {            // dowhile halutaan suorittaa ainakin kerran ennen looppia
    console.log("tämä tulostuu ainakin kerran, vaikka ehto ei täyttyisi.")
    number++;
} while(number < 5);
   // number++;

//for i tilanteisiin jossa haluat toistaa luupin x määrän kertoja
//esim kun käydään taulukon indexin läpi

for (let i = 20; i >= 1 ; i--) {
    console.log("Luku on:", i)

}










