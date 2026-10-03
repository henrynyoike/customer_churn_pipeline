Here is the complete README rewritten with the **MIT License** included.

# Customer Churn Prediction Pipeline

A modular machine learning pipeline for predicting customer churn using the **Telco Customer Churn** dataset.

The project is structured as a reusable ML pipeline with separate components for data loading, cleaning, validation, preprocessing, feature engineering, model training, and evaluation.

> **Status:** 🚧 Work in Progress

---

## Overview

Customer churn prediction is a binary classification problem where the goal is to predict whether a customer is likely to leave a telecom service.

This project uses customer demographic information, subscribed services, contract details, billing information, and tenure to prepare data for a churn prediction model.

The pipeline is designed to provide a clean separation between the major stages of a machine learning workflow.

### Main stages

```text
Data Loading
     ↓
Data Cleaning
     ↓
Data Validation
     ↓
Feature Engineering
     ↓
Preprocessing
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model & Metrics Export
```

---

## Dataset

The project uses the **Telco Customer Churn** dataset.

The dataset contains:

* **7,043 records**
* **21 columns**
* **20 input features**
* **1 target variable**

### Target Variable

The prediction target is:

```text
Churn
```

Possible values:

```text
Yes
No
```

The dataset contains:

| Churn | Records |
| ----- | ------: |
| No    |   5,174 |
| Yes   |   1,869 |

### Feature Categories

#### Customer Information

* `customerID`
* `gender`
* `SeniorCitizen`
* `Partner`
* `Dependents`

#### Service Information

* `PhoneService`
* `MultipleLines`
* `InternetService`
* `OnlineSecurity`
* `OnlineBackup`
* `DeviceProtection`
* `TechSupport`
* `StreamingTV`
* `StreamingMovies`

#### Contract & Billing Information

* `Contract`
* `PaperlessBilling`
* `PaymentMethod`
* `MonthlyCharges`
* `TotalCharges`

#### Target

* `Churn`

---

## Project Structure

```text
Customer_Churn_Pipeline/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── model.py
│   └── evaluate.py
│
├── config.yaml
├── main.py
├── tests.py
├── goal.txt
└── .gitignore
```

---

## Pipeline Architecture

```text
                    ┌──────────────────┐
                    │   Raw CSV Data   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Data Loading   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Data Cleaning   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Data Validation  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │Feature Engineering│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Preprocessing   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Model Training   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Model Evaluation │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Model & Metrics  │
                    └──────────────────┘
```

---

# Components

## `src/data.py`

Handles dataset loading, cleaning, and integrity validation.

### `DataLoader`

Responsible for loading the dataset from the configured data directory.

The loader verifies that the dataset exists before attempting to read it.

Example:

```python
loader = DataLoader(data_dir=data_dir)
data = loader.load()
```

### `DataCleaner`

The cleaning stage performs several transformations:

* Normalizes column names
* Removes duplicate customer IDs
* Converts numerical columns to numeric types
* Normalizes categorical values
* Removes unnecessary whitespace
* Normalizes payment-method strings
* Handles missing values

The numerical columns include:

```text
seniorcitizen
tenure
monthlycharges
totalcharges
```

`TotalCharges` requires conversion because the original dataset stores it as a string/object column.

### `DataIntegrity`

Validates the cleaned dataset against the expected schema.

The validation process checks for required columns including:

```text
customerid
gender
seniorcitizen
partner
dependents
tenure
phoneservice
multiplelines
internetservice
onlinesecurity
onlinebackup
deviceprotection
techsupport
streamingtv
streamingmovies
contract
paperlessbilling
paymentmethod
monthlycharges
totalcharges
churn
```

It also verifies expected data types.

---

# `src/preprocessing.py`

Contains the feature preprocessing pipeline.

The preprocessor separates the input data into numerical and categorical features.

## Numerical Features

The numerical preprocessing pipeline uses:

```text
Median Imputation
       ↓
Standard Scaling
```

Implemented using:

```python
SimpleImputer(strategy="median")
StandardScaler()
```

This allows missing numerical values to be handled while placing numerical features on a standardized scale.

## Categorical Features

The categorical preprocessing pipeline uses:

```text
Most-Frequent Imputation
          ↓
One-Hot Encoding
```

Implemented using:

```python
SimpleImputer(strategy="most_frequent")
OneHotEncoder(handle_unknown="error")
```

Categorical variables are converted into numerical representations suitable for machine learning models.

## Target Encoding

The `Churn` target is converted from:

```text
Yes / No
```

into numerical labels using `LabelEncoder`.

---

# `src/features.py`

Contains feature-engineering logic.

The project currently defines a derived feature based on customer tenure and monthly charges:

```text
charges_tenure_ratio
```

The intended calculation is:

```text
MonthlyCharges / tenure
```

Feature engineering is separated into its own module so that additional domain-specific features can be introduced without modifying the core preprocessing logic.

Potential future features include:

* Customer tenure groups
* Number of subscribed services
* Total services used
* Charge-to-tenure relationships
* Contract-based indicators
* Service combinations

---

# `src/model.py`

Contains the machine-learning model layer.

The project currently references tree-based classifiers including:

* `RandomForestClassifier`
* `GradientBoostingClassifier`
* `DecisionTreeClassifier`

The project specification also calls for a linear baseline:

* `LogisticRegression`

The intended model comparison is:

```text
Logistic Regression
        vs
Tree-Based Classifier
```

This allows the pipeline to compare a linear model against a nonlinear model.

---

# `src/evaluate.py`

Reserved for model evaluation and reporting.

The completed evaluation stage is intended to calculate:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

It is also intended to generate:

* Confusion matrices
* Feature importance
* JSON-formatted evaluation metrics

---

# Configuration

Pipeline configuration is stored in:

```text
config.yaml
```

The configuration contains project and dataset settings.

Example:

```yaml
name: "Telco Customer Churn Prediction"

directories:
  data: "./data/WA_Fn-UseC_-Telco-Customer-Churn.csv"

dataset:
  splits:
    training_set: 0.7
    validation_set: 0.10
    testing_set: 0.20
```

The intended dataset split is:

| Dataset    | Percentage |
| ---------- | ---------: |
| Training   |        70% |
| Validation |        10% |
| Testing    |        20% |

---

# Installation

## Requirements

The project uses Python and the following main dependencies:

* Python 3.12.3
* pandas
* NumPy
* scikit-learn
* PyYAML

Install the dependencies with:

```bash
pip install pandas numpy scikit-learn pyyaml
```

---

# Usage

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd Customer_Churn_Pipeline
```

Run the pipeline:

```bash
python main.py
```

The current `main.py` is responsible for the initial pipeline stages:

1. Load the dataset
2. Clean the dataset
3. Validate the dataset
4. Encode the target
5. Remove the customer ID and target columns
6. Separate numerical and categorical features
7. Apply preprocessing
8. Pass the processed data to the model component

The complete training and evaluation workflow is still under development.

---

# Machine Learning Workflow

The intended workflow is:

```text
Raw Dataset
     │
     ▼
Data Validation
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Train / Validation / Test Split
     │
     ▼
Feature Preprocessing
     │
     ├───────────────┐
     ▼               ▼
Numerical        Categorical
Features          Features
     │               │
     ▼               ▼
Imputation       Imputation
     │               │
     ▼               ▼
Scaling          One-Hot Encoding
     │               │
     └───────┬───────┘
             ▼
       Model Training
             │
             ▼
       Model Validation
             │
             ▼
       Final Evaluation
             │
             ▼
     Model + Metrics
```

---

# Models

## Logistic Regression

Logistic Regression provides a simple linear baseline for the binary churn classification problem.

It can provide an interpretable reference point against which more complex models can be compared.

## Random Forest

Random Forest is intended to provide a nonlinear tree-based alternative capable of modeling interactions between customer characteristics and services.

Other tree-based models referenced by the project include:

* Decision Tree
* Gradient Boosting

---

# Evaluation Metrics

The completed pipeline will use several classification metrics.

| Metric    | Description                                                       |
| --------- | ----------------------------------------------------------------- |
| Accuracy  | Overall proportion of correct predictions                         |
| Precision | Proportion of predicted churn cases that are actually churn cases |
| Recall    | Proportion of actual churn cases detected by the model            |
| F1-score  | Harmonic mean of precision and recall                             |
| ROC-AUC   | Measures the model's ability to discriminate between classes      |

A confusion matrix will also be used:

```text
                    Predicted
                  No       Yes
              ┌────────┬────────┐
Actual   No   │   TN   │   FP   │
              ├────────┼────────┤
         Yes  │   FN   │   TP   │
              └────────┴────────┘
```

For tree-based models, feature importance can also be examined to identify influential input variables.

---

# Data Leakage Prevention

A key goal of the completed pipeline is to prevent information from the validation or test sets from influencing preprocessing.

The intended workflow is:

```text
Split Dataset
     │
     ├── Training
     ├── Validation
     └── Testing
           │
           ▼
Fit preprocessing only on training data
           │
           ▼
Transform validation/test data
```

The preprocessing implementation should ultimately be integrated with the train/test split using an sklearn `Pipeline` and `ColumnTransformer`.

---

# Reproducibility

The project is designed to support reproducible experiments through centralized configuration and controlled random states.

Configuration is stored in:

```text
config.yaml
```

Model and dataset parameters should be controlled from the configuration rather than being scattered throughout the source code.

---

# Current Development Status

| Component                    | Status         |
| ---------------------------- | -------------- |
| Dataset                      | ✅ Included     |
| Data loading                 | ✅ Implemented  |
| Column normalization         | ✅ Implemented  |
| Duplicate handling           | ✅ Implemented  |
| Numeric conversion           | ✅ Implemented  |
| Categorical cleaning         | ✅ Implemented  |
| Data validation              | ✅ Implemented  |
| Numerical preprocessing      | ✅ Implemented  |
| Categorical preprocessing    | ✅ Implemented  |
| Target encoding              | ✅ Implemented  |
| Feature engineering          | 🚧 In progress |
| Train/validation/test split  | 🚧 In progress |
| Logistic Regression          | 🚧 In progress |
| Random Forest                | 🚧 In progress |
| Model evaluation             | 🚧 In progress |
| Confusion matrix             | 🚧 In progress |
| Feature importance           | 🚧 In progress |
| Model serialization          | 🚧 In progress |
| Metrics export               | 🚧 In progress |
| Complete end-to-end pipeline | 🚧 In progress |

---

# Known Development Issues

The project is currently under active development and is not yet a completed production-ready pipeline.

Current areas requiring further implementation include:

* Completing model-training logic
* Completing the evaluation module
* Completing feature engineering
* Implementing the configured dataset split
* Connecting `config.yaml` to the actual pipeline
* Preventing preprocessing leakage
* Saving trained models
* Saving evaluation metrics
* Adding automated tests
* Completing the end-to-end execution flow

The current categorical encoder also uses:

```python
OneHotEncoder(handle_unknown="error")
```

which may cause errors when previously unseen categories are encountered during inference. This should be considered when the prediction pipeline is finalized.

---

# Future Improvements

Planned improvements include:

* [ ] Implement train/validation/test splitting
* [ ] Integrate `Pipeline` and `ColumnTransformer`
* [ ] Complete feature engineering
* [ ] Implement Logistic Regression
* [ ] Implement Random Forest
* [ ] Add model comparison
* [ ] Implement evaluation metrics
* [ ] Generate confusion matrices
* [ ] Add feature-importance analysis
* [ ] Save trained models
* [ ] Export metrics to JSON
* [ ] Add automated tests
* [ ] Add structured logging
* [ ] Make `config.yaml` control the complete pipeline
* [ ] Add a prediction interface
* [ ] Export predictions to CSV

---

# Design Principles

The project follows several core principles:

### Modularity

Each major stage of the ML workflow is separated into its own module.

### Reproducibility

Configuration and random seeds should make experiments repeatable.

### Data Validation

Input data should be validated before being passed to the model.

### Leakage Prevention

Preprocessing transformations should only be fitted using training data.

### Maintainability

Data handling, preprocessing, feature engineering, modeling, and evaluation remain separated.

### Explainability

The final system should provide meaningful evaluation metrics and model insights.

### CLI-First

The pipeline is designed to be executable directly from the command line.

---

# License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for the full license text.

---

## Author

**HSQ**

Machine Learning / AI Engineering Project

