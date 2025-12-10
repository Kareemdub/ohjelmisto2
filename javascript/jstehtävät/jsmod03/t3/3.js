'use strict';
document.getElementById("target")
const names = ['John', 'Paul', 'Jones'];


names.forEach((text, index) => {
    const li = document.createElement("li");
    li.textContent = text;
    if (index === 1) li.classList.add("my-item");

    target.appendChild(li);
});