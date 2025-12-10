"use strict"

const form = document.getElementById('search');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    const searchValue = document.getElementById('query').value.trim();

    resultsDiv.innerHTML = '';

    const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(searchValue)}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            console.log(`Search results for "${searchValue}":`, data);

            if (data.length === 0) {
                resultsDiv.textContent = 'No results found.';
                return;
            }
            data.forEach(item => {
                const tvShow = item.show;

                const article = document.createElement('article');

                const h2 = document.createElement('h2');
                h2.textContent = tvShow.name;
                article.appendChild(h2);

                if (tvShow.image?.medium) {
                    const img = document.createElement('img');
                    img.src = tvShow.image.medium;
                    img.alt = tvShow.name;
                    article.appendChild(img);
                }
                const summaryDiv = document.createElement('div');
                article.appendChild(summaryDiv);
                resultsDiv.appendChild(article);
            });
        })
});