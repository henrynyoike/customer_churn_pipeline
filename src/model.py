"""The main Model for the Churn Pipeline"""
from . import preprocessing
from sklearn.ensemble import RandomForestClassifier 
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
from numpy.typing import ArrayLike
from pandas import DataFrame
import sys
from typing_extensions import Literal

class ChurnModel:
    def __init__(self , model:Literal[ "LogisticRegression" , "RandomForestClassifier"]="RandomForestClassifier"):
        self.preprocessor = preprocessing.Preprocessor()
    
    def column_transformer(self , data:DataFrame=None):
        """A set of Transformers for  preprocessing the Independent Variables"""


        num_cols = data.select_dtypes(include=["float64" , "int64" , "int" , "float"]).columns
        cat_cols = data.select_dtypes(include=["object"]).columns

        numerical_pipeline = self.preprocessor.numerical_pipeline()
        categorical_pipeline = self.preprocessor.categorical_pipeline()
        
        transformer = ColumnTransformer(transformers=[
            ("numerical_pipeline" , numerical_pipeline, num_cols) , 
            ("categorical_pipeline" , categorical_pipeline , cat_cols) 
        ])

        return transformer

    def fit(self , X:ArrayLike|DataFrame=None , y:ArrayLike|DataFrame=None):
        """Train the Churn Model using Pipelines and Transformers"""
        n_samples , n_features = np.shape(X)

        if n_samples != np.shape(y)[0]:
            raise ValueError("X and Y must be of the Same shape.")
        
        transformers = self.column_transformer(data = X)
        self.target_encoder = self.preprocessor.target_encoder()
        
        self.y = self.target_encoder.fit_transform(y)
        
        self.model_pipeline = Pipeline(steps=[
            ("column_transformer" , transformers),
            ("training_model" , RandomForestClassifier())
        ])
        

        self.model_pipeline.fit(X ,self.y)

    def predict(self , X:ArrayLike|DataFrame):
        return self.model_pipeline.predict(X)

