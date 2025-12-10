"use strict"

const output = document.getElementById('jsonOutput');
const apiUrl = "https://api.tvmaze.com/search/shows?q=query";

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        output.textContent = JSON.stringify(data);
        console.log(data);
    });
