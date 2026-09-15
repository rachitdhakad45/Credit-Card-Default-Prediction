\# Credit Card Default Prediction



A machine learning project that predicts whether a credit card customer is likely to default on their next month's payment.



The project includes exploratory data analysis, comparison of multiple machine learning models, model evaluation, and a Streamlit web application for making predictions on new customer data.



\---



\## 📌 Project Overview



Credit card default prediction is a classification problem where the goal is to identify customers who may fail to make their next credit card payment.



In this project, customer information, repayment history, bill amounts, and previous payment amounts are used to predict the likelihood of payment default.



The final trained model is integrated into a Streamlit application where users can enter customer details and receive:



\- Default / No Default prediction

\- Probability of default

\- Risk level



\---



\## 🎯 Problem Statement



Build a machine learning classification model that can predict whether a credit card customer will default on their next payment.



The project focuses on:



\- Understanding customer and repayment data

\- Performing exploratory data analysis

\- Comparing different classification algorithms

\- Evaluating models using multiple classification metrics

\- Selecting the best-performing model

\- Deploying the model through an interactive web application



\---



\## 📊 Dataset



The project uses the \*\*Default of Credit Card Clients Dataset\*\* from the UCI Machine Learning Repository.



The dataset contains information about 30,000 credit card customers.



Important features include:



\- Credit limit

\- Gender

\- Education

\- Marital status

\- Age

\- Repayment status for the previous 6 months

\- Bill amounts for the previous 6 months

\- Payment amounts for the previous 6 months



\### Target Variable



`default\_payment\_next\_month`



Where:



\- `0` → No default

\- `1` → Default



\---



\## 🔍 Exploratory Data Analysis



The notebook includes analysis of:



\- Dataset structure and data types

\- Missing and invalid values

\- Target class distribution

\- Customer demographics

\- Credit limit distribution

\- Repayment status

\- Bill amounts

\- Previous payment amounts

\- Default rate across important features

\- Feature correlations



Categorical values were also cleaned and grouped where appropriate.



\---



\## 🤖 Machine Learning Models



Three classification models were evaluated:



1\. Logistic Regression

2\. Random Forest

3\. HistGradientBoostingClassifier (Gradient Boosting)



The dataset was split into:



\- \*\*80% Training\*\*

\- \*\*20% Testing\*\*



Stratified splitting was used to preserve the target class distribution.



\---



\## 📈 Model Evaluation



The models were evaluated using:



\- Accuracy

\- Precision

\- Recall

\- F1 Score

\- Confusion Matrix

\- Classification Report



\### Model Comparison



| Model | Accuracy | Precision | Recall | F1 Score |

|---|---:|---:|---:|---:|

| Logistic Regression | 67.9% | 36.7% | 62.0% | 46.1% |

| Random Forest | \*\*79.9%\*\* | \*\*55.3%\*\* | 48.9% | 51.9% |

| \*\*Gradient Boosting\*\* | 76.4% | 47.5% | \*\*61.9%\*\* | \*\*53.7%\*\* |



\### Final Model



\*\*Gradient Boosting (HistGradientBoostingClassifier)\*\* was selected as the final model because it achieved the \*\*highest F1 score (53.7%)\*\* among the evaluated models while maintaining strong recall for the default class.



The trained model is saved using Joblib and loaded by the Streamlit application.



\---



\## 🌐 Streamlit Application



The trained model is integrated into an interactive Streamlit application.



Users can enter:



\### Customer Information

\- Credit limit

\- Age

\- Gender

\- Education

\- Marital status



\### Payment History

\- Repayment status for the previous 6 months



\### Financial Information

\- Bill amounts for the previous 6 months

\- Payment amounts for the previous 6 months



The application then provides:



\- Prediction

\- Default probability

\- Risk level



\---



\## 🖥️ Application Workflow



```text

User Input

&#x20;   ↓

Input Validation \& Transformation

&#x20;   ↓

23 Model Features

&#x20;   ↓

Trained Gradient Boosting Model

&#x20;   ↓

Prediction + Probability

&#x20;   ↓

Risk Level



