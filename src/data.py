import pandas as pd
from pandas import DataFrame
import numpy as np
import yaml

class DataLoader: 
    def __init__(self , data_dir:str = None):
        self.data_dir = data_dir

    def load(self) :
        try :
            self.data = pd.read_csv(self.data_dir)
            return self.data
        except Exception as e :
            if not self.data_dir :
                print("Please pass data directory")
            else:
                print("Failed to load file : Please find a suitable file directory")
        return None

class DataCleaner :
    def __init__(self , data : DataFrame = None):
        self.data = data
       
    def clean(self):
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
        for col in self.data.select_dtypes(include=["object"]).columns :
            self.data[col] = self.data[col].str.lower()
        return self.data

    def remove_automatic(self):
        """Remove the data (automatic) from the column paymentmethod'"""
        self.data["paymentmethod"] = self.data["paymentmethod"].str.replace(r"\s*\(.*\)" , "", regex=True) 
        return self.data

    def remove_whitespaces(self):
        for col in self.data.select_dtypes(include=["object"]).columns:
            # Remove the whitespaces at the ends in order to replace those from the middle 
            self.data[col] = self.data[col].str.strip()
            self.data[col] = self.data[col].str.replace(r"\s" , "-" , regex=True)
        return self.data

    def drop_na_values(self):
        return self.data.dropna()

