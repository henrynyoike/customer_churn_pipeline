import pandas as pd
from data import Dataloader , DataCleaner

class FeatureEngineer :
    """Create new columns/features from the raw data""" 
    def __init__(self , data):
        self.data = data

    def start(self):
        self.data = self._monthly_tenure_ratio(self.data) # Monthly charges to Tenure ratio

        return self.data

    def _monthly_tenure_ratio(self , df):
        """Create a feature - ratio of monthly charges to tenure""" 
         df["charges_tenure_ratio"] = df["monthlycharges"] / df["tenure"] # Get the ratio
         return df

#* Tenure-based ratios
#* Charges per month
#* Contract-derived signals



