#This class has two functions to build trainset and testset for model
class RecommendingData:
    
    #this is the constructor called at the time of object creation
    def __init__(self, data):
        self.fullTrainSet = data.build_full_trainset()
        
    #This function returns FullTrain Set to train the model        
    def GetFullTrainSet(self):
        return self.fullTrainSet
    
    #This method returns the anti test set for the userId you have passed in argument
    #Then this testset is used tofind recommendations
    def GetAntiTestSetForUser(self, userId):
        trainset = self.fullTrainSet
        fill = trainset.global_mean
        anti_testset = []
        user_items = set([j for (j, _) in trainset.ur[userId]])
        anti_testset += [(str(userId), str(i), fill) for
                                 i in trainset.all_items() if
                                 i not in user_items]
        return anti_testset