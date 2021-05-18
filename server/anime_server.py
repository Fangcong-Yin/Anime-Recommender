import cherrypy
import routes
import os,sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import OO_API

from OO_API.anime_database import anime_database
from anime_controller import AnimeController

def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()
    ac = AnimeController()

    dispatcher.connect('get information by title', '/anime/info/title/:title', controller=ac, action = 'GET_INFO_BY_TITLE', conditions=dict(method=['GET']))
    dispatcher.connect('get information by keyword', '/anime/info/keyword/:keyword', controller=ac, action = 'GET_INFO_BY_KEYWORD', conditions=dict(method=['GET']))
    dispatcher.connect('get information by genre', '/anime/info/genre/:genre', controller=ac, action = 'GET_INFO_BY_GENRE', conditions=dict(method=['GET']))
    dispatcher.connect('get information by year', '/anime/info/year/:year', controller=ac, action = 'GET_INFO_BY_YEAR', conditions=dict(method=['GET']))
    dispatcher.connect('get information by length', '/anime/info/length/:length', controller=ac, action = 'GET_INFO_BY_LENGTH', conditions=dict(method=['GET']))
    dispatcher.connect('get all information', '/anime/info/', controller=ac, action = 'GET_ALL_INFO', conditions=dict(method=['GET']))
    dispatcher.connect('get all review', '/anime/review/', controller=ac, action = 'GET_ALL_REVIEW', conditions=dict(method=['GET']))
    dispatcher.connect('get review by uid', '/anime/review/:uid', controller=ac, action = 'GET_REVIEW_BY_UID', conditions=dict(method=['GET']))
    dispatcher.connect('get ranking by a metric', '/anime/review/ranking/:metric', controller=ac, action = 'GET_RANKING', conditions=dict(method=['GET']))
    dispatcher.connect('update the review score of an anime', '/anime/review/:uid', controller=ac, action = 'UPDATE_REVIEW', conditions=dict(method=['PUT']))
    dispatcher.connect('add a new anime', '/anime/info/:title', controller=ac, action = 'ADD_INFO', conditions=dict(method=['POST']))
    dispatcher.connect('delete an existing anime', '/anime/info/:uid', controller=ac, action = 'DELETE_INFO', conditions=dict(method=['DELETE']))
    dispatcher.connect('reset data', '/anime/reset/', controller=ac, action = 'RESET', conditions=dict(method=['PUT']))

    dispatcher.connect('recommendation', '/anime/rec/:anime_uid',controller=ac, action = 'GET_REC_ANIMES', conditions=dict(method=['GET']))


    dispatcher.connect('title option', '/anime/info/title/:title', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('keyword option', '/anime/info/keyword/:keyword', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('genre option', '/anime/info/genre/:genre', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('year option', '/anime/info/year/:year', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('length opiton', '/anime/info/length/:length', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('information option', '/anime/info/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('review option', '/anime/review/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('by uid option', '/anime/review/:uid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('ranking option', '/anime/review/ranking/:metric', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('delete option', '/anime/info/:uid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('reset option', '/anime/reset/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('recommendation option', '/anime/rec/:anime_uid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))

    conf = {
        'global' : {
            'server.thread_pool': 5,
            #Run on the localhost
            'server.socket_host' : 'localhost',
            'server.socket_port': 80
        },
    '/': {
        'request.dispatch' : dispatcher,
        'tools.CORS.on' : True,
        }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# class for CORS
class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

# function for CORS
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()
