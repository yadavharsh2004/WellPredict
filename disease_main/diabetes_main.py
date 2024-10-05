import streamlit as st
import pickle
import os

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/../saved_models/diabetes.pkl', 'rb'))

def diabetes():

    NewBMI_Overweight=0
    NewBMI_Underweight=0
    NewBMI_Obesity_1=0
    NewBMI_Obesity_2=0 
    NewBMI_Obesity_3=0
    NewInsulinScore_Normal=0 
    NewGlucose_Low=0
    NewGlucose_Normal=0 
    NewGlucose_Overweight=0
    NewGlucose_Secret=0
    

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", step=1)
    with col2:
        Glucose = st.number_input("Glucose Level", step=1)
    with col3:
        BloodPressure = st.number_input("Blood Pressure", step=1)
    with col1:
        SkinThickness = st.number_input("Skin Thickness", step=1)
    with col2:
        Insulin = st.number_input("Insulin", step=1)
    with col3:
        BMI = st.number_input("BMI", step=0.1)
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", step=0.01)
    with col2:
        Age = st.number_input("Age", step=1)
    
    # Add state handling for button clicks
    if st.button("Diabetes Test Result"):
        # Logic to handle inputs and predictions
        if float(BMI) <= 18.5:
            NewBMI_Underweight = 1
        elif 18.5 < float(BMI) <= 24.9:
            pass
        elif 24.9 < float(BMI) <= 29.9:
            NewBMI_Overweight = 1
        elif 29.9 < float(BMI) <= 34.9:
            NewBMI_Obesity_1 = 1
        elif 34.9 < float(BMI) <= 39.9:
            NewBMI_Obesity_2 = 1
        elif float(BMI) > 39.9:
            NewBMI_Obesity_3 = 1

        if 16 <= float(Insulin) <= 166:
            NewInsulinScore_Normal = 1

        if float(Glucose) <= 70:
            NewGlucose_Low = 1
        elif 70 < float(Glucose) <= 99:
            NewGlucose_Normal = 1
        elif 99 < float(Glucose) <= 126:
            NewGlucose_Overweight = 1
        elif float(Glucose) > 126:
            NewGlucose_Secret = 1

        # Prepare input
        user_input = [
            Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI,
            DiabetesPedigreeFunction, Age, NewBMI_Underweight, NewBMI_Overweight,
            NewBMI_Obesity_1, NewBMI_Obesity_2, NewBMI_Obesity_3, NewInsulinScore_Normal,
            NewGlucose_Low, NewGlucose_Normal, NewGlucose_Overweight, NewGlucose_Secret
        ]

        # Make prediction
        prediction = diabetes_model.predict([user_input])
        diabetes_result = "The person has diabetes" if prediction[0] == 1 else "The person does not have diabetes"
        
        # Display result
        st.success(diabetes_result)
