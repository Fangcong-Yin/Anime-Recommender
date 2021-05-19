# AnimeRecommender

This is the final project for SP21 University of Notre Dame CSE 30332 Programming Paradigms by Fangcong Yin. The project aims at building an anime recommender that can display information of animes and recommend animes based on the similarity of anime data.  

The project consists of a OO_API library that provides supporting functions for the API in `/OO_API` folder, an API web service that sets up the API in `/server` folder, and a JS front end in `/jsfrontend` folder.  

## DEMO

Video Demo:  https://drive.google.com/file/d/14x-0JB-reFwGhMmTFHw7J4WPalnzkCM-/view?usp=sharing

Code Walkthrough:  https://drive.google.com/file/d/1bxRHGJBqrCymgcS8NZBXple0Ii5w_NOK/view?usp=sharing

Demo website (please run the server on localhost before opening the website): https://fangcong-yin.github.io/AnimeRecommender/index.html  

Presentation slides:  https://docs.google.com/presentation/d/1wGSln6kI-ipKy__FZt4qnqiLOhQJ79JJAQZimLSBiE8/edit?usp=sharing

## OO_API

### API Usage

In general, this api can be used to access the fatucal information about animes or the review data about animes. This api also supports endpoints that can add information of animes that are not in the dataset and add review score for existing animes. In addition, the api also has an endpoint that can generate anime recommendations for a given anime using k nearest neighbor algorithm.These pieces of data are used by the jsfrontend application "anime recommender" to display information of animes and generating anime recommendations. Any client programs or people interested in exploring information of animes can utilize this api.     
     
Please refer to JSon Specification section for details.

### OO_API Library  

The API is supported by a OO_API library under `/OO_API` folder. The library preprocesses the raw data from `animes.csv`, stores them in pandas dataframes, and provides wrapper functions to get specific attributes of animes from the dataset.  

This API web service can be used to retrieve factual and review data of animes in the dataset. It can also be used to generate anime recommendations for a liked anime. The client can add new animes to the dataset as well.  
  
Please refer to `/OO_API/anime_databse.py` for details.  

### JSON Specification  

The API should be run on the localhost with port = 80.  The controller of the api is `/server/anime_controller.py` and the service of the api is `server/anime_server.py`.  

To start the server, use the following command: `python anime_server.py` or `python3 anime_server.py`    

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
GET|/anime/rec/:anime_uid|None|{“result”: “success”, “data”:["rec_title1","rec_title2",...]}|Return the list of recommended animes similar to the given anime   
PUT|/anime/review/:uid|{“score”: 100}|{“result”: “success”}|Update the evaluation of the given anime based on the score in the body
POST|/anime/info/:title|{“title”:“anime”, “synopsis”:“some synopsis”, “genre”:“some genres”, “aired”:“2020-02-30”, “episodes”:1}|{“result”:”success”}|Add a new anime to the end of the list
DELETE|/anime/info/:uid|None|{“result”: “success”}|Delete the anime with the given uid



### Tests
All the data, server script, and server-related libraries are included in /OO-API/ folder.    

Before running the server, please have these python modules installed: `routes` `cherrypy` `pandas` `scikit-learn`    

To test the OO_API library, use the following command `python test_api.py` or `python3 test_api.py`   

To test the API, use the following command `python test_api.py` or `python3 test_api.py` after starting the server.  

## JS Front End - User Interaction

### Description
This is a web front end where the user can glance popular animes and search for animes.  

On the main page, 3 random animes from our huge anime databaset are displayed together with their covers, titles, and synopsises. Click on the title of the anime or the cover, the user will be directed to the info page of that specific anime.  

The anime ranking is also listed on the main page. The top 3 animes will be displayed ranked by viewed members, rating score, and overall ranking. Click on the title of the anime on the list and the user will be directed to the info page of that specific anime. Click on "See More"  and the user will be directed to the ranking page.

On the ranking page of a given metric (viewed members, rating score, and overall ranking), the full ranking list will be displayed with the ranking of each anime along with its title. The user can click on the title of each anime and will be directed to the info page of that anime. The user can also click on previous and next to see more animes on the long ranking list. 

On the info page of a specific anime, the title, cover image, genre, aired time, number of episodes, number of people watched, popularity ranking, overall ranking, rating, and synopsis of this anime will be displayed. Click on "Discover" and the user will see several animes that are recommended because they are similar to the current anime on the page.   

The user can also search for an anime by clicking either the search button on the jumbotron or the tab on the upper right corner. The user can choose one out of 5 filters when searching: title will give an exact match of an anime title; genre will show animes of a given genre; keyword will search for a given word in anime titles and synopsises; year will give an exact match of the aired year; length will give an exact match of the number of episodes. The user can click on previous and next to see more animes in the search results. the user can click on the result title or cover image to be directed to the info page of that anime.  

### Deploy

All codes for the JS front end are included under `/jsfrontend` folder.  

To run the front end, first start the server locally by using the following command: `python anime_server.py` or `python3 anime_server.py`  

Then, navigate to "https://fangcong-yin.github.io/AnimeRecommender/index.html" (the gitlab page does not update for some unknown reasons) and have fun!  

### Test

To test all the user interaction of the js front end, please do the following step:  

1. On the main page, check if there is anything not rendering.  
2. Click on the cover image or title of an anime under popular animes and check if the website directs to its info page.  
3. Click on the Home button at the upper right corner and check if the websites goes back to the home page.  
4. On the main page, click on the title of an anime under anime ranking and check if the website directs to its info page.  
5. On the info page, check if there is anything not rendering.  
6. Click on the search button on the jumbotron and check if it directs to the search page.  
7. Choose any of the search filter, enter some texts, and click submit. Check if there is anything not rendering.  
8. Glance through the animes in the search results and try to use previous and next button to navigate through different pages of the search result.  
9. Go back to the main page and click on the see more hyperlink of each of the anime ranking list. Check if the page is redirected to the ranking page.  
10. Navigate through different pages of the ranking list by using previous and next button.  
11. Click on the title of animes on the ranking list and check if the page is redirected to the info page of that anime.  


## Complexity

This project involves building both the front end and back end of a recommendation system, simulating a full stack app development process.  

At the back end, the project involves basic data preprocessing produce on csv data using pandas dataframe and basic machine-learning-based recommendation system algorithm (k nearest neighbor algorithm). The data processing part is particularly complex when preparing training data for KNN algorithm.  

At the front end, this project involves dynamic element generation, nested API calls, multi-media display, form data processing, and search engine in JavaScript.

Though the feature of user login/signup that has been included in the initial plan is not implemented, the scale of the project is fairly large and complex.  

