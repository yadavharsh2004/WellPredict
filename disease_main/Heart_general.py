import streamlit as st


def heart_gen():
    def calculate_bmi(height_cm, weight_kg):
        height_m = height_cm / 100
        return round(weight_kg / (height_m ** 2), 2)

    weights = {
        'smoking_status': {
            'Current Smoker': 3,
            'Former Smoker': 2,
            'Non-Smoker': 0
        },
        'physical_activity': {
            'Sedentary': 3,
            'Light': 2,
            'Moderate': 1,
            'Vigorous': 0
        },
        'unhealthy_foods': {
            'Always': 3,
            'Often': 2,
            'Sometimes': 1,
            'Rarely': 0,
            'Never': 0
        },
        'alcohol_consumption': {
            'Never': 0,
            'Occasionally': 1,
            'Weekly': 2,
            'Daily': 3
        },
        'family_history': {
            'Yes': 2,
            'No': 0
        }
    }

    def predict_disease_risk(smoking_status, physical_activity, unhealthy_foods, height_cm, weight_kg, alcohol_consumption, family_history):
        bmi = calculate_bmi(height_cm, weight_kg)
        
        if bmi < 18.5:
            bmi_weight = 1
        elif 18.5 <= bmi < 24.9:
            bmi_weight = 0
        elif 25 <= bmi < 29.9:
            bmi_weight = 2
        else:
            bmi_weight = 3
        
        risk_score = (
            weights['smoking_status'][smoking_status] +
            weights['physical_activity'][physical_activity] +
            weights['unhealthy_foods'][unhealthy_foods] +
            bmi_weight +
            weights['alcohol_consumption'][alcohol_consumption] +
            weights['family_history'][family_history]
        )
        
        if risk_score <= 5:
            risk_category = "Safe"
            message = "You are fit! Keep up the good work."
        elif 6 <= risk_score <= 11:
            risk_category = "Moderate Risk"
            message = "Consult a healthcare professional for personalized advice."
        else:
            risk_category = "High Risk"
            message = "It's advisable to consult a doctor for further evaluation."

        return risk_category, message

    st.title("Heart Disease Risk Predictor")

    col1, col2, col3 = st.columns(3)

    with col1:
        height_cm = st.number_input('Height (cm)', min_value=50, max_value=250, value=175)

    with col2:
        weight_kg = st.number_input('Weight (kg)', min_value=10, max_value=200, value=75)

    with col3:
        alcohol_consumption = st.selectbox('Alcohol Consumption', options=['Select', 'Never', 'Occasionally', 'Weekly', 'Daily'], index=0)

    col4, col5, col6 = st.columns(3)

    with col4:
        smoking_status = st.selectbox('Smoking Status', options=['Select', 'Current Smoker', 'Former Smoker', 'Non-Smoker'], index=0)

    with col5:
        physical_activity = st.selectbox('Physical Activity', options=['Select', 'Sedentary', 'Light', 'Moderate', 'Vigorous'], index=0)

    with col6:
        unhealthy_foods = st.selectbox('Unhealthy Foods Frequency', options=['Select', 'Always', 'Often', 'Sometimes', 'Rarely', 'Never'], index=0)

    family_history = st.selectbox('Family History of Heart Disease', options=['Select', 'Yes', 'No'], index=0)

    if st.button("Predict Risk"):
        if all(input != 'Select' for input in [smoking_status, physical_activity, unhealthy_foods, alcohol_consumption, family_history]):
            risk_category, message = predict_disease_risk(
                smoking_status,
                physical_activity,
                unhealthy_foods,
                height_cm,
                weight_kg,
                alcohol_consumption,
                family_history
            )
            
            st.write(f"Risk Category: {risk_category}")
            st.write(message)
        else:
            st.warning("Please select all options before predicting the risk.")
