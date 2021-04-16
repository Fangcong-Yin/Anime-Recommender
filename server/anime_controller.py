import sys,os
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import OO_API

from OO_API.anime_database import anime_database
import json
import cherrypy
import numpy as np

class AnimeController(object):
    def __init__(self):
        self.adb = anime_database()
        self.adb.prepare_data()
    

    def GET_ALL_INFO(self):
        output = dict()
        try:
            output['data'] = self.adb.get_info_by_feature(None,None)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def GET_INFO_BY_TITLE(self,title):
        output = dict()
        try:
            output['data'] = self.adb.get_info_by_feature('title',title)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def GET_INFO_BY_KEYWORD(self,keyword):
        output = dict()
        try:
            output['data'] = self.adb.get_info_by_feature('keyword',keyword)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def GET_INFO_BY_GENRE(self,genre):
        output = dict()
        try:
            output['data'] = self.adb.get_info_by_feature('genre',genre)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)
    def GET_INFO_BY_YEAR(self,year):
        
        output = dict()
        try:
            year = int(year)
            print(year)
            output['data'] = self.adb.get_info_by_feature('aired',year)
            output['result'] = 'success'
            
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def GET_INFO_BY_LENGTH(self,length):
        
        output = dict()
        try:
            length = int(length)
            output['data'] = self.adb.get_info_by_feature('episodes',length)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def GET_REVIEW_BY_UID(self,uid):
        output = dict()
        try:
            uid = int(uid)
            output['data'] = self.adb.get_review_by_feature('uid',uid)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def GET_ALL_REVIEW(self):
        output = dict()
        try:

            output['data'] = self.adb.get_review_by_feature(None,None)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def GET_RANKING(self,metric):
        output = dict()
        try:
            output['data'] = self.adb.get_ranking_by_metric(metric)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        
        return json.dumps(output)
    def UPDATE_REVIEW(self,uid):
        output = dict()
        input_data = json.loads(cherrypy.request.body.read().decode('utf-8'))
        try:
            uid = int(uid)
            score = float(input_data['score'])
            self.adb.update_anime(uid,'score',score)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
    def DELETE_INFO(self,uid):
        output = dict()
        try:
            uid = int(uid)
            self.adb.delete_anime(uid)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
    def ADD_INFO(self,title):
        output = dict()
        input_data = json.loads(cherrypy.request.body.read().decode('utf-8'))
        try:
            self.adb.add_new_anime(input_data)
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
    def RESET(self):
        output = dict()
        try:
            self.adb.prepare_data()
            output['result'] = 'success'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
        

if __name__=='__main__':
    ac = AnimeController()
    print(ac.GET_REVIEW_BY_UID(28891))
    print(ac.UPDATE_REVIEW(28891))
    print(ac.GET_REVIEW_BY_UID(28891))