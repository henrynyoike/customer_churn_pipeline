from src import DataLoader , DataCleaner , DataIntegrity
from src import ChurnModel
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import os

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir , "data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
loader = DataLoader(data_dir=data_dir)

# Load the Data
data = loader.load()

# Clean the Data
cleaner = DataCleaner()
data = cleaner.clean(data)

# Validate that the data contains the required columns
integrity = DataIntegrity()
integrity_check = integrity.validate(data)

if not integrity_check :
    print("Data does not match the training data . Please check the columns and data types required")

# Drop the columns customerid and churn (target variable)

X = data.drop(columns=["customerid" , "churn"]) 
y = data["churn"]

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size=0.2)

model = ChurnModel()

model.fit(X_train , y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(model.target_encoder.transform(y_test) , y_pred)

print(accuracy)


