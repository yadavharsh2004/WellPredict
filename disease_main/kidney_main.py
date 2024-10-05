import streamlit as st
import pickle
import os

working_dir = os.path.dirname(os.path.abspath(__file__))
kidney_disease_model = pickle.load(open(f'{working_dir}/../saved_models/kidney.pkl', 'rb'))

def kidney():

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        age = st.number_input('Age', min_value=0, step=1)
    with col2:
        blood_pressure = st.number_input('Blood Pressure', min_value=0.0, step=0.1)
    with col3:
        specific_gravity = st.number_input('Specific Gravity', min_value=0.0, step=0.1)
    with col4:
        albumin = st.number_input('Albumin', min_value=0.0, step=0.1)
    with col5:
        sugar = st.number_input('Sugar', min_value=0.0, step=0.1)

    with col1:
        red_blood_cells = st.selectbox('Red Blood Cells', ['Normal', 'Abnormal'])  
    with col2:
        pus_cell = st.selectbox('Pus Cell', ['Normal', 'Abnormal'])  
    with col3:
        pus_cell_clumps = st.selectbox('Pus Cell Clumps', ['Yes', 'No']) 
    with col4:
        bacteria = st.selectbox('Bacteria', ['Present', 'Not Present']) 
    with col5:
        blood_glucose_random = st.number_input('Blood Glucose Random', min_value=0.0, step=0.1)

    with col1:
        blood_urea = st.number_input('Blood Urea', min_value=0.0, step=0.1)
    with col2:
        serum_creatinine = st.number_input('Serum Creatinine', min_value=0.0, step=0.1)
    with col3:
        sodium = st.number_input('Sodium', min_value=0.0, step=0.1)
    with col4:
        potassium = st.number_input('Potassium', min_value=0.0, step=0.1)
    with col5:
        haemoglobin = st.number_input('Haemoglobin', min_value=0.0, step=0.1)

    with col1:
        packed_cell_volume = st.number_input('Packed Cell Volume', min_value=0.0, step=0.1)
    with col2:
        white_blood_cell_count = st.number_input('White Blood Cell Count', min_value=0.0, step=0.1)
    with col3:
        red_blood_cell_count = st.number_input('Red Blood Cell Count', min_value=0.0, step=0.1)
    with col4:
        hypertension = st.selectbox('Hypertension', ['Yes', 'No']) 
    with col5:
        diabetes_mellitus = st.selectbox('Diabetes Mellitus', ['Yes', 'No'])
    with col1:
        cad = st.selectbox('coronary_artery_disease', ['Yes','No'])
    with col2:
        appet = st.selectbox('appetite', ['Good', 'Poor'])
    with col3:
        pe = st.selectbox('peda_edema', ['Yes', 'No'])
    with col4:
        aane = st.selectbox('aanemia', ['Yes', 'No'])

    kidney_disease_result = ""
    if st.button("Kidney Disease Test Result"):
        user_input = [
            age,
            blood_pressure,
            specific_gravity,
            albumin,
            sugar,
            1 if red_blood_cells == 'Normal' else 0,
            1 if pus_cell == 'Normal' else 0,
            1 if pus_cell_clumps == 'Yes' else 0,
            1 if bacteria == 'Present' else 0,
            blood_glucose_random,
            blood_urea,
            serum_creatinine,
            sodium,
            potassium,
            haemoglobin,
            packed_cell_volume,
            white_blood_cell_count,
            red_blood_cell_count,
            1 if hypertension == 'Yes' else 0,
            1 if diabetes_mellitus == 'Yes' else 0,
            1 if cad == 'Yes' else 0,
            1 if appet == 'Good' else 0,
            1 if pe == 'Yes' else 0,
            1 if aane == 'Yes' else 0

        ]

        prediction = kidney_disease_model.predict([user_input])
        kidney_disease_result = "The person has kidney disease" if prediction[0] == 1 else "The person does not have kidney disease"

    st.success(kidney_disease_result)