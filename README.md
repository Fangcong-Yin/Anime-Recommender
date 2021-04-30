# AnimeRecommender

## OO_API

### API Usage

In general, this api can be used to access the fatucal information about animes or the review data about animes. These pieces of data should be applied to anime recommendation client programs in the future. Please refer to Json Specification section for details.

### JSON Specification
The api endpoints of this project are summarized in the following table.

**Request Type**|**Resource endpoint**|**Body**|**Expected response**|**Inner working of handler**
:-----:|:-----:|:-----:|:-----:|:-----:
GET|/anime/info/title/:title|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}}}|Information about all the animes whose titles match the given anime title
GET|/anime/info/keyword/:keyword|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}}}|Information about all the animes whose titles or synopsisis match the given keyword
GET|/anime/info/genre/:genre|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}}}|Information about all the animes whose genres match the given genre
GET|/anime/info/year/:year|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}}}|Information about all the animes whose aired time match the given year
GET|/anime/info/length/:length|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}}}|Information about all the animes whose number of episodes match the given length
GET|/anime/info/|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}}}|Information about all the animes in the database.
GET|/anime/review/|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “members”:12345, “popularity”:789, “ranked”:1}}}|Evaluation of all the animes in the database.
GET|/anime/review/:uid|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “members”:12345, “popularity”:789, “ranked”:1,“score”:8.1}}}|Evaluation of the anime given the uid
GET|/anime/review/ranking/:metric|None|{“result”: “success”, “data”:{'0':{“uid”:“1”, “title”:“anime”, “members”:12345, “popularity”:789, “ranked”:1,“score”:8.1}}}|Return the list of animes ranked by a given metric 
PUT|/anime/review/:uid|{“score”: 100}|{“result”: “success”}|Update the evaluation of the given anime based on the score in the body
POST|/anime/info/:title|{“title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}|{“result”:”success”}|Add a new anime to the end of the list
DELETE|/anime/info/:uid|None|{“result”: “success”}|Delete the anime with the given uid



### Tests
All the data, server script, and server-related libraries are included in /OO-API/ folder.    

Before running the server, please have these python modules installed: `routes` `cherrypy` `pandas`  

To start the server, use the following command: `python anime_server.py` or `python3 anime_server.py`  

To test the database library, use the following command `python test_anime_database.py` or `python3 test_anime_database.py`   

To test the API, use the following command `python test_api.py` or `python3 test_api.py` after starting the server.  

## JS Front End - User Interaction

### Description
This is a web front end where the user can glance popular animes and search for animes.  

On the main page, the most popular 3 animes are displayed together with their covers, titles, and synopsises. Click on the title of the anime or the cover, the user will be directed to the info page of that specific anime.  

The anime ranking is also listed on the main page. The top 3 animes will be displayed ranked by viewed members, rating score, and overall ranking. Click on the title of the anime on the list and the user will be directed to the info page of that specific anime.  

On the info page of a specific anime, the title, cover image, genre, aired time, number of episodes, number of people watched, popularity ranking, overall ranking, rating, and synopsis of this anime will be displayed.  

The user can also search for an anime by clicking either the search button on the jumbotron or the tab on the upper right corner. The user can choose one out of 5 filters when searching: title will give an exact match of an anime title; genre will show animes of a given genre; keyword will search for a given word in anime titles and synopsises; year will give an exact match of the aired year; length will give an exact match of the number of episodes. The top 3 results of all results will be displayed and the user can click on the result title or cover image to be directed to the info page of that anime.  

### Deploy

All codes for the JS front end are included under `/jsfrontend` folder.  

To run the front end, first start the server locally by using the following command: `python anime_server.py` or `python3 anime_server.py`  

Then, navigate to "https://fangcong-yin.github.io/AnimeRecommender/index.html" (the gitlab page does not update for some unknown reasons) and enjoy!  

### Test

To test all the user interaction of the js front end, please do the following step:  

1. On the main page, check if there is anything not rendering.  
2. Click on the cover image or title of an anime under popular animes and check if the website directs to its info page.  
3. Click on the Home button at the upper right corner and check if the websites goes back to the home page.  
4. On the main page, click on the title of an anime under anime ranking and check if the website directs to its info page.  
5. On the info page, check if there is anything not rendering.  
6. Click on the search button on the jumbotron and check if it directs to the search page.  
7. Choose any of the search filter, enter some texts, and click submit. Check if there is anything not rendering.  

