
import os
import pandas as pd
from pandas import DataFrame
from data import DataLoader , DataCleaner
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , OneHotEncoder , OrdinalEncoder
from sklearn.impute import SimpleImputer

class Preprocessing:
    def __init__(self , data: DataFrame) -> None:
        pass
    
    def numerical_pipeline(self) -> Pipeline :
        """Transformer for numerical features"""
        num_pipe = Pipeline(steps = [
            ("num_imputer" , SimpleImputer(strategy="median")),
            ("num_scaler"  , StandardScaler())
        ])
        print(num_pipe)

        return num_pipe

    def categorical_pipeline(self) -> Pipeline :
        """Transformer for categorical features""" 
        cat_pipe = Pipeline(steps = [
            ("cat_imputer" , SimpleImputer()) ,
            ("cat_encoder" , OneHotEncoder(handle_unknown="error"))
        ])  
        
        return cat_pipe

# parent_dir = Path(__file__).resolve().parent.parent
# data_dir = os.path.join(parent_dir , "data")
# file_dir = os.path.join(data_dir , "WA_Fn-UseC_-Telco-Customer-Churn.csv")

# df = pd.read_csv(file_dir)

# df = DataCleaner(df).clean()

# processor = Preprocessing(data = df)

# processor.numerical_pipeline()

    

