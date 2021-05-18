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

//Load info of all animes and randomly select 3 animes from them
function MakeAPICallToPopularAnimeInfo() {
    //Make an api call to get the info of all animes
    var url = base_url + "info/";
    var i = 0;

    var xhr = new XMLHttpRequest();
    var anime_url = url;
    xhr.open("GET", anime_url, true);
    var jsonResponse;

    xhr.onload = function(e) {
        jsonResponse = JSON.parse(xhr.responseText);
        console.log(jsonResponse["result"]);

        var data = jsonResponse["data"];
        var data_length = Object.keys(data).length;
        var keys = Object.keys(data);
        var pre_index = 0;
        var i = 1;
        while (i <= 3) {
            //Randomly select 3 animes from all
            var index = parseInt(Math.random() * data_length);

            if (index == pre_index) {
                continue;
            } else {
                try {
                    index = keys[index];
                    //Update each of the 3 animes
                    updateMostPopularAnimes(i, data[index.toString()]);
                    i += 1
                } catch (e) {
                    console.log("Error updating popular animes" + e.toString());
                    continue;
                }

            }
        }

    }

    xhr.onerror = function(e) {
        console.error(xhr.statusText);
    }

    xhr.send(null);;


}

//Update the UI to show the information of the top 3 popular animes
function updateMostPopularAnimes(index, data) {
    console.log(index);

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