# HACKTHON

Streamlite:https://sturdy-spork-wqq96xjqr5g39qxx-8501.app.github.dev/#

Document: https://docs.google.com/document/d/1fx4TTz66Fia7JOCKunaxRAGT44dueOwfXYQCg70I7qQ/edit?usp=sharing

Google Drive:
https://drive.google.com/drive/folders/1MMG8GqljYRy6HUMZkX9v7CXuaUfOr02R?usp=sharing

ColabLink:
https://colab.research.google.com/drive/1D9NzCv12le4eVpPgcPeq99Z8ZG0HNYT7?usp=sharing

Github:
https://github.com/c-40/HACKTHON


Implementation:


https://github.com/user-attachments/assets/0c2ce3e0-bd8d-4aa6-ae40-783749c875cd


https://github.com/user-attachments/assets/8244487f-0cfb-40bc-a6cf-a20ff3441d1c


<iframe width="800" height="450" 
src="https://www.youtube.com/embed/egXAHySYYSo?autoplay=1" 
title="YouTube video player" frameborder="0" 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen>
</iframe>


🔷 Project Title:
Credit Risk Classification Using Machine Learning on the German Credit Dataset

🔶 Project Introduction:
In the modern banking and financial sector, assessing the creditworthiness of loan applicants is a critical task. Misjudging an applicant’s risk can result in substantial financial losses, while being overly conservative may lead to missed opportunities and dissatisfied genuine borrowers.

To address this issue, our project develops a machine learning model that predicts whether a loan applicant is likely to default or repay a loan, based on historical credit data. The German Credit dataset, containing real-world information such as credit history, loan purpose, employment status, income level, savings, and more, is used to train and evaluate the model.

In addition to standard modeling, we also introduced a custom-defined feature called credit_risk_label, derived from a set of business-rule-driven thresholds that enhance the interpretability and robustness of the model.

🔹 Project Objectives:
✅ Build a machine learning classification model to predict credit risk (Good/Bad).

✅ Engineer a new feature (credit_risk_label) based on domain knowledge to enhance predictive capability.

✅ Preprocess the dataset for data quality and modeling compatibility.

✅ Perform exploratory data analysis to extract insights and patterns.

✅ Evaluate model performance using metrics such as accuracy, ROC-AUC, confusion matrix, F1-score, and learning curves.

🔸 Key Tasks Performed:
Data Cleaning and Preprocessing:
  Handled missing values
  Encoded categorical features using label/one-hot encoding
  Removed statistical outliers to reduce noise
  Scaled and normalized numeric features

📊 Exploratory Data Analysis (EDA):
Visualized feature distributions
Plotted correlations between variables
Compared risk classes against key features (e.g., loan amount, duration, job type)

🔢 Feature Engineering:
Added a custom rule-based risk feature credit_risk_label using this logic:

python
Copy
Edit
def label_credit_risk(row):

    if (
        row['Age'] <= 25 or
        row['Job'] == 0 or
        row['Credit amount'] > 8000 or
        (row['Saving accounts'] in ['little', 'none'] and row['Checking account'] in ['little', 'none'])
    ):
        return 1  # High risk
    else:
        return 0  # Low risk
This heuristic enhances interpretability and captures domain-specific risk indicators early in the pipeline.

⚙️ Model Building:
Used machine learning algorithms such as Decision Tree, Random Forest, or XGBoost.
Trained on processed features including the newly engineered credit_risk_label.
Performed cross-validation and hyperparameter tuning.
Analyzed feature importance to identify key influencers of credit risk.

🧪 Model Evaluation:
Measured accuracy, precision, recall, and F1-score
Plotted confusion matrix and ROC-AUC curve
Analyzed learning curves to detect overfitting or underfitting
**Model Accuracy: 0.89**

Confusion Matrix:
 [[145   2]
 [ 20  33]]

Classification Report:
               precision    recall  f1-score   support

           0       0.88      0.99      0.93       147
           1       0.94      0.62      0.75        53

    accuracy                           0.89       200
   macro avg       0.91      0.80      0.84       200
weighted avg       0.90      0.89      0.88       200

![image](https://github.com/user-attachments/assets/2d895f1b-af5c-4411-95c0-2848d96867eb)


🔶 Conclusion:
The developed machine learning model, supported by both data-driven and rule-based insights, proved effective in classifying applicants as low or high credit risk. The inclusion of the credit_risk_label feature, based on domain-specific thresholds, significantly improved interpretability and predictive power.
<img width="1267" alt="Screenshot 2025-04-24 at 11 23 07 PM" src="https://github.com/user-attachments/assets/d2efe71f-ed71-4a88-b9ba-dd502f9f975c" />







