#importing Dataset module and raeder class from surprise
from surprise import Dataset
from surprise import Reader
#importing pandas
import pandas as pd

#this is the class which have functions to load data
#this class also has functions to get movie name from movieid and vice-a-versa
class MovieLens:

    #Dictionary for MovieId to MovieName
    movieID_to_name = {}
    #Storing path of dataset into variables
    ratingsPath = "C:\\Users\\acer\\Desktop\\placment\\projects\\Movie Recommendation System\\data\\ratings.csv"
    moviesPath = "C:\\Users\\acer\\Desktop\\placment\\projects\\Movie Recommendation System\\data\\movies.csv"
    
    #This function load movielens data and returns rating dataset 
    #and also fill values in above dictionaries from movies dataset 
    def loadMovieLensLatestSmall(self):

        self.movieID_to_name = {}
        self.name_to_movieID = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)
        #Loading ratings dataset
        ratingsDataset = Dataset.load_from_file(self.ratingsPath, reader=reader)
        
        ds=pd.read_csv(self.moviesPath)
        ids=list(ds['movieId'])
        mname=list(ds['title'])
        for i in range(len(ids)):
                self.movieID_to_name[ids[i]] = mname[i]
                self.name_to_movieID[mname[i]] = ids[i]
            
        return ratingsDataset
    
    #this function returns Moviename for given movieid as argument
    def getMovieName(self, movieID):
        if movieID in self.movieID_to_name:
            return self.movieID_to_name[movieID]
        else:
            return ""
