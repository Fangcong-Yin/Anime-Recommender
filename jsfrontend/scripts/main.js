console.log('page load - entered main.js for web service');

base_url = "http://localhost:80/anime/";

//This function will load as index.html loads
function onLoad() {
    //Load top 3 popular animes on the page
    MakeAPICallToPopularAnimeInfo();
    //Load the ranking by members
    MakeAPICallToRanking('members');
    //Load the ranking by ranking
    MakeAPICallToRanking('ranked');
    //Load the ranking by score
    MakeAPICallToRanking('score');
}

//Load top 3 popular animes on the page
function MakeAPICallToPopularAnimeInfo() {

    var url = base_url + "info/title/";
    //The names of the top 3 popular animes
    var most_popular = ["Death Note", "Shingeki no Kyojin", "Sword Art Online"]
    var i = 0;
    most_popular.forEach((element) => {
        //For each of the 3 animes, make an API call to get its information 
        var xhr = new XMLHttpRequest();
        var anime_url = url + element
        xhr.open("GET", anime_url, true);
        var jsonResponse;

        xhr.onload = function(e) {
            jsonResponse = JSON.parse(xhr.responseText);
            console.log(jsonResponse["result"]);

            var data = jsonResponse["data"];
            console.log(data);

            i += 1;
            //After getting the response, update the UI by calling this function
            updateMostPopularAnimes(i, data);
        }

        xhr.onerror = function(e) {
            console.error(xhr.statusText);
        }

        xhr.send(null);
    });


}

//Update the UI to show the information of the top 3 popular animes
function updateMostPopularAnimes(index, data) {
    console.log(index);

    for (var k in data) data = data[k];
    //Get the information of the anime to display on the UI
    var title = data["title"];
    var uid = data["uid"];
    var syn = data["synopsis"];
    var img = data["img_url"];
    //Update the texual information
    var media_title = document.getElementById("title_popular_anime" + "_" + index);
    media_title.innerHTML = title;
    media_title.href = "./info.html" + "#" + title;
    var media_syn = document.getElementById("syn_popular_anime" + "_" + index);
    media_syn.innerHTML = syn;
    //Update the image
    var media_img = document.getElementById("img_popular_anime" + "_" + index);
    media_img.src = img;
    media_img.href = "./info.html" + "#" + title;
    var media_img_url = document.getElementById("img_url_popular_anime" + "_" + index);
    media_img_url.href = "./info.html" + "#" + title;;

}

//This function gets the top 3 animes for 3 metrics
function MakeAPICallToRanking(metric) {

    var url = base_url + "review/ranking/" + metric;
    var xhr = new XMLHttpRequest();
    var anime_url = url
        //Make the get request
    xhr.open("GET", anime_url, true);
    var jsonResponse;

    xhr.onload = function(e) {
        jsonResponse = xhr.responseText.toString();
        //Do some parsing for the response
        jsonResponse.replace((/([\w]+)(:)/g), "\"$1\"$2");

        jsonResponse = jsonResponse.replace(/NaN/g, '0');
        //Convert the response to a json object
        jsonResponse = JSON.parse(jsonResponse);

        var data = jsonResponse["data"];
        //Update the UI in this function
        updateRankingAnimes(data, metric);

    }

    xhr.onerror = function(e) {
        console.error(xhr.statusText);
    }

    xhr.send(null);

}

//Update the ranking information 
function updateRankingAnimes(data, metric) {
    var i = 0;
    for (var k in data) {
        i += 1;
        //Update the top 3 animes for each ranking metric
        if (i > 3) break;
        var anime = data[k];
        console.log(data);
        var title = anime["title"];
        var anime_title = document.getElementById(metric + "_top_" + i);
        anime_title.innerHTML = title;
        anime_title.href = "./info.html" + "#" + title;
    }
}