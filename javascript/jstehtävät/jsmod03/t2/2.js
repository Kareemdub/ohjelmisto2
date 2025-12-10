"use strict"

const target = document.getElementById("target");
const list = ["First item", "Second item", "Third item"];

list.forEach((text, index) => {
    const li = document.createElement("li");
    li.textContent = text;
    if (index === 1) li.classList.add("my-item");

    target.appendChild(li);
});