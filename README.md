## Telecom Retention Using Data Science to address Customer Churn

![churn poster](/images/churn_poster.jpg)

# Context
The most common issue that any company faces is to retain their customers, be it gaming, food, banking or a telecom industry, the issue pertains to be the same. These companies invest in lump sum in order to retain their customers and it proves to be a challenging task. The primary goal is to develop a model that can predict customer churn, i.e. identify customers who are likely to stop using the company's services. By predicting customer churn in advance, companies can take proactive measures to retain their valuable customers and reduce attrition rates.

![customer churn](/images/customer_churn.jpg)

# Content
In this project, we will analyze the customer retention use case, focusing on customer behavior and attributes. Our objective is to identify the characteristics of churners, which will be instrumental in building an effective model. By gaining insights into these characteristics, we aim to create a robust model that can predict and improve customer retention rates.

### Data Source
KAGGLE - https://www.kaggle.com/datasets/blastchar/telco-customer-churn

# Customer Churning can happen in many ways

![different churn scenarios](/images/different_churn_scenarios.jpg)

# Company Goals
__Increasing profit! But how can we achieve it? Some of the way to increase profit are:__
- Acquiring new customers as much as we can
- Retaining existing customers as much as we can

![types of customers](/images/customer_types.jpg)

# Problems arising in order to retain
- __Investment Costs:__ <br>
Companies have to invest significant resources and expenses to acquire new customers, making it crucial to retain existing ones to maximize return on investment.

- __Loss of Investment:__ <br>
When a customer leaves the service (churns), it signifies a loss of the investment made in acquiring that customer. Retaining customers becomes essential to avoid such losses.

- __Replacement Efforts:__ <br>
Losing customers requires redirecting cost, time, and effort to replace them, which can be resource-intensive and impact overall efficiency.

- __Acquisition vs. Retention:__ <br>
Acquiring new customers is not only difficult but also more expensive compared to retaining existing customers. Hence, a strong focus on customer retention is vital for sustainable growth and profitability.

- On Harvard Business Review page, they said __"Acquiring a new customer is anywhere from 5 to 25 times more expensive than retaining an existing one"__

![Harvard Business Review reference page](/images/harvard_business_review.jpg)

# Objectives
- __Predictive Modeling:__<br>
Develop a predictive model to forecast whether customers are likely to continue using the service or churn.

- __Understanding Customer Behaviors:__ <br>
Gain insights into customer behaviors by analyzing patterns and factors that influence customer retention and churn.

- __Retention Strategies:__ <br>
Use the model to identify key factors that contribute to customer retention and design effective retention strategies to reduce churn rates.

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
### 1. Data exploration: 
Explored the dataset using pandas, numpy, matplotlib, and seaborn libraries to understand its structure and contents.

### 2. Exploratory Data Analysis : 
Visualized data through various graphs to gain insights into the relationships between dependent and independent features.

### 3. Feature Engineering : 
Performed feature engineering to handle numerical and categorical features. Scaled numerical data and encoded categorical data for model compatibility.

### 4. Model Building : 
Split the data into training and testing sets and trained various algorithms for predictive model, including::<br>
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

### 5. Model Selection : 
Due to dataset imbalance, evaluation metrics like accuracy were not reliable. Oversampling techniques were applied to balance the dataset and retrained the models. The CatBoostClassifier performed the best.

### 6. HyperParameter Tuning :
After selecting the best model based on evaluation metrics, GridSearchCV was utilized for Hyperparameter Tuning, providing better results as it comprehensively searches for optimal parameters.

### 7. Web Application & Deployment : 
Developed a web application using Streamlit API to take user inputs and display the corresponding outputs.

# Conclusion
Customer churn is a significant threat to a company's profitability. To mitigate it, firms can implement various strategies such as understanding their customers better, identifying at-risk customers, and enhancing customer satisfaction. Improving customer service and providing personalized experiences can build loyalty and reduce churn. Additionally, conducting surveys with churned customers helps gather insights to proactively address future churn.

# Helper
This project consists of three main components (jupyter notebooks):

### 🟢 For EDA, please refer to : telco_Churn_Analysis_EDA.ipynb
### 🟢 For Model Building, please refer to : telco_Churn_Analysis_Model Building.ipynb
### 🟢 For Model Deployment, please enter this link : https://ashx3-insurance-premium-prediction.streamlit.app/

# How to start and use streamlit?

Simply run the following commands on command line and let it do the magic
```
pip3 install -r requirements.txt
streamlit run app.py
```

__This is how our Streamlit Application looks:__

![streamlitapp page1](/images/app1.jpg)

![streamlitapp page2](/images/app2.jpg)
