"""The main Model for the Churn Pipeline"""
from sklearn.ensemble import RandomForestClassifier , GradientBoostingClassifier , VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransfomer
from sklearn.linear_model import LogisticRegression
from numpy.typing import ArrayLike
from pandas import DataFrame
import sys
from typing_extensions import Literal

class ChurnModel:
    def __init__(self , 
            categorical_model:Literal["random_forest" , "gradient_boosting_classifier" , "decision_tree"]="random_forest",
                 numerical_model:Literal["random_forest" , "gradient_boosting_classifier" , "decision_tree"]="gradient_boosting_classifier"):

        model_dict = {
            "random_forest" : RandomForestClassifier() , 
            "gradient_boosting_classifier": GradientBoostingClassifier() , 
            "decision_tree" : DecisionTreeClassifier()
        }

        self.cat_model = model_dict[categorical_model]
        self.num_model = model_dict[numerical_model]

    def fit(self , categorical_features:ArrayLike=None , numerical_features:ArrayLike=None , y:ArrayLike=None):
        # Fit the Chosen models
        self.columns_transfomer = ColumnTransfomer(transformers=[
                ("numerical_model" , self.num_model , numerical_features) , 
                ("categorical_model" , self.cat_model , categorical_features)
        ])


     

        return self.voting_clf.fit(X ,y)



