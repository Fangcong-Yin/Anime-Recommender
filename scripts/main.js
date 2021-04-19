console.log('page load - entered main.js for js-other api');

var submitButton = document.getElementById('bsr-submit-button');
submitButton.onmouseup = getFormInfo;

function getFormInfo() {
    console.log('entered get form info');
    var name = document.getElementById("name-text").value;
    makeNetworkCallToAgeApi(name);
} // end of getFormInfo

function makeNetworkCallToAgeApi(name) {
    console.log('entered makeNetworkCallToHPApi');
    var url = "http://localhost:51040/hp/" + name;
    var xhr = new XMLHttpRequest(); // 1. creating req
    xhr.open("GET", url, true); // 2. configure request attributes

    // set up onload - triggered when nw response is received
    // must be defined before making the network call
    xhr.onload = function(e) {
            console.log('network response received' + xhr.responseText);
            // do something
            updateHPWithResponse(name, xhr.responseText);
        } // end of onload

    // set up onerror - triggered if nw response is error response
    xhr.onerror = function(e) {
            console.error(xhr.statusText);
        } // end of onerror

    xhr.send(null); // actually send req with no message body
} // end of makeNetworkCallToAgeApi

function updateHPWithResponse(name, response_text) {
    // extract json info from response
    var response_json = JSON.parse(response_text);
    // update label with it
    var label1 = document.getElementById('response-line1');

    if (response_json['result'] != 'success') {
        label1.innerHTML = 'Apologies, we could not find the character you want to search for .';
    } else {
        response_json = response_json['character']
        label1.innerHTML = 'Information of ' + name + ':' + '<br>';
        label1.innerHTML += 'Species: ' + response_json['species'] + '<br>';
        label1.innerHTML += 'Gender: ' + response_json['gender'] + '<br>';
        label1.innerHTML += 'House: ' + response_json['house'] + '<br>';
        label1.innerHTML += 'Actor/Actress: ' + response_json['actor'] + '<br>';
        // make nw call to number api
        makeNetworkCallToWikiApi(response_json['actor']);
    }

} // end of updateAgeWithResponse

function makeNetworkCallToWikiApi(name) {
    console.log('enetered makeNetworkCallToNumbersApi');
    var url = "https://en.wikipedia.org/w/api.php?action=parse&&origin=*&section=0&format=json&prop=text&page=" + name;
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, true);

    xhr.onload = function(e) {
        console.log('got wiki response from wikipediaapi');
        updateWikiWithResponse(name, xhr.responseText);
    }

    xhr.onerror = function(e) {
        console.error(xhr.statusText);
    }

    xhr.send(null); // send request without bosy
} // end of makeNetworkCallToNumbersApi

function updateWikiWithResponse(name, response_text) {
    var label2 = document.getElementById("response-line2");
    var response_json = JSON.parse(response_text);
    if (document.getElementById("dynamic-label") == null) {
        label_item = document.createElement("label"); // weird - "label" is a class name
        label_item.setAttribute("id", "dynamic-label");
        var response_div = document.getElementById("response-div");
        response_div.appendChild(label_item);
    }
    if (response_json['parse']['text']['*'] == null) {
        label1.innerHTML = 'Apologies, we could not find the actor associated with this character you want to search for .';
        label_item.innerHTML = "<div></div>";
        label2.innerHTML = "";
    } else {
        label2.innerHTML = "Information for " + name + " from wikipedia is given below. <br>";
        label_item.innerHTML = response_json['parse']['text']['*'];
        //Remove all images for simplicity
        //The console might show file not found error, but it is fine because we do not want to use image files on the site
        var images = document.getElementsByTagName('img');
        var l = images.length;
        for (var i = 0; i < l; i++) {
            images[0].parentNode.removeChild(images[0]);
        }
    }


    // dynamically adding a label
    // setAttribute(property_name, value) so here id is property name of button object




    // option 1: directly add to document
    // adding label to document
    //document.body.appendChild(label_item);

    // option 2:
    // adding label as sibling to paragraphs


} // end of updateTriviaWithResponse
