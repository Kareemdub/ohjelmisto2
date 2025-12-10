"use strict"


const dogs = []
for (let i = 0; i < 6; i++){

    let dog = prompt(`Give the name of dog ${i + 1}`)
    dogs.push(dog)
    console.log(dogs[i])
    dogs.sort()
    dogs.reverse()

}

let list = document.querySelector("#dogs")

for (let i = 0; i < dogs.length; i++) {
    let li = document.createElement("li")
    li.innerText = dogs[i]
    list.appendChild(li)
    console.log(dogs[i])
}