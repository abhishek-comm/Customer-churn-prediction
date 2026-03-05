# Customer Churn Prediction using Machine Learning

## Project Overview
Customer churn prediction is an important problem for subscription-based businesses where retaining existing customers is often more cost-effective than acquiring new ones.

This project builds a machine learning system that predicts whether a customer is likely to churn based on demographic information, service usage patterns, support interactions, and billing behavior.

The project includes a trained machine learning model and a Streamlit web application that allows real-time churn prediction by entering customer details.

---

## Dataset
- Size: **220,000+ records**
- Type: Structured tabular dataset
- Target variable: `churn`

Target labels:
- `0` → Customer retained
- `1` → Customer churned

### Features include:
- Customer demographics
- Account tenure
- Internet usage patterns
- Support ticket history
- Billing information
- Service subscriptions
- Contract type
- Engineered behavioral features

The dataset is cleaned and prepared for machine learning modeling.

---

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis was performed to understand patterns related to churn. The analysis included:

- Distribution of churn vs retained customers
- Feature distributions
- Correlation between numerical variables
- Relationship between tenure, monthly charges, and churn
- Impact of support tickets and contract type on churn probability

Various visualizations such as histograms, boxplots, and correlation heatmaps were used to extract insights.

---

## Feature Engineering
Several additional features were created to improve model performance:

- **Average charge per GB**
- **High support contact indicator**
- **Long-term customer flag**
- **Engagement score** (combining usage and tenure)

These engineered features help the model better capture customer behavior patterns associated with churn.

---

## Model Used
The final model used in this project is:

**Random Forest Classifier**

Random Forest was chosen because it:
- Handles non-linear relationships effectively
- Is robust to noise and overfitting
- Works well with tabular datasets
- Captures feature interactions automatically

The trained model predicts churn probability for each customer.

---

## Model Evaluation
The model was evaluated using standard classification metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

These metrics help assess the model's ability to correctly identify customers who are likely to churn.

---

## Web Application
A **Streamlit web application** is included to demonstrate the model in action.

Users can enter customer details such as:

- Age
- Gender
- Tenure
- Monthly usage
- Support tickets
- Monthly charges
- Payment delay ratio
- Service subscriptions
- Contract type

The application processes the inputs, generates engineered features, and returns:

- **Churn prediction**
- **Churn probability**

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## Conclusion
This project demonstrates a complete machine learning workflow including data exploration, feature engineering, model training, evaluation, and deployment through a web interface.

The system provides a practical example of how machine learning can be used to identify high-risk customers and support business decisions for customer retention.
