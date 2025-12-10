'use strict';

const form = document.getElementById('searchForm');

form.addEventListener('submit', function (event) {
    event.preventDefault(); // prevent default form submission

    // Get the input value
    const searchValue = document.getElementById('query').value.trim();


    // Construct the API URL
    const apiUrl = `https://api.tvmaze.com/search/shows?q=${searchValue}`;

    // Fetch data from TVMaze
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            let response;
            console.log(response.json ,data);
        });
});