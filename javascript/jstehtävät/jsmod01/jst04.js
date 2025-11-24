"use strict"

name = prompt("Give me your name!")
const num = Math.ceil(Math.random()*4);
console.log(name)
console.log(num)
/*
const hufflePuff = 1
const ravenClaw = 2
const slitherin = 3
const gryffindor = 4
*/
if (num === 1) {
    document.querySelector("#selector").innerHTML = name + " you are Hufflepuff!"
}
if (num === 2) {
    document.querySelector("#selector").innerHTML = name + " you are Ravenclaw!"
}
if (num === 3) {
    document.querySelector("#selector").innerHTML = name + " you are Slitherin!"
}
if (num === 4) {
    document.querySelector("#selector").innerHTML = name + " you are Gryffindor!"
}

/*switch (name) {
    case 1:
        console.log("Tuli ykköne") //jos break niin toimii niinkuin if else
        break;
    case 2:
        console.log("kakkone")
        break
    case 3:
        console.log("korlmone tai 4")
        break
    case 4:
        console.log("loput")
        break
}*/