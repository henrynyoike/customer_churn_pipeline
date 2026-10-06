import os
import pandas as pd
from pandas import DataFrame
from numpy.typing import ArrayLike
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , OneHotEncoder , OrdinalEncoder , LabelEncoder
from sklearn.impute import SimpleImputer

class Preprocessor:
    def __init__(self):
        pass

    def preprocess(self , data:DataFrame|ArrayLike):
        """Preprocess the Data"""

        num_features  = data.select_dtypes(include=["int" , "float"])
        cat_features = data.select_dtypes(include=["object"])
        
        num_transformed = self.numerical_pipeline().fit_transform(num_features) # Transform the Numerical features
        cat_transformed = self.categorical_pipeline().fit_transform(cat_features) # Transform the categorical features

        return num_transformed , cat_transformed

    def numerical_pipeline(self) -> Pipeline :
        """Pipeline for numerical features"""
        num_pipe = Pipeline(steps = [
            ("num_imputer" , SimpleImputer(strategy="median")),
            ("num_scaler"  , StandardScaler())
        ])
        return num_pipe

    def target_encoder(self):
        """Encoding Target Variables"""
        return LabelEncoder()

    def categorical_pipeline(self) -> Pipeline :
        """Pipeline for categorical features""" 
        self.cat_pipe = Pipeline(steps = [
            ("cat_imputer" , SimpleImputer(strategy="most_frequent")) ,
            ("cat_encoder" , OrdinalEncoder(handle_unknown="error"))
        ])  
        return self.cat_pipe
