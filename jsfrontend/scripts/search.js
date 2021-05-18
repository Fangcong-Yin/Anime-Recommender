base_url = "http://localhost:80/anime/";

//Configure the form submit button
var submitButton = document.getElementById('bsr-submit-button');
submitButton.onmouseup = search;


function search() {
    //Start searching
    var search_term = document.getElementById('search_term').value;
    var filter;
    //Choose a filter according to the selection of the user
    if (document.getElementById('title_filter').selected) {
        filter = 'title';

    } else if (document.getElementById('genre_filter').selected) {
        filter = 'genre';
    } else if (document.getElementById('keyword_filter').selected) {
        filter = 'keyword';
    } else if (document.getElementById('year_filter').selected) {
        filter = 'year';
    } else if (document.getElementById('length_filter').selected) {
        filter = 'length';
    }
    //Use this function to get the search results
    MakeAPICallToFilterAnimeInfo(search_term, filter);
}
//This function makes API call to get search results based on the filter

//This variable stores all the data from the filtered response
var info_data;
//This variable records the current location for pagination
var counter = 0;
//This variable stores the name of the filter 
var search_t;

//Make an API call to get the filtered anime info
function MakeAPICallToFilterAnimeInfo(search_term, filter) {
    search_t = search_term;
    var info_url = base_url + "info/" + filter + "/" + search_term;
    var xhr = new XMLHttpRequest();
    //Make the get request
    xhr.open("GET", info_url, true);

    xhr.onload = function(e) {
        //Get the response
        var jsonResponse = xhr.responseText;
        //Do some parsing
        jsonResponse.replace((/([\w]+)(:)/g), "\"$1\"$2");

        jsonResponse = jsonResponse.replace(/NaN/g, '0');
        jsonResponse = JSON.parse(jsonResponse);

        info_data = jsonResponse["data"];
        var result_title = document.getElementById("result_title");
        //If we get any result, show the result part; else, set the result part to be hidden
        if (Object.keys(info_data).length > 0) {
            counter = 1;
            //update at most 10 results in one page
            updateResultPage("next");
            result_title.innerHTML = "Results for:" + search_term + " <br> Showing results: " + (counter - 1).toString() + " / " + Object.keys(info_data).length.toString();





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

//Update one result anime on the page
function updateResultAnimeInfo(data, index) {
    try {
        var title = data["title"];
        var uid = data["uid"];
        var syn = data["synopsis"];
        var img = data["img_url"];
        var new_media_str = "<div class='media'>" +
            "<div class='media-left'>" +
            "<a href=" + "'./info.html" + "#" + title + "' target='_self' ><img src=" + img + " href=" + "'./info.html" + "#" + title + "'  ></a>" +
            "</div>" +
            "<div class='media-body'>" +
            "<h5 class='media-heading'>" +
            "<a href=" + "'./info.html" + "#" + title + "' target='_self'>" + title + "</a>" +
            "</h5>" +
            "<p>" + syn + "</p>" +
            "</div>" +
            "</div>";
        var result_media_list = document.getElementById("result_animes");
        result_media_list.innerHTML += new_media_str;
    } catch (e) {
        console.log("Error when loading resources: " + e.toString());
    }


}

//This function is triggered when previous button is clicked and it will show the previous 10 results on the page
function previous_result() {
    if (counter > 11 && Object.keys(info_data).length > 0) {
        try {
            updateResultPage("previous");
            result_title.innerHTML = "Results for:" + search_t + " <br> Showing results: " + (counter - 1).toString() + " / " + Object.keys(info_data).length.toString();
        } catch (e) {
            console.log("Error when showing previous result:" + e.toString());
        }
    }
}
//This function is triggered when next button is clicked and it will show the next 10 results on the page
function next_result() {
    if (counter >= 11 && Object.keys(info_data).length > 0 && counter <= Object.keys(info_data).length) {
        try {
            updateResultPage("next");
            result_title.innerHTML = "Results for:" + search_t + " <br> Showing results: " + (counter - 1).toString() + " / " + Object.keys(info_data).length.toString();
        } catch (e) {
            console.log("Error when showing previous result:" + e.toString());
        }
    }
}

//Update the whole result page after getting response from the server
function updateResultPage(direction) {
    var result_animes = document.getElementById("result_animes");
    result_animes.style.visibility = "visible";
    var medias = result_animes.getElementsByClassName("media");
    var len = medias.length;
    //Clear the previous results on the page
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
    //Update up to 10 animes on the page 
    while (i <= 10 && counter >= 0 && counter <= Object.keys(info_data).length) {
        var index = Object.keys(info_data)[counter - 1];
        //Update each of the animes on the page
        updateResultAnimeInfo(info_data[index.toString()], counter);
        counter += 1;


        i += 1;
    }

    var pagination = document.getElementById("result_pagination");
    pagination.style.visibility = "visible";


}