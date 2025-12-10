"use strict"

const trigger = document.getElementById("trigger");
const target = document.getElementById("target");

trigger.addEventListener("mouseenter", () =>{
    target.src = "img/picB.jpg";
})

trigger.addEventListener("mouseleave", () =>{
    target.src = "img/picA.jpg"
})