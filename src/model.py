"""The main Model for the Churn Pipeline"""
from sklearn.ensemble import RandomForestClassifier
from pandas import DataFrame
import sys

class ChurnModel :
    def __init__(self ,data:DataFrame=None,train:bool=False) -> None:
        """
        Class used to train the model and predict the churn data 
        """
        self.train = train
        self.model_trained = False # since model is not initially trained
        return None

    def __model(self):
        model = RandomForestClassifier()
        return model

    def train(self,X:DataFrame=None,y:DataFrame=None) -> bool:
        if not self.train: # Ensure Model is in training mode
            sys.exit("Error : Cannot train model in prediction mode.Please set 'train=True.'")
        
        model = self.__model()
        
        try:
            model.train(X,y)
        except Exception as e:
            print(e)
            return False    

        self.model_trained = True # Setting for model training
        return True

    def predict(self , X_data:DataFrame=None)-> DataFrame:
        pass
    














