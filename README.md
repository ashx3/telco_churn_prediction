## Telecom Retention Using Data Science to address Customer Churn

![churn poster](/images/churn_poster.jpg)

# Context
The most common issue that any company faces is to retain their customers, be it gaming, food, banking or a telecom industry, the issue pertains to be the same. These companies invest in lump sum in order to retain their customers and it proves to be a challenging task.

![customer churn](/images/customer_churn.jpg)

# Content
Here we will analyzing the customer retention use case which will include all the customer behaviour and attributes that will be useful in identifying the characteristics of the churners. Such characteristics or insights will help in building a good model.

### Data Source
KAGGLE - https://www.kaggle.com/datasets/blastchar/telco-customer-churn

# Customer Churning can happen in many ways

![different churn scenarios](/images/different_churn_scenarios.jpg)

# Abstract
Customer churn is definitely bad to a firm’s profitability. Various strategies can be implemented to eliminate customer churn. The best way to avoid customer churn is for a company to truly know its customers. This includes identifying customers who are at risk of churning and working to improve their satisfaction. Improving customer service is of course, at the top of the priority for tackling this issue. Building customer loyalty through relevant experiences and specialized service is another strategy to reduce customer churn. Some firms survey customers who have already churned to understand their reasons for leaving in order to adopt a proactive approach to avoiding future customer churn.

# Company Goals
__Increasing profit! But how can we achieve it? Some of the way to increase profit are:__
- Acquiring new customers as much as we can
- Retaining existing customers as much as we can

![types of customers](/images/customer_types.jpg)

# Problems arising in order to retain
- Companies need to invest (expense costs) to get new customers.
- When a customer leaves the service (churns), it indicates a loss of investment.
- Cost, time and effort need to be channelled to replace customers who have left the service.
- Acquiring new customers is often more difficult and more expensive than retaining customers.
- On Harvard Business Review page, they said __"Acquiring a new customer is anywhere from 5 to 25 times more expensive than retaining an existing one"__. Below is a reference of the page for the same.

![Harvard Business Review reference page](/images/harvard_business_review.jpg)

# Objectives
- Predict whether customers will continue to use the service or will leave the service.
- Understanding the customer behaviours:
    - What keeps customers using the service.
    - What makes customers leave the service.

# Attribute Information

## Identifier
- customerID - ID number of the customer

## Churn
- Churn - Churn status, whether the customer churned or not

## Demographic information
- gender - Whether the customer is a male or female
- SeniorCitizen - Whether the customer is a senior citizen or not
- Partner - Whether the customer has a partner or not
- Dependents - Whether the customer has dependents or not

## Customer account information
- tenure - Number of months the customer has used the service
- Contract - The contract term of the customer
- PaperlessBilling - Whether the customer has paperless billing or not
- PaymentMethod - The customer's payment method
- MonthlyCharges - The amount charged to the customer monthly
- TotalCharges - The total amount charged to the customer

## Services that each customer has signed up for
- PhoneService - Whether the customer has a phone service or not
- MultipleLines - Whether the customer has multiple lines or not
- InternetService - Customer's internet service provider
- OnlineSecurity - Whether the customer has online security or not
- OnlineBackup - Whether the customer has online backup or not
- DeviceProtection - Whether the customer has device protection or not
- TechSupport - Whether the customer has tech support or not
- StreamingTV - Whether the customer has streaming TV or not
- StreamingMovies - Whether the customer has streaming movies or not

## Tasks Performed
##### 1. Data exploration: 
Exploring the dataset using pandas, numpy, matplotlib and seaborn libraries.

##### 2. Exploratory Data Analysis : 
Plotted different graphs to get more insights about dependent and independent features.

##### 3. Feature Engineering : 
There are numerical and categorical features are present. Scaling was performed on numerical data and encoding of categorical data is done.

##### 4. Model Building : 
For model building, data was splitted into training and testing set and various algorithms were used to train the model, namely:<br>
- Logistic Regression
- Ridge Classifier
- Decision Tree Classifier
- Random Forest Classifier
- KNN
- SVC
- Neural Network
- Gradient Boosing Classifier
- Adaboost Classifier
- CatBoost Classifier
- XGBoost
- LightGBM

##### 5. Model Selection : 
Trained all the models but as the dataset was imbalanced, evaluation metrics such as accuracy score were not used. So Oversampling techniques were performed and trained all the models then after. The best performing model turned out to be CatBoostClassifier.

##### 6. HyperParameter Tuning :
After picking out the best model using the evaluation metrics, HyperParameter Tuning was performed using GridSearchCV which is an exhaustive method but gives better results as it runs as a whole. After finding out the best parameters, PCA was performed, but the results were not promising, so it was not used in the model.

##### 7. Web Application & Deployment : 
Created a web application using streamlit API that takes all the necessary inputs from the user & shows the output. Then deployed project on the Heroku Platform.

# Helper
In this repository, we have performed the end to end Exploratory Data Analysis and identified the characteristics of the customers that are more likely to churn, trained the model using different classifiers, and then picking the model with good accuracy and performing hyperparameter tuning to further boost accuracy. Later on, we have created a web application using streamlit API that takes all the necessary inputs from the user & shows the output. And then deploying the project on the Heroku Platform.

### 🟢 For EDA, please refer to : Telco_Churn_Analysis_EDA.ipynb
### 🟢 For Model Building, please refer to : Telco_Churn_Analysis_Model Building.ipynb
### 🟢 For Model Deployment, please enter this link : https://telco-churn-prediction--app.herokuapp.com/

# How to start and use streamlit?

Simply run the following commands on command line and let it do the magic
```
pip3 install -r requirements.txt
streamlit run app.py
```

__This is how our Streamlit Application looks:__

![streamlitapp page1](/images/app1.jpg)

![streamlitapp page2](/images/app2.jpg)