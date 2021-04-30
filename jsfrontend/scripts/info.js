console.log('enter a single anime info page');

base_url = "http://localhost:80/anime/";

//Get the title as a parameter of the hyperlink directed from other pages
title = window.location.hash.substring(1);

//This function makes API call to get info of a single anime
function MakeAPICallToASingleAnimeInfo() {

    var info_url = base_url + "info/title/" + title;
    var xhr = new XMLHttpRequest();
    //Make the get request
    xhr.open("GET", info_url, true);

    xhr.onload = function(e) {
        //Do some parsing and convert it to a json object
        var jsonResponse = JSON.parse(xhr.responseText);
        console.log(jsonResponse["result"]);

        var info_data = jsonResponse["data"];
        for (var k in info_data) info_data = info_data[k];
        console.log(info_data);
        //Then, get the reviews of this anime by making another API call
        MakeAPICallToASingleAnimeReview(info_data);


    }
    xhr.onerror = function(e) {
        console.error(xhr.statusText);
    }

    xhr.send(null);


}

//This function gets the reviews of this anime by making another API call
function MakeAPICallToASingleAnimeReview(info_data) {
    var uid = info_data["uid"];
    var review_url = base_url + "review/" + uid;
    var xhr = new XMLHttpRequest();
    //Make the get request
    xhr.open("GET", review_url, true);

    xhr.onload = function(e) {

        var jsonResponse = JSON.parse(xhr.responseText);
        console.log(jsonResponse["result"]);

        var review_data = jsonResponse["data"];
        for (var k in review_data) review_data = review_data[k];
        console.log(review_data);
        //Update the UI based on the responses
        updateSingleAnimeInfo(info_data, review_data);


    }


    xhr.onerror = function(e) {
        console.error(xhr.statusText);
    }

    xhr.send(null);


}

//This function updates the UI based on the API responses
function updateSingleAnimeInfo(info_data, review_data) {

    var title = info_data["title"];
    var media_title = document.getElementById("title_this_anime");
    media_title.innerHTML = title;

    var syn = info_data["synopsis"];
    var media_syn = document.getElementById("syn_this_anime");
    media_syn.innerHTML = syn;
    var img = info_data["img_url"];
    var media_img = document.getElementById("img_this_anime");
    media_img.src = img;
    var year = info_data["aired"];
    var media_year = document.getElementById("year_this_anime");
    media_year.innerHTML = "<b> Aired: </b> " + year;
    var episodes = info_data["episodes"];
    var media_episodes = document.getElementById("episodes_this_anime");
    media_episodes.innerHTML = "<b> Number of Episodes: </b> " + parseInt(episodes);
    //Format the list of genres better
    var genre = info_data["genre"];
    genre = genre.replace(/\'/g, '\"');
    console.log(genre);
    genre = JSON.parse(genre);
    genre = genre.join();
    var media_genre = document.getElementById("genre_this_anime");
    media_genre.innerHTML = "<b> Genres: </b> " + genre;

    var members = review_data["members"];
    var media_members = document.getElementById("members_this_anime");
    media_members.innerHTML = "<b> Number of People Watched: </b> " + parseInt(members);
    var popularity = review_data["popularity"];
    var media_popularity = document.getElementById("popularity_this_anime");
    media_popularity.innerHTML = "<b> Popularity: </b> " + parseInt(popularity);
    var ranked = review_data["ranked"];
    var media_ranked = document.getElementById("ranked_this_anime");
    media_ranked.innerHTML = "<b> Ranking: </b> " + parseInt(ranked);
    var score = review_data["score"];
    var media_score = document.getElementById("score_this_anime");
    media_score.innerHTML = "<b> Rating: </b> " + score;
}