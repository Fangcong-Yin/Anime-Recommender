base_url = "http://localhost:80/anime/";

//Configure the form submit button
var submitButton = document.getElementById('bsr-submit-button');
submitButton.onmouseup = search;


function search() {
    //Start searching
    console.log('I am searching for something!');
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
function MakeAPICallToFilterAnimeInfo(search_term, filter) {

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
        console.log(jsonResponse["result"]);

        var info_data = jsonResponse["data"];
        var result_title = document.getElementById("result_title");
        //If we get any result, show the result part; else, set the result part to be hidden
        if (Object.keys(info_data).length > 0) {
            document.getElementById('result_animes').style.visibility = 'show';
            result_title.innerHTML = "Results for:" + search_term;
            var temp = 1;
            for (var index in info_data) {
                if (temp > 3) break;
                //Update the top 3 results from search results in this function
                updateResultAnimeInfo(info_data[index], temp);
                temp += 1;
            }



        } else {
            result_title.innerHTML = "No Results Found for !" + search_term;
            document.getElementById('result_animes').style.visibility = 'hidden';
        }







    }

    xhr.onerror = function(e) {
        console.error(xhr.statusText);

    }

    xhr.send(null);


}

//This function updates the UI based on the search result
function updateResultAnimeInfo(data, index) {
    var title = data["title"];
    var uid = data["uid"];
    var syn = data["synopsis"];
    var img = data["img_url"];
    var media_title = document.getElementById("title_popular_anime" + "_" + index);
    media_title.innerHTML = title;
    media_title.href = "./info.html" + "#" + title;
    var media_syn = document.getElementById("syn_popular_anime" + "_" + index);
    media_syn.innerHTML = syn;
    var media_img = document.getElementById("img_popular_anime" + "_" + index);
    media_img.src = img;
    media_img.href = "./info.html" + "#" + title;
    var media_img_url = document.getElementById("img_url_popular_anime" + "_" + index);
    media_img_url.href = "./info.html" + "#" + title;;

}