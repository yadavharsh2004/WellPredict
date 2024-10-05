import streamlit as st
import pandas as pd
import numpy as np


def user_profile():
    user_name = "Yatharth Singh"
    age = 19
    start_date = "2024-10-05"
    health_metrics = {
        'Date': pd.date_range(start=start_date, periods=12, freq='M'),
        'BMI': np.random.uniform(22, 28, size=12),
        'Blood Pressure': np.random.uniform(120, 140, size=12),
        'Exercise Frequency': np.random.randint(0, 7, size=12),
        'Diabetes': np.random.uniform(5.0, 9.0, size=12)
    }

    df = pd.DataFrame(health_metrics)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("## Profile Details")
        st.write(f"**Name**: {user_name}")
        st.write(f"**Age**: {age}")
        
        st.write("### Health Records")
        st.write(f"**BMI**: {df['BMI'].iloc[-1]:.2f}")
        st.write(f"**Blood Pressure**: {df['Blood Pressure'].iloc[-1]:.2f} mmHg")
        st.write(f"**Exercise Frequency**: {df['Exercise Frequency'].iloc[-1]} days/week")
        st.write(f"**Diabetes (HbA1c)**: {df['Diabetes'].iloc[-1]:.2f} %")

        st.write("### Recent Diabetes Records")
        st.dataframe(df[['Date', 'Diabetes']].tail(4).set_index('Date'), height=100)

    with col2:
        st.markdown("## Health Progress Over Time")
        
        st.write("### BMI Trend")
        st.line_chart(df[['Date', 'BMI']].set_index('Date'), height=150, use_container_width=True)

        st.write("### Blood Pressure Trend")
        st.line_chart(df[['Date', 'Blood Pressure']].set_index('Date'), height=150, use_container_width=True)
        st.success("Your Stauts has been Improved from Last time...")