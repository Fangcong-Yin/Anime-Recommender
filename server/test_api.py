import unittest
import sys,os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import OO_API

from OO_API.anime_database import anime_database
import json
import requests

class TestAnimeDatabase(unittest.TestCase):
    SITE_URL = 'http://localhost:80'

    def test_put_reset(self):
        m = {}
        r = requests.put(self.SITE_URL+'/anime/reset/', json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.SITE_URL + '/anime/info/')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertEqual(animes['0']['uid'], 28891)
        
    def test_get_info_by_feature(self):
        m = {}
        r = requests.put(self.SITE_URL+'/anime/reset/', json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        #Search for animes by title: death note
        r = requests.get(self.SITE_URL + '/anime/info/title/Death Note')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        for key in animes.keys():
            self.assertEqual(animes[key]['title'], 'Death Note')
        
        #Search for animes by genre: Drama
        r = requests.get(self.SITE_URL + '/anime/info/genre/Drama')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        for key in animes.keys():
            genres = animes[key]['genre']
            self.assertTrue('Drama' in genres)

        #Search for animes by year: 2020
        r = requests.get(self.SITE_URL + '/anime/info/year/2020')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        for key in animes.keys():
            year_list = animes[key]['aired'].split(', ')
            year_list = year_list[1:]
            for i in year_list:
                year = int(i[:4])
                self.assertTrue(year,2020)

        #Search for animes by keyword: innocent
        r = requests.get(self.SITE_URL + '/anime/info/keyword/innocent')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        
        #Search for animes by length: 24
        r = requests.get(self.SITE_URL + '/anime/info/length/24')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        for key in animes.keys():
            self.assertEqual(animes[key]['episodes'],24)

    def test_get_review(self):
        m = {}
        r = requests.put(self.SITE_URL+'/anime/reset/', json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        #Search for reviews for all animes
        r = requests.get(self.SITE_URL + '/anime/review/')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        self.assertEqual(animes['0']['uid'], 28891)
        self.assertEqual(animes['0']['score'], 8.82)
        
        #Search for anime review by uid: 28891
        r = requests.get(self.SITE_URL + '/anime/review/28891')
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        self.assertEqual(animes['0']['uid'], 28891)
        self.assertEqual(animes['0']['ranked'], 25)
    def test_get_ranking(self):
        m = {}
        r = requests.put(self.SITE_URL+'/anime/reset/', json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        #Testing ranking all animes by the following metrics
        metrics = ['popularity','members','score','ranked']
        for m in metrics:
            r = requests.get(self.SITE_URL + '/anime/review/ranking/'+m)
            resp = json.loads(r.content.decode())
            animes = resp['data']
            self.assertTrue(len(animes.keys())>0)
            index_a = list(animes.keys())[0]
            index_b = list(animes.keys())[1]
            if(m == 'popularity' or m=='ranked'):
                self.assertTrue(float(animes[index_a][m]) < float(animes[index_b][m]))
            else:
                self.assertTrue(float(animes[index_a][m]) > float(animes[index_b][m]))
    #Test adding a new anime to the database
    def test_add_new_anime(self):
        m = {}
        r = requests.put(self.SITE_URL+'/anime/reset/', json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        anime_dict = {'uid':1145141919810,'title':'anime', 'synopsis':'some synopsis', 'genre':'some genres', 'aired':'2020-02-30', 'episodes':1}
        r = requests.post(self.SITE_URL+'/anime/info/'+anime_dict['title'], json.dumps(anime_dict))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SITE_URL + '/anime/info/title/'+anime_dict['title'])
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertTrue(len(animes.keys())>0)
        for key in animes.keys():
            self.assertEqual(animes[key]['title'], anime_dict['title'])
    #Test deleting an existing anime
    def test_delete_anime(self):
        m = {}
        r = requests.put(self.SITE_URL+'/anime/reset/', json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        anime_dict = {'uid':1145141919810,'title':'anime', 'synopsis':'some synopsis', 'genre':'some genres', 'aired':'2020-02-30', 'episodes':1}
        r = requests.post(self.SITE_URL+'/anime/info/'+anime_dict['title'], json.dumps(anime_dict))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.delete(self.SITE_URL+'/anime/info/'+str(anime_dict['uid']))
        resp = json.loads(r.content.decode())
        

        r = requests.get(self.SITE_URL + '/anime/info/title/'+anime_dict['title'])
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        animes = resp['data']
        self.assertTrue(len(animes.keys())==0)
    #Test updating the score of an existing anime
    def test_update_anime_score(self):
        m = {}
        r = requests.put(self.SITE_URL+'/anime/reset/', json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        anime_dict = {'uid':1145141919810,'title':'anime', 'synopsis':'some synopsis', 'genre':'some genres', 'aired':'2020-02-30', 'episodes':1}
        r = requests.post(self.SITE_URL+'/anime/info/'+anime_dict['title'], json.dumps(anime_dict))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        update_dict = {'score':10.0}
        r = requests.put(self.SITE_URL + '/anime/review/'+str(anime_dict['uid']),json.dumps(update_dict))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SITE_URL + '/anime/review/'+str(anime_dict['uid']))
        resp = json.loads(r.content.decode())
        animes = resp['data']
        self.assertEqual(resp['result'], 'success')
        for key in animes.keys():
            self.assertEqual(animes[key]['score'], 10)
        

       

if __name__ == "__main__":
    unittest.main()