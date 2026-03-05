# Customer Churn Prediction using Machine Learning

## Project Overview
Customer churn is a critical business problem where retaining existing customers is more cost-effective than acquiring new ones.  
This project implements an end-to-end machine learning pipeline to predict customer churn using a large, feature-engineered dataset and multiple supervised learning models.

The goal is to identify customers who are likely to churn so that businesses can take proactive retention actions.

---

## Dataset
- Size: **220,000+ records**
- Type: Structured tabular data
- Target variable: `churn`  
  - `0` → Customer retained  
  - `1` → Customer churned  

### Features include:
- Customer demographics
- Account tenure and usage behavior
- Billing and payment patterns
- Service subscriptions
- Contract details
- Engineered engagement and support metrics

The dataset is fully cleaned and requires no additional preprocessing for model training.

---

## Exploratory Data Analysis (EDA)
Exploratory Data Analysis was performed to understand:
- Churn distribution
- Feature distributions
- Correlation between features
- Impact of tenure, monthly charges, support tickets, and contract type on churn
- Effectiveness of engineered features such as engagement score

Multiple visualizations such as histograms, boxplots, correlation heatmaps, and churn comparison plots were used to extract insights.

---

## Feature Engineering
Key engineered features include:
- **Average charge per GB**
- **High support contact indicator**
- **Long-term customer flag**
- **Engagement score** (combining usage, services, and tenure)

These features significantly improved the model’s ability to distinguish between churned and retained customers.

---

## Models Used
The following supervised learning models were trained and evaluated:

1. **Logistic Regression** – Baseline model for performance comparison  
2. **Random Forest Classifier** – Captures non-linear relationships and feature interactions  
3. **XGBoost Classifier** – Final and best-performing model  

All models were evaluated on the same train-test split for fair comparison.

---

## Model Evaluation
Models were evaluated using the following metrics:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Among all models, **XGBoost achieved the best overall performance**, particularly in terms of ROC-AUC, making it the final selected model.

---

## Results Summary
- Logistic Regression provided a strong baseline.
- Random Forest improved performance by capturing non-linear patterns.
- XGBoost outperformed all other models by effectively handling complex feature interactions and imbalance in the data.

This demonstrates the effectiveness of gradient boosting techniques for churn prediction on large tabular datasets.

---

## Technologies Used
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- XGBoost  

---

## Conclusion
This project demonstrates a complete machine learning workflow, from data exploration and feature engineering to model training, evaluation, and selection.  
By using a large-scale dataset and industry-relevant models, the solution closely reflects real-world customer churn prediction systems used in production environments.
