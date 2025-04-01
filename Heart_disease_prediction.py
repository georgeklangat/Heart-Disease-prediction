# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 15:01:06 2025

@author: Georges Lang'at
"""

# Import necessary libraries
import pickle  # For loading the trained model
import streamlit as st  # For building the web app
from streamlit_option_menu import option_menu


# Load the saved model
heart_disease_model = pickle.load(open('E:/GEORGES DOC/CODING/Coding With PYTHON/Prediction_project/heart_disease_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Heart Disease Prediction System',  # Sidebar title
        ['Heart Disease Prediction'],  
        icons=['heart'], 
        default_index=0
    )

# Main page title
st.title('Heart Disease Prediction Using ML')

# Getting the input data from the user
# Creating columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')

with col2:
    sex = st.text_input('Sex (0 = Female, 1 = Male)')

with col3:
    cp = st.text_input('Chest Pain Type')

with col1:
    trestbps = st.text_input('Resting Blood Pressure')

with col2:
    chol = st.text_input('Serum Cholesterol in mg/dl')

with col3:
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

with col1:
    restecg = st.text_input('Resting Electrocardiographic Results')

with col2:
    thalach = st.text_input('Maximum Heart Rate Achieved')

with col3:
    exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')

with col1:
    oldpeak = st.text_input('ST Depression Induced by Exercise')

with col2:
    slope = st.text_input('Slope of the Peak Exercise ST Segment')

with col3:
    ca = st.text_input('Major Vessels Colored by Fluoroscopy')

with col1:
    thal = st.text_input('Thal: 0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect')

heart_diagnosis = ''
# Creating a button for prediction
if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

st.success(heart_diagnosis)