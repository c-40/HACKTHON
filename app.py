import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load pre-trained model pipelines (ensure correct paths)
logreg_pipeline_1 = joblib.load('credit_risk_model.pkl')
logreg_pipeline_2 = joblib.load('optimized_credit_risk_model.pkl')

# Streamlit app title
st.title('Credit Risk Prediction')

# Streamlit form for user input
st.sidebar.header('Enter Information')

# Take user input via the sidebar form
age = st.sidebar.number_input('Age', min_value=18, max_value=100, value=35)
sex = st.sidebar.selectbox('Sex', ['male', 'female'])
job = st.sidebar.selectbox('Job', [0, 1, 2])  # Assuming these are categorical values for Job
housing = st.sidebar.selectbox('Housing', ['own', 'rent'])
saving_accounts = st.sidebar.selectbox('Saving accounts', ['little', 'moderate', 'rich'])
checking_account = st.sidebar.selectbox('Checking account', ['little', 'moderate', 'rich', 'none'])
credit_amount = st.sidebar.number_input('Credit amount', min_value=1000, max_value=10000, value=3000)
duration = st.sidebar.number_input('Duration', min_value=6, max_value=72, value=24)
purpose = st.sidebar.selectbox('Purpose', ['radio/tv', 'education', 'new car', 'used car', 'furniture/equipment', 'others'])

# Convert the input data into a dictionary
input_data = {
    'Age': age,
    'Sex': sex,
    'Job': job,
    'Housing': housing,
    'Saving accounts': saving_accounts,
    'Checking account': checking_account,
    'Credit amount': credit_amount,
    'Duration': duration,
    'Purpose': purpose
}

# Convert to DataFrame for prediction
input_df = pd.DataFrame([input_data])

# Apply both Logistic Regression model pipelines for prediction
input_df['Model_1_Prediction'] = logreg_pipeline_1.predict(input_df)
input_df['Model_2_Prediction'] = logreg_pipeline_2.predict(input_df)

# Map the predictions to 'Good'/'Bad' labels for both models
input_df['Model_1_Prediction_Label'] = input_df['Model_1_Prediction'].map({0: 'Good', 1: 'Bad'})
input_df['Model_2_Prediction_Label'] = input_df['Model_2_Prediction'].map({0: 'Good', 1: 'Bad'})

# Ensemble Model (Majority Voting)
input_df['Ensemble_Prediction'] = input_df[['Model_1_Prediction', 'Model_2_Prediction']].mode(axis=1)[0]
input_df['Ensemble_Prediction_Label'] = input_df['Ensemble_Prediction'].map({0: 'Good', 1: 'Bad'})

# Display all user inputs along with the predictions
st.subheader('User Input and Model Predictions')

st.write(f"### Provided Information")
st.write(input_data)

# Show the predictions for both models and the ensemble
st.write(f"### Predictions by the Models")
st.write(input_df[['Age', 'Purpose', 'Credit amount', 'Job', 
                   'Model_1_Prediction_Label', 'Model_2_Prediction_Label', 
                   'Ensemble_Prediction_Label']])

# Display the final decision with reasoning
st.subheader('Credit Decision and Reasoning')

# Check if the ensemble prediction is 'Bad'
if input_df['Ensemble_Prediction_Label'].iloc[0] == 'Bad':
    st.write("### Reason for Rejection:")
    # Explain why the application was rejected
    st.write("- The credit risk is high based on the models' predictions.")
    st.write("- Both models or at least one model predicts the application as 'Bad'.")
    st.write("- Factors contributing to rejection could be:")
    st.write(f"  - Age: {age} (Age might be considered high or low for loan approval)")
    st.write(f"  - Credit Amount: {credit_amount} (The requested amount might be too high for the current financial profile)")
    st.write(f"  - Job: {job} (Job stability can influence approval chances)")
    st.write(f"  - Purpose: {purpose} (Certain purposes like 'new car' may carry higher risk)")
    st.write("- Please review the input information for possible improvements.")

else:
    # If the decision is 'Good'
    st.write("### Reason for Acceptance:")
    # Explain why the application was accepted
    st.write("- The credit risk is deemed acceptable by both models or through majority voting.")
    st.write("- Both models or at least one model predicts the application as 'Good'.")
    st.write("- Factors contributing to approval could be:")
    st.write(f"  - Age: {age} (The age is within a reasonable range for credit approval)")
    st.write(f"  - Credit Amount: {credit_amount} (The requested amount aligns with the financial profile)")
    st.write(f"  - Job: {job} (A stable job increases the likelihood of approval)")
    st.write(f"  - Purpose: {purpose} (Purpose such as 'education' might be favored)")
    st.write("- Your credit application is approved based on these factors!")
