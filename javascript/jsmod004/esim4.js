    'use strict';
    console.log('the script starts');

    function synchronousFunction() {
      let number = 1;
      for(let i = 1; i < 100000; i++){
        number += i;
        console.log('synchronousFunction running');
      }
      console.log('regular function complete', number);
    }

    async function asynchronousFunction() {                 // asynchronous function is defined by the async keyword
        console.log('asynchronous download begins');
        try {                                               // error handling: try/catch/finally
            const response = await fetch('https://api.chucknorris.io/jokes/random');    // starting data download, fetch returns a promise which contains an object of type 'response'
            const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
            console.log(jsonData.values);    // log the result to the console
           // document.querySelector(".output").textContent.
        } catch (error) {
            console.log(error.message);
        } finally {                                         // finally = this is executed anyway, whether the execution was successful or not
            console.log('asynchronous load complete');
        }
    }

    //synchronousFunction();
    //asynchronousFunction();

    console.log('the script ends');

//pics.json latausesimerkki

//const pics =


async function fetchPics(){
    const picsDiv = document.querySelector("#pics");

    try {
        const response = await fetch("pics.json")
        //console.log("response status", response.status, response.statusText, response.ok)
        if (!response.ok){
            throw new Error("response status not ok")
        }
        const pics = await response.json();
        console.log("pics", pics)
        for (const pic of pics) {
            const imgElem = document.createElement("img");
            imgElem.src = pic.address
            imgElem.alt = pic.description
            picsDiv.append(imgElem);
        }
    } catch (error) {
        //console.error()
        picsDiv.innerHTML = "<p>Kuvien lataamisessa ongelma</p>"
    }
}
document.querySelector("button").addEventListener("click", function(){
    fetchPics();

});

    //tv maze esimerkki

//datan haku, asynkroninen funkito
async function searchTVMaze (searchString){
    const response = await fetch("https://api.tvmaze.com/search/showsq=" + searchString);
    const results = await response.json();
    console.log("tv maze results", results)
    //tulokset voisi lisätä DOMiin tässä
    return results;
}



//hakulomakkeen käsittely
const searchForm = document.querySelector("form#tvmaze")
const inputText = searchForm.querySelector("input")
searchForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    if (inputText.value.length > 1 ) {
        searchTVMaze(inputText.value);
        const tvMazeResults = await searchTVMaze(inputText.value);
        // haun tulokset
        console.log("event handler hakutulokset", tvMazeResults)
        //tulokset voisi lisätä DOMiin myös tässä
    }
});


