// New league searcher functions

async function displaySummoner() {
    document.getElementById('Summoner').innerHTML = 'Hello';
}




// Old movie searcher functions
/*
async function changeTitle() {
    document.getElementById("TitleText").setAttribute('value', data.Title);
    document.getElementById("YearText").setAttribute('value','2022');
}

function changePoster(posterLink) {

    var img = document.getElementById("poster");
    img.src = posterLink;

}

// Update the entire form (completed version)
async function showDetails(OMDBID) {
    //changePoster();
    loadMovie(OMDBID);

}

function changeRatings(rating) {
    const images = ["images/trophy.png"];

    document.querySelector('.trophy').innerHTML = "";

    // Floor rating
    for (let x = 0; x < Math.floor(rating); x++) {            
        element = '<img src="' + images + '">'
        document.querySelector('.trophy').innerHTML += element;
    }
}

async function loadMovie(ID) {

    if (ID != null) {

        var URL = 'https://omdbapi.com/?apikey=dc0d5578&i=' + ID;
        const res = await fetch(`${URL}`);
        const data = await res.json();
        if(data.Response == "True") console.log(data);
        console.log(data.Title);

        // Change the poster
        changePoster(data.Poster);
        // Update the data in the front end
        document.getElementById("TitleText").setAttribute('value', data.Title);
        document.getElementById("YearText").setAttribute('value', data.Year);
        document.getElementById("GenreText").setAttribute('value', data.Genre);
        document.getElementById("RuntimeText").setAttribute('value', data.Runtime);
        document.getElementById("DirectorText").setAttribute('value', data.Director);
        document.getElementById("WriterText").setAttribute('value', data.Writer);
        document.getElementById("ActorsText").innerHTML =  data.Actors;
        document.getElementById("PlotText").innerHTML =  data.Plot;

        changeRatings(data.imdbRating);

    }

    else {
        document.getElementById("TitleText").setAttribute('value', 'Error');
        document.getElementById("YearText").setAttribute('value', 'Error');
        document.getElementById("GenreText").setAttribute('value', 'Error');
        document.getElementById("RuntimeText").setAttribute('value', 'Error');
        document.getElementById("DirectorText").setAttribute('value', 'Error');
        document.getElementById("WriterText").setAttribute('value', 'Error');
    }
    
}
*/