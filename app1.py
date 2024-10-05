import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

# Import other files
from disease_main import kidney_main, heart_main, diabetes_main, Diabetes_general, Heart_general, Kidney_general, Doctor_general
from Profile import user_profile
from chatbot_folder.streamlit_chatbot_interface_main import chatbot
from report_ocr_folder import report_ocr_app

# Check if user is logged in, if not, show login page
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False  # Default to not logged in

# If user is not logged in, show the login page
if not st.session_state['logged_in']:
    st.write("Please log in to access the application.")
else:
    st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="")

    working_dir = os.path.dirname(os.path.abspath(__file__))

    # Load model
    diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes.pkl', 'rb'))

    # Sidebar menu for navigation
    with st.sidebar:
        selected = option_menu("Multiple Disease Prediction", 
                               ['Profile',
                                'Report Uploader',
                                'Diabetes Prediction',
                                'Heart Disease Prediction',
                                'Kidney Disease Prediction',
                                'Doctor Consultancy',
                                'Chat Bot'
                                ],
                               menu_icon='hospital-fill',
                               icons=['person', 'report', 'activity', 'heart', 'person', 'person', 'person'],
                               default_index=0)

    # Handle selected option
    if selected == 'Profile':
        user_profile()

    elif selected == 'Report Uploader':
        report_ocr_app.report_uploader()

    elif selected == 'Diabetes Prediction':
        Diabetes_general.diabetes_general()
        with st.expander('Additional Info'):
            diabetes_main.diabetes()

    elif selected == 'Heart Disease Prediction':
        Heart_general.heart_gen()
        with st.expander('Additional Info'):
            heart_main.heart()

    elif selected == 'Kidney Disease Prediction':
        Kidney_general.kidney_gen()
        with st.expander('Additional Info'):
            kidney_main.kidney()

    elif selected == 'Doctor Consultancy':
        Doctor_general.doctor_general()

    elif selected == 'Chat Bot':
        chatbot.chat_bot()
