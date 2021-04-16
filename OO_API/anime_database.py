import pandas as pd
import numpy as np 
import json


class anime_database:

    def __init__(self):
        self.data_loc = '../animes.csv'
        self.anime_db = pd.read_csv(self.data_loc)
        self.features = self.anime_db.columns
        self.info_db = pd.DataFrame()
        self.review_db = pd.DataFrame()
    
    def prepare_data(self):
        #Info database only contains the factual information of an anime
        self.info_db = self.anime_db.iloc[:,0:6]
        self.info_db.drop_duplicates(keep='first',inplace=True)
        #Review database only contains the evaluation information of an anime
        self.review_db = self.anime_db.iloc[:,6:-2]
        self.review_db['uid'] = self.anime_db['uid']
        self.review_db['title'] = self.anime_db['title']
        self.review_db.drop_duplicates(keep='first',inplace=True)
    def get_info_by_feature(self,feature_name,feature_value):
        return_dict = dict()
        #If no features are entered, output information of all animes
        if(feature_name==None):
            return_dict = self.info_db.to_dict(orient='index')
        elif(feature_name in list(self.info_db)):
            #If filter by genre, call the helper function
            if(feature_name=='genre'):
                return_dict = self.get_info_by_genre(feature_value)
            #If filter by year (aired), call the helper function
            elif (feature_name=='aired'):
                return_dict = self.get_info_by_year(feature_value)
            
            else:
                return_db = self.info_db[self.info_db[feature_name] == feature_value]
                return_dict = return_db.to_dict(orient='index')
        #If filter by keyword, call the helper function
        elif(feature_name=='keyword'):
            return_dict = self.get_info_by_keyword(feature_value)

        return return_dict
    #This help function checks whether a given keyword is in the title or the synopsis of an anime
    def get_info_by_keyword(self,keyword):
        return_dict = dict()
        keyword = str(keyword)
        title_list = list(self.info_db['title'])
        syn_list = list(self.info_db['synopsis'])
        index_list = list()  
        for i in range(len(title_list)):
            title = str(title_list[i])
            syn = str(syn_list[i])
            if keyword in [ws.strip(',.?!') for ws in title.split()] or keyword in [ ws.strip(',.?!') for ws in syn.split()]:
                index_list.append(i)

        j = 0

        for i in index_list:
            try:
                return_dict[j] = self.info_db.loc[i].to_dict()
                #The following codes are used to convert the numpy values to normal int/float values for json parsing
                for key in return_dict[j].keys():
                    if(isinstance(return_dict[j][key],(np.float_,np.float16,np.float32,np.float64))):
                        return_dict[j][key] = float(return_dict[j][key])
                    elif(isinstance(return_dict[j][key],(np.int_,np.int16,np.int32,np.int64))):
                        return_dict[j][key] = int(return_dict[j][key])
                j+=1
            except:
                continue
        return return_dict
    #This help function checks whether a given genre is in the genre list of an anime
    def get_info_by_genre(self,genre):
        genre = str(genre)
        return_dict = dict()
        genre_dict = self.info_db['genre'].to_dict()
        j = 0
        for key in genre_dict.keys():
            if genre in genre_dict[key]:
                return_dict[j] = self.info_db.loc[int(key)].to_dict()
                #The following codes are used to convert the numpy values to normal int/float values for json parsing
                for key in return_dict[j].keys():
                    if(isinstance(return_dict[j][key],(np.float_,np.float16,np.float32,np.float64))):
                        return_dict[j][key] = float(return_dict[j][key])
                    elif(isinstance(return_dict[j][key],(np.int_,np.int16,np.int32,np.int64))):
                        return_dict[j][key] = int(return_dict[j][key])
                j+=1
        return return_dict
    #This help function checks whether a given year is in aired range of an anime
    def get_info_by_year(self,year):
        year = int(year)
        year_dict = self.info_db['aired'].to_dict()
        return_dict = dict()
        j = 0
        for key in year_dict.keys():
            year_list = year_dict[key].split(', ')
            year_list = year_list[1:]
            for i in year_list:
                try:
                    if (year == int(i[:4])):
                        return_dict[j] = self.info_db.loc[int(key)].to_dict()
                        #The following codes are used to convert the numpy values to normal int/float values for json parsing
                        for key in return_dict[j].keys():
                            if(isinstance(return_dict[j][key],(np.float_,np.float16,np.float32,np.float64))):
                                return_dict[j][key] = float(return_dict[j][key])
                            elif(isinstance(return_dict[j][key],(np.int_,np.int16,np.int32,np.int64))):
                                return_dict[j][key] = int(return_dict[j][key])
                        j+=1
                except:
                    continue
                    
        return return_dict
    #Get the review information of all animes by a given feature
    def get_review_by_feature(self,feature_name,feature_value):
        return_dict = dict()
        if(feature_name==None):
            return_dict = self.review_db.to_dict(orient='index')
        elif(feature_name in list(self.review_db)):
            return_db = self.review_db[self.review_db[feature_name] == feature_value]
            return_dict = return_db.to_dict(orient='index')
        return return_dict
    #Rank all animes by a given metric
    def get_ranking_by_metric(self,metric_name):
        return_dict = dict()
        if(metric_name in self.review_db.columns):
            sorted_db = self.review_db.copy()
            ascending=False
            #Ranked and popularity are ranked in ascending order
            if(metric_name=='ranked' or metric_name=='popularity'):
                ascending=True
            #score and members are ranked in descending order
            sorted_db.sort_values(by=[metric_name],ascending=ascending,inplace=True)
            return_dict = sorted_db.to_dict(orient='index')
        return return_dict
    #Add a new anime to the database
    def add_new_anime(self,anime_dict):
        self.info_db = self.info_db.append(anime_dict,ignore_index=True)
    #Delete an existing anime
    def delete_anime(self,uid):
        self.info_db = self.info_db.drop(self.info_db[self.info_db['uid']==uid].index)
        self.review_db = self.review_db.drop(self.review_db[self.review_db['uid']==uid].index)
    #Update specific information/review for an anime
    def update_anime(self,uid,update_feature,update_value):
        if update_feature in self.info_db.columns:
            self.info_db.loc[self.info_db[self.info_db['uid']==uid].index,update_feature] = update_value
        if update_feature in self.review_db.columns:
            self.review_db.loc[self.review_db[self.review_db['uid']==uid].index,update_feature] = update_value

if __name__=='__main__':
    ad = anime_database()
    ad.prepare_data()
    