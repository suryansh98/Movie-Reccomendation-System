#Importing class recommending data from recommending data file present in the same directory
from RecommendingData import RecommendingData

#importing the SVD algo from surprise package
from surprise import SVD

#This class is the main class as it has function to find recommendation
class Recommender:
    
    #this is the constructor which assigns the object of recommending data class to passed to it
    def __init__(self, dataset):
        rd = RecommendingData(dataset)
        self.dataset = rd
    
    #This function calculates the recommendations as it is taking three arguments 
    #ml,testSubject and n which are MovieLens object,UserId and No. of recs respectively. 
    def SVDTopNRecs(self, ml, userId, n):
        
        #Using recommender SVD
        SVDAlgorithm = SVD(n_factors=100,random_state=10)
        
        #Building recommendation model...
        trainSet = self.dataset.GetFullTrainSet()
        SVDAlgorithm.fit(trainSet)
            
        #Computing recommendations...
        testSet = self.dataset.GetAntiTestSetForUser(userId)
        
        predictions = SVDAlgorithm.test(testSet)
            
        recommendations = []
        
        #filtering movieid and estimate rating from predictions to recommendations
        for userID, movieID, actualRating, estimatedRating, _ in predictions:
            intMovieID = int(movieID)
            recommendations.append((intMovieID, estimatedRating))
            
        #Sorting the recommendations list using ratings in descending order to return top n recs    
        recommendations.sort(key=lambda x: x[1], reverse=True)
        recommendations=recommendations[:n]
        
        return recommendations

            
            
    
    
