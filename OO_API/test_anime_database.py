import unittest
from anime_database import anime_database
import json

class TestAnimeDatabase(unittest.TestCase):

    def init_data(self):
        ad = anime_database()
        ad.prepare_data()
        return ad
       
    def test_get_info_by_feature(self):
        ad = self.init_data()
        #Test return all information
        result = ad.get_info_by_feature(None,None)
        self.assertTrue(isinstance(result,dict))

        #Test return get anime information by genre
        result = ad.get_info_by_feature('genre','Drama')
        self.assertTrue(isinstance(result,dict))

        #Test return get anime information by keyword
        result = ad.get_info_by_feature('keyword','innocent')
        self.assertTrue(isinstance(result,dict))

        #Test return get anime information by title
        result = ad.get_info_by_feature('title','Death Note')
        self.assertTrue(isinstance(result,dict))

        #Test return get anime information by year
        result = ad.get_info_by_feature('aired',2020)
        self.assertTrue(isinstance(result,dict))

        #Test return get anime information by length
        result = ad.get_info_by_feature('episodes',25)
        self.assertTrue(isinstance(result,dict))

        #Test return get anime information by an unknown feature
        result = ad.get_info_by_feature('dfgdfgdfg',25)
        self.assertTrue(isinstance(result,dict) and len(result.keys()) == 0)

    def test_get_review_by_feature(self):
        ad = self.init_data()
        #Test return all review 
        result = ad.get_review_by_feature(None,None)
        self.assertTrue(isinstance(result,dict))

        #Test return get anime review by uid
        result = ad.get_info_by_feature('uid',28891)
        self.assertTrue(isinstance(result,dict)and len(result.keys()) > 0)

        #Test return get anime review by an unknown feature
        result = ad.get_review_by_feature('sfsfsdfs',28891)
        self.assertTrue(isinstance(result,dict)and len(result.keys()) == 0)
    def test_get_ranking_by_metric(self):
        ad = self.init_data()
        #Test return all reviews ranked by popularity
        result = ad.get_ranking_by_metric('popularity')
        self.assertTrue(isinstance(result,dict) and len(result.keys()) > 0)

        #Test return all reviews ranked by score
        result = ad.get_ranking_by_metric('score')
        self.assertTrue(isinstance(result,dict) and len(result.keys()) > 0)

        #Test return all reviews ranked by members
        result = ad.get_ranking_by_metric('members')
        self.assertTrue(isinstance(result,dict) and len(result.keys()) > 0)

        #Test return all reviews ranked by ranked
        result = ad.get_ranking_by_metric('ranked')
        self.assertTrue(isinstance(result,dict) and len(result.keys()) > 0)

        #Test return get anime review ranked by an unknown feature
        result = ad.get_ranking_by_metric('sfsfsdfs')
        self.assertTrue(isinstance(result,dict)and len(result.keys()) == 0)
    #Test adding a new anime to the information database
    def test_add_new_anime(self):
        ad = self.init_data()
        anime_dict = {'uid':1145141919810,'title':'anime', 'synopsis':'some synopsis', 'genre':'some genres', 'aired':'2020-02-30', 'episodes':1}
        ad.add_new_anime(anime_dict)
        result = ad.get_info_by_feature('title','anime')
        self.assertTrue(isinstance(result,dict)and len(result.keys()) > 0)
    #Test deleting an existing anime
    def test_delete_anime(self):
        ad = self.init_data()
        anime_dict = {'uid':1145141919810,'title':'anime', 'synopsis':'some synopsis', 'genre':'some genres', 'aired':'2020-02-30', 'episodes':1}
        ad.add_new_anime(anime_dict)
        ad.delete_anime(1145141919810)
        result = ad.get_info_by_feature('title','anime')
        self.assertTrue(isinstance(result,dict)and len(result.keys()) == 0)
    #Test updating an existing anime
    def test_update_anime(self):
        ad = self.init_data()
        anime_dict = {'uid':1145141919810,'title':'anime', 'synopsis':'some synopsis', 'genre':'some genres', 'aired':'2020-02-30', 'episodes':1}
        ad.add_new_anime(anime_dict)
        ad.update_anime(1145141919810,'episodes',810)
        result = ad.get_info_by_feature('title','anime')
        for key in result.keys():
            ep = int(result[key]['episodes'])
            self.assertTrue(ep == 810)
if __name__ == "__main__":
    unittest.main()