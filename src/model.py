"""THe main Model for the Churn Pipeline"""
from sklearn.ensemble import RandomForestClassifier
from pandas import DataFrame
import sys

class ChurnModel :
    def __init__(self ,data:DataFrame=None,train:bool=False):
        """
        Class used to train the model and predict the churn data 
        """
        self.train = train

    def __model(self):
        model = RandomForestClassifier()
        return model

    def train(self,data:DataFrame=None):
        if not self.train: # Ensure Model is in training mode
            sys.exit("Error : Cannot train model in prediction mode.Please set 'train=True.'")
        
        model = self.__model()














