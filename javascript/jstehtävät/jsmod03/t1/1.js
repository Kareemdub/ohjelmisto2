"use strict"

document.getElementById("target").innerHTML += `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
`;

let element = document.getElementById("target")
element.classList.add("my-list")


