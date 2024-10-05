import streamlit as st
import pickle
import os

working_dir = os.path.dirname(os.path.abspath(__file__))

heart_disease_model = pickle.load(open(f'{working_dir}/../saved_models/heart.pkl', 'rb'))


def heart():
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0, step=1)
    with col2:
        sex = st.selectbox("Sex", ["Male", "Female"]) 
    with col3:
        heart_bps = st.number_input("Blood Pressure", min_value=0.0, step=0.1)

    with col1:
        chol = st.number_input("Serum Cholesterol in mg/dl", min_value=0.0, step=0.1)
    with col2:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ["Yes", "No"])  
    with col3:
        heart_rate = st.number_input("Current Heart Rate", min_value=0, step=1)

    with col1:
        exang = st.selectbox('Exercise Induced Angina', ["Yes", "No"])
    with col2:
        oldpeak = st.number_input('ST Depression Induced by Exercise', min_value=0.0, step=0.1)
    with col3:
        slope = st.number_input('Slope of the Peak Exercise ST Segment', min_value=0.0, step=0.1)

    with col1:
        ca = st.number_input('Major Vessels Colored by Fluoroscopy', min_value=0, step=1)
    with col2:
        cp = st.selectbox("Chest Pain Level", [0, 1, 2]) 
    with col3:
        restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2]) 

    with col1:
        thal = st.selectbox('Thal: 0 = Normal; 1 = Fixed Defect; 2 = Reversible Defect', [0, 1, 2])  

    heart_disease_result = ""
    if st.button("Heart Disease Test Result"):
        user_input = [
            age,
            1 if sex == "Male" else 0, 
            heart_bps,
            chol,
            1 if fbs == "Yes" else 0,
            heart_rate,
            1 if exang == "Yes" else 0,  
            float(oldpeak),
            slope,
            ca
        ]

        def change_levels(level):
            if level == 0:
                return [False, False, False]
            elif level == 1:
                return [True, False, False]
            elif level == 2:
                return [True, False, True]
        
        for i in change_levels(cp):
            user_input.append(i)
        
        for i in change_levels(restecg):
            user_input.append(i)
            
        for i in change_levels(thal):
            user_input.append(i)
            
        user_input.pop(-1)

        try:
            prediction = heart_disease_model.predict([user_input])
            heart_disease_result = "This person has heart disease" if prediction[0] == 1 else "This person does not have heart disease"
        except Exception as e:
            heart_disease_result = f"Error during prediction: {str(e)}"

    st.success(heart_disease_result)