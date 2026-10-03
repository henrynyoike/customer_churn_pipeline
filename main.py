from src import DataLoader , DataCleaner , DataIntegrity
from src.preprocessing import Preprocessor
from src.model import ChurnModel
import os

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir , "data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
loader = DataLoader(data_dir=data_dir)

data = loader.load()

cleaner = DataCleaner()
data = cleaner.clean(data)

integrity = DataIntegrity()
integrity_check = integrity.validate(data)

if not integrity_check :
    print("Data does not match the training data . Please check the columns and data types required")

preprocessing = Preprocessor()

y = preprocessing.preprocess_target(data["churn"])


data = data.drop(columns=["customerid" , "churn"]) # Remember to drop the customerid columns and the target variable before preprocessing 
#print(data)
numerical_output , categorical_output = preprocessing.preprocess(data)

model = ChurnModel()

model.fit(categorical_output , y)

