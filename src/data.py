import pandas as pd
from pandas import DataFrame
import numpy as np
import yaml
import os , sys 

class DataLoader: 
    def __init__(self , data_dir:str = None):
        self.data_dir = data_dir

    def load(self):
        if not os.path.exists(self.data_dir):
            print(f"File Path : {self.data_dir} does not exist")
            sys.exit()
        data = pd.read_csv(self.data_dir)
        
        return data

class DataCleaner :
    def __init__(self ):
        pass

    def clean(self, data : DataFrame = None):
        self.data = data
        print("Lowering column names...")
        self.data = self.lower_col_names()
        
        print("Removing duplicate customer ids...")
        self.data = self.remove_duplicate_ids()
        
        print("Cleaning column Data types...")
        self.clean_col_dtypes()

        print("Converting values to lowercase...")
        self.data = self.convert_rowsto_lowercase()

        print("Removing ('automatic') in payment methods...")
        self.data = self.remove_automatic()

        print("Removing and replacing whitespaces...")
        self.data = self.remove_whitespaces()

        print("Removing Duplicated data...")
        self.data = self.drop_na_values()

        return self.data

    def lower_col_names(self):
        """Lower the column names """
        return self.data.rename(columns = str.lower)
    
    def remove_duplicate_ids(self):
        return self.data.drop_duplicates(subset=["customerid"])

    def clean_col_dtypes(self):
        """Ensure all the dtypes are in the type needed"""
        int_cols = ["seniorcitizen" , "tenure" , "monthlycharges" , "totalcharges"]
        for col in int_cols :
            self.data[col] = pd.to_numeric(self.data[col] , errors = "coerce")
        for col in self.data.columns:
            if col not in int_cols :
                self.data[col].astype("object")
        return self.data

    def convert_rowsto_lowercase(self):
        for col in self.data.select_dtypes(include=["str"]).columns :
            self.data[col] = self.data[col].str.lower()
        return self.data

    def remove_automatic(self):
        """Remove the data (automatic) from the column paymentmethod'"""
        self.data["paymentmethod"] = self.data["paymentmethod"].str.replace(r"\s*\(.*\)" , "", regex=True) 
        return self.data

    def remove_whitespaces(self):
        for col in self.data.select_dtypes(include=["str"]).columns:
            # Remove the whitespaces at the ends in order to replace those from the middle 
            self.data[col] = self.data[col].str.strip()
            self.data[col] = self.data[col].str.replace(r"\s" , "-" , regex=True)
        return self.data

    def drop_na_values(self):
        return self.data.dropna()

class DataIntegrity : 
    def __init_(self , data:DataFrame=None):
        """
        Checks the Integrity of the data i.e If it contains all the features and columns required
        """ 
        self.data = data

    def _check_columns(self) -> bool:
        """Checks if all the columns required are present"""
        columns = ['customerid', 'gender', 'seniorcitizen', 'partner', 'dependents',
       'tenure', 'phoneservice', 'multiplelines', 'internetservice',
       'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport',
       'streamingtv', 'streamingmovies', 'contract', 'paperlessbilling',
       'paymentmethod', 'monthlycharges', 'totalcharges', 'churn']

        if self.data.columns != colums:
            print("Missing columns in")

file_dir = "../data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

loader = DataLoader(data_dir=file_dir)
data = loader.load()
cleaner = DataCleaner()
data = cleaner.clean(data)

print(data.columns)
