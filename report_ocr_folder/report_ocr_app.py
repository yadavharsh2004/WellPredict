# import streamlit as st
# from PIL import Image
# import pytesseract
# import re

# # If you're using Windows, you need to specify the tesseract executable path
# # Uncomment the following line and modify the path accordingly
# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# # Streamlit App Title
# st.title("OCR for Medical Reports")

# # File uploader to upload a medical report image
# uploaded_file = st.file_uploader("Upload a medical report", type=['png', 'jpg', 'jpeg'])

# def extract_info(text):
#     # Extracting Name (assuming it's on top of the report and starts with "Name" or "Patient")
#     name = re.search(r"Name[:\s]*(\w+\s\w+)", text)
    
#     # Extracting Age (look for patterns like "Age: XX" or "Age XX")
#     age = re.search(r"Age[:\s]*(\d{1,3})", text)
    
#     # Extracting Gender (look for Male/Female or M/F pattern)
#     gender = re.search(r"(Male|Female|M|F)", text, re.IGNORECASE)
    
#     # Extracting Date (common date formats like DD-MM-YYYY or MM/DD/YYYY)
#     date = re.search(r"(\d{2}[\/\-]\d{2}[\/\-]\d{4})", text)
    
#     # Extracting Diagnosis (assuming it appears after the word "Diagnosis" or "Diagnoses")
#     diagnosis = re.search(r"Diagnosis[:\s]*(.*)", text, re.IGNORECASE)
    
#     return {
#         "Name": name.group(1) if name else "Not found",
#         "Age": age.group(1) if age else "Not found",
#         "Gender": gender.group(1) if gender else "Not found",
#         "Date": date.group(1) if date else "Not found",
#         "Diagnosis": diagnosis.group(1) if diagnosis else "Not found"
#     }

# if uploaded_file is not None:
#     # Load the image with PIL
#     image = Image.open(uploaded_file)
    
#     # Display the uploaded image
#     st.image(image, caption="Uploaded Medical Report", use_column_width=True)
    
#     # Extract text from image using pytesseract
#     st.write("Extracting text...")
#     extracted_text = pytesseract.image_to_string(image)
    
#     # Display the extracted text
#     st.text_area("Extracted Text", extracted_text, height=300)
    
#     # Extract specific information
#     info = extract_info(extracted_text)
    
#     st.write("**Extracted Information**")
#     st.write(f"**Name**: {info['Name']}")
#     st.write(f"**Age**: {info['Age']}")
#     st.write(f"**Gender**: {info['Gender']}")
#     st.write(f"**Date**: {info['Date']}")
#     st.write(f"**Diagnosis**: {info['Diagnosis']}")
    
#     # Option to download the extracted information
#     info_text = f"""
#     Name: {info['Name']}
#     Age: {info['Age']}
#     Gender: {info['Gender']}
#     Date: {info['Date']}
#     Diagnosis: {info['Diagnosis']}
#     """
#     st.download_button("Download Extracted Information", info_text, file_name="extracted_info.txt")
# else:
#     st.write("Please upload a medical report to extract text.")















# import streamlit as st
# from PIL import Image
# import pytesseract
# import re
# from datetime import datetime

# # Streamlit App Title
# st.title("OCR for Medical Reports")

# # File uploader to upload a medical report image
# uploaded_file = st.file_uploader("Upload a medical report", type=['png', 'jpg', 'jpeg'])

# def calculate_age(dob):
#     """Calculate age from date of birth."""
#     today = datetime.today()
#     birth_date = datetime.strptime(dob, "%d/%m/%Y")  # Adjust this format to match the date format in the report
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return age

# def extract_info(text):
#     # Extracting Name (assuming it's on top of the report and starts with "Name" or "Patient")
#     name = re.search(r"Name[:\s]*(\w+\s\w+)", text)
    
#     # Extracting Age (look for patterns like "Age: XX" or "Age XX")
#     age = re.search(r"Age[:\s]*(\d{1,3})", text)
    
#     # Extracting Gender (look for Male/Female or M/F pattern)
#     gender = re.search(r"(Male|Female|M|F)", text, re.IGNORECASE)
    
#     # Extracting Date (common date formats like DD-MM-YYYY or MM/DD/YYYY)
#     date = re.search(r"(\d{2}[\/\-]\d{2}[\/\-]\d{4})", text)
    
#     # Extracting Date of Birth (DOB) - common formats like "DOB: DD/MM/YYYY"
#     dob = re.search(r"DOB[:\s]*(\d{2}[\/\-]\d{2}[\/\-]\d{4})", text)
    
#     # Extracting Diagnosis (assuming it appears after the word "Diagnosis" or "Diagnoses")
#     diagnosis = re.search(r"Diagnosis[:\s]*(.*)", text, re.IGNORECASE)
    
#     # Extracting Report or Summary (assuming it starts with "Report" or "Summary" and goes till the end)
#     report = re.search(r"(Report|Summary)[:\s]*(.*)", text, re.IGNORECASE | re.DOTALL)

#     # If age is not found but DOB is found, calculate age from DOB
#     calculated_age = None
#     if not age and dob:
#         calculated_age = calculate_age(dob.group(1))
    
#     return {
#         "Name": name.group(1) if name else "Not found",
#         "Age": age.group(1) if age else (str(calculated_age) if calculated_age else "Not found"),
#         "Gender": gender.group(1) if gender else "Not found",
#         "Date": date.group(1) if date else "Not found",
#         "DOB": dob.group(1) if dob else "Not found",
#         "Diagnosis": diagnosis.group(1) if diagnosis else "Not found",
#         "Report/Summary": report.group(2) if report else "Not found"
#     }

# if uploaded_file is not None:
#     # Load the image with PIL
#     image = Image.open(uploaded_file)
    
#     # Display the uploaded image
#     st.image(image, caption="Uploaded Medical Report", use_column_width=True)
    
#     # Extract text from image using pytesseract
#     st.write("Extracting text...")
#     extracted_text = pytesseract.image_to_string(image)
    
#     # Display the extracted text
#     st.text_area("Extracted Text", extracted_text, height=300)
    
#     # Extract specific information
#     info = extract_info(extracted_text)
    
#     st.write("**Extracted Information**")
#     st.write(f"**Name**: {info['Name']}")
#     st.write(f"**Age**: {info['Age']}")
#     st.write(f"**Gender**: {info['Gender']}")
#     st.write(f"**Date**: {info['Date']}")
#     st.write(f"**DOB**: {info['DOB']}")
#     st.write(f"**Diagnosis**: {info['Diagnosis']}")
#     st.write(f"**Report/Summary**: {info['Report/Summary']}")
    
#     # Option to download the extracted information
#     info_text = f"""
#     Name: {info['Name']}
#     Age: {info['Age']}
#     Gender: {info['Gender']}
#     Date: {info['Date']}
#     DOB: {info['DOB']}
#     Diagnosis: {info['Diagnosis']}
#     Report/Summary: {info['Report/Summary']}
#     """
#     st.download_button("Download Extracted Information", info_text, file_name="extracted_info.txt")
# else:
#     st.write("Please upload a medical report to extract text.")















# import streamlit as st
# from PIL import Image
# import pytesseract
# import re
# from datetime import datetime
# import fitz  # PyMuPDF for handling PDF files

# # Streamlit App Title
# st.title("OCR for Medical Reports (Images and PDFs)")

# # File uploader to upload a medical report image or PDF
# uploaded_file = st.file_uploader("Upload a medical report (image or PDF)", type=['png', 'jpg', 'jpeg', 'pdf'])

# def calculate_age(dob):
#     """Calculate age from date of birth."""
#     today = datetime.today()
#     birth_date = datetime.strptime(dob, "%d/%m/%Y")  # Adjust this format to match the date format in the report
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return age

# def extract_info(text):
#     # Extracting Name (assuming it's on top of the report and starts with "Name" or "Patient")
#     name = re.search(r"Name[:\s]*(\w+\s\w+)", text)
    
#     # Extracting Age (look for patterns like "Age: XX" or "Age XX")
#     age = re.search(r"Age[:\s]*(\d{1,3})", text)
    
#     # Extracting Gender (look for Male/Female or M/F pattern)
#     gender = re.search(r"(Male|Female|M|F)", text, re.IGNORECASE)
    
#     # Extracting Date (common date formats like DD-MM-YYYY or MM/DD/YYYY)
#     date = re.search(r"(\d{2}[\/\-]\d{2}[\/\-]\d{4})", text)
    
#     # Extracting Date of Birth (DOB) - common formats like "DOB: DD/MM/YYYY"
#     dob = re.search(r"DOB[:\s]*(\d{2}[\/\-]\d{2}[\/\-]\d{4})", text)
    
#     # Extracting Diagnosis (assuming it appears after the word "Diagnosis" or "Diagnoses")
#     diagnosis = re.search(r"Diagnosis[:\s]*(.*)", text, re.IGNORECASE)
    
#     # Extracting Report or Summary (assuming it starts with "Report" or "Summary" and goes till the end)
#     report = re.search(r"(Report|Summary)[:\s]*(.*)", text, re.IGNORECASE | re.DOTALL)

#     # If age is not found but DOB is found, calculate age from DOB
#     calculated_age = None
#     if not age and dob:
#         calculated_age = calculate_age(dob.group(1))
    
#     return {
#         "Name": name.group(1) if name else "Not found",
#         "Age": age.group(1) if age else (str(calculated_age) if calculated_age else "Not found"),
#         "Gender": gender.group(1) if gender else "Not found",
#         "Date": date.group(1) if date else "Not found",
#         "DOB": dob.group(1) if dob else "Not found",
#         "Diagnosis": diagnosis.group(1) if diagnosis else "Not found",
#         "Report/Summary": report.group(2) if report else "Not found"
#     }

# def extract_text_from_pdf(uploaded_file):
#     """Extract text from PDF file using PyMuPDF (fitz)."""
#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = ""
#     for page in doc:
#         text += page.get_text("text")
#     return text

# if uploaded_file is not None:
#     if uploaded_file.type in ['image/png', 'image/jpeg', 'image/jpg']:
#         # Load the image with PIL
#         image = Image.open(uploaded_file)
        
#         # Display the uploaded image
#         st.image(image, caption="Uploaded Medical Report", use_column_width=True)
        
#         # Extract text from image using pytesseract
#         st.write("Extracting text from image...")
#         extracted_text = pytesseract.image_to_string(image)
#     elif uploaded_file.type == 'application/pdf':
#         # Extract text from PDF
#         st.write("Extracting text from PDF...")
#         extracted_text = extract_text_from_pdf(uploaded_file)
#     else:
#         st.error("Unsupported file type.")
#         extracted_text = ""

#     if extracted_text:
#         # Display the extracted text
#         st.text_area("Extracted Text", extracted_text, height=300)
        
#         # Extract specific information
#         info = extract_info(extracted_text)
        
#         st.write("**Extracted Information**")
#         st.write(f"**Name**: {info['Name']}")
#         st.write(f"**Age**: {info['Age']}")
#         st.write(f"**Gender**: {info['Gender']}")
#         st.write(f"**Date**: {info['Date']}")
#         st.write(f"**DOB**: {info['DOB']}")
#         st.write(f"**Diagnosis**: {info['Diagnosis']}")
#         st.write(f"**Report/Summary**: {info['Report/Summary']}")
        
#         # Option to download the extracted information
#         info_text = f"""
#         Name: {info['Name']}
#         Age: {info['Age']}
#         Gender: {info['Gender']}
#         Date: {info['Date']}
#         DOB: {info['DOB']}
#         Diagnosis: {info['Diagnosis']}
#         Report/Summary: {info['Report/Summary']}
#         """
#         st.download_button("Download Extracted Information", info_text, file_name="extracted_info.txt")
# else:
#     st.write("Please upload a medical report to extract text.")



import streamlit as st
from PIL import Image
import pytesseract
import re
from datetime import datetime
import fitz  # PyMuPDF for handling PDF files
import os
import pickle

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/../saved_models/diabetes.pkl', 'rb'))


def report_uploader():
    # Streamlit App Title
    st.title("OCR for Medical Reports (Images and PDFs)")

    # File uploader to upload a medical report image or PDF
    uploaded_file = st.file_uploader("Upload a medical report (image or PDF)", type=['png', 'jpg', 'jpeg', 'pdf'])

    def extract_factors(text):
        """Extract specific medical factors from text."""
        factors = {}
        
        # Extract Number of Pregnancies
        pregnancies = re.search(r"(?:Pregnancies|Number of Pregnancies)[:\s]*(\d+)", text, re.IGNORECASE)
        factors['Number of Pregnancies'] = pregnancies.group(1) if pregnancies else "Not found"
        
        # Extract Skin Thickness
        skin_thickness = re.search(r"(?:Skin Thickness)[:\s]*(\d+)", text, re.IGNORECASE)
        factors['Skin Thickness'] = skin_thickness.group(1) if skin_thickness else "Not found"
        
        # Extract Diabetes Pedigree Function
        diabetes_pedigree = re.search(r"(?:Diabetes Pedigree Function)[:\s]*([\d.]+)", text, re.IGNORECASE)
        factors['Diabetes Pedigree Function'] = diabetes_pedigree.group(1) if diabetes_pedigree else "Not found"
        
        # Extract Glucose Level
        glucose = re.search(r"(?:Glucose Level|Glucose)[:\s]*(\d+)", text, re.IGNORECASE)
        factors['Glucose Level'] = glucose.group(1) if glucose else "Not found"
        
        # Extract Insulin
        insulin = re.search(r"(?:Insulin)[:\s]*(\d+)", text, re.IGNORECASE)
        factors['Insulin'] = insulin.group(1) if insulin else "Not found"
        
        # Extract Age
        age = re.search(r"Age[:\s]*(\d{1,3})", text)
        factors['Age'] = age.group(1) if age else "Not found"
        
        # Extract Blood Pressure
        bp = re.search(r"(?:Blood Pressure|BP)[:\s]*(\d+/\d+|\d+)", text, re.IGNORECASE)
        factors['Blood Pressure'] = bp.group(1) if bp else "Not found"
        
        # Extract BMI
        bmi = re.search(r"(?:BMI|Body Mass Index)[:\s]*([\d.]+)", text, re.IGNORECASE)
        factors['BMI'] = bmi.group(1) if bmi else "Not found"

        return factors

    def extract_text_from_pdf(uploaded_file):
        """Extract text from PDF file using PyMuPDF (fitz)."""
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text("text")
        return text

    if uploaded_file is not None:
        if uploaded_file.type in ['image/png', 'image/jpeg', 'image/jpg']:
            # Load the image with PIL
            image = Image.open(uploaded_file)
            
            # Display the uploaded image
            st.image(image, caption="Uploaded Medical Report", use_column_width=True)
            
            # Extract text from image using pytesseract
            st.write("Extracting text from image...")
            extracted_text = pytesseract.image_to_string(image)
        elif uploaded_file.type == 'application/pdf':
            # Extract text from PDF
            st.write("Extracting text from PDF...")
            extracted_text = extract_text_from_pdf(uploaded_file)
        else:
            st.error("Unsupported file type.")
            extracted_text = ""

        if extracted_text:
            # Display the extracted text
            st.text_area("Extracted Text", extracted_text, height=300)
            
            # Extract specific medical factors
            factors = extract_factors(extracted_text)
            
            st.write("**Extracted Medical Factors**")
            for factor, value in factors.items():
                st.write(f"**{factor}**: {value}")
            
            # Option to download the extracted factors
            factors_text = "\n".join([f"{factor}: {value}" for factor, value in factors.items()])
            if st.button("Diabetes Test Result"):
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


                all_values = list(factors.values())
                user_value_for_prediction = []
                user_value_for_prediction.append(all_values[0]) #Number of Pregnancies
                user_value_for_prediction.append(all_values[3]) #Glucose Level
                user_value_for_prediction.append(all_values[6]) #Blood Pressure
                user_value_for_prediction.append(all_values[1]) #Skin Thickness
                user_value_for_prediction.append(all_values[4]) #Insulin
                user_value_for_prediction.append(all_values[7]) #BMI
                user_value_for_prediction.append(all_values[2]) #Diabetes Pedigree Function
                user_value_for_prediction.append(all_values[5]) #Age


                if float(all_values[7]) <= 18.5:
                    NewBMI_Underweight = 1
                elif 18.5 < float(all_values[7]) <= 24.9:
                    pass
                elif 24.9 < float(all_values[7]) <= 29.9:
                    NewBMI_Overweight = 1
                elif 29.9 < float(all_values[7]) <= 34.9:
                    NewBMI_Obesity_1 = 1
                elif 34.9 < float(all_values[7]) <= 39.9:
                    NewBMI_Obesity_2 = 1
                elif float(all_values[7]) > 39.9:
                    NewBMI_Obesity_3 = 1

                if 16 <= float(all_values[4]) <= 166:
                    NewInsulinScore_Normal = 1

                if float(all_values[3]) <= 70:
                    NewGlucose_Low = 1
                elif 70 < float(all_values[3]) <= 99:
                    NewGlucose_Normal = 1
                elif 99 < float(all_values[3]) <= 126:
                    NewGlucose_Overweight = 1
                elif float(all_values[3]) > 126:
                    NewGlucose_Secret = 1
                
                user_value_for_prediction += [NewBMI_Underweight, NewBMI_Overweight,
                NewBMI_Obesity_1, NewBMI_Obesity_2, NewBMI_Obesity_3, NewInsulinScore_Normal,
                NewGlucose_Low, NewGlucose_Normal, NewGlucose_Overweight, NewGlucose_Secret
                ]


                # Make prediction
                prediction = diabetes_model.predict([user_value_for_prediction])
                diabetes_result = "The person has diabetes" if prediction[0] == 1 else "The person does not have diabetes"
                
                # Display result
                if diabetes_result == "The person has diabetes":
                    st.error(diabetes_result)
                else:
                    st.success(diabetes_result)

            st.download_button("Download Extracted Factors", factors_text, file_name="extracted_factors.txt")
    else:
        st.write("Please upload a medical report to extract text.")
