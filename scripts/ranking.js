base_url = "http://localhost:80/anime/review/ranking/";

//Get the title as a parameter of the hyperlink directed from other pages
metric = window.location.hash.substring(1);
//This function makes API call to get ranking results based on the metric
MakeAPICallToShowRanking(metric);



var info_data;
var counter = 0;
var search_t;
//This function makes API call to get ranking results based on the metric
function MakeAPICallToShowRanking(metric) {
    search_t = metric;
    var info_url = base_url + metric;
    var xhr = new XMLHttpRequest();
    //Make the get request
    xhr.open("GET", info_url, true);

    xhr.onload = function(e) {
        //Get the response
        var jsonResponse = xhr.responseText;
        //Do some parsing
        jsonResponse.replace((/([\w]+)(:)/g), "\"$1\"$2");

        jsonResponse = jsonResponse.replace(/NaN/g, '0');
        jsonResponse = jsonResponse.replace(/</g, '<');
        jsonResponse = JSON.parse(jsonResponse);

        info_data = jsonResponse["data"];
        var result_title = document.getElementById("result_title");
        //If we get any result from the ranking, show the result part; else, set the result part to be hidden
        if (Object.keys(info_data).length > 0) {
            counter = 1;
            //Update the results on the page
            updateResultPage("next");
            result_title.innerHTML = "Anime Ranking by " + metric + " <br> Showing results: " + (counter - 1).toString() + " / " + Object.keys(info_data).length.toString();





        } else {
            result_title.innerHTML = "No Results Found for: " + search_term;
            document.getElementById("result_animes").style.visibility = "hidden";
            var pagination = document.getElementById("result_pagination");
            pagination.style.visibility = "hidden";
        }







    }

    xhr.onerror = function(e) {
        console.error(xhr.statusText);

    }

    xhr.send(null);


}

//Update a single anime with its title and its ranking
function updateResultAnimeInfo(data, index) {
    var title = data["title"];

    var new_media_str = "<li class='list-group-item text-left'>" +
        "<b>" + index + " </b>" +
        "<a href=" + "'./info.html" + "#" + title.toString() + "'>" + title + "</a> </li>";
    console.log(new_media_str);
    var result_media_list = document.getElementById("result_animes");
    result_media_list.innerHTML += new_media_str;

}

//This function is triggered when previous button is clicked
function previous_result() {
    if (counter > 11 && Object.keys(info_data).length > 0) {
        try {
            updateResultPage("previous");
            result_title.innerHTML = "Anime Ranking by " + search_t + " <br> Showing results: " + (counter - 1).toString() + " / " + Object.keys(info_data).length.toString();
        } catch (e) {
            console.log("Error when showing previous result:" + e.toString());
        }
    }
}
//This function is triggered when next button is clicked
function next_result() {
    if (counter >= 11 && Object.keys(info_data).length > 0 && counter <= Object.keys(info_data).length) {
        try {
            updateResultPage("next");
            result_title.innerHTML = "Anime Ranking by " + search_t + " <br> Showing results: " + (counter - 1).toString() + " / " + Object.keys(info_data).length.toString();
        } catch (e) {
            console.log("Error when showing previous result:" + e.toString());
        }
    }
}

//Update the whole page
function updateResultPage(direction) {
    var result_animes = document.getElementById("result_animes");
    result_animes.style.visibility = "visible";
    var medias = result_animes.getElementsByClassName("list-group-item text-left");
    var len = medias.length;
    if (len != 0) {
        while (medias.length > 0) {
            var removed_media = medias[0];
            removed_media.remove();
        }
    }

    var i = 1;
    if (direction == "previous") {
        if ((counter % 10) == 1) {
            counter -= 20;
        } else {
            counter -= (10 + (counter - 1) % 10);
        }

    }
    //Update at most 10 results on the page
    while (i <= 10 && counter >= 0 && counter <= Object.keys(info_data).length) {
        var index = Object.keys(info_data)[counter - 1];
        //Update each of the 10 results
        updateResultAnimeInfo(info_data[index.toString()], counter);
        counter += 1;


        i += 1;
    }

    var pagination = document.getElementById("result_pagination");
    pagination.style.visibility = "visible";

}