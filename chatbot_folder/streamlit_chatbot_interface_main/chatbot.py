# from openai import OpenAI
# import streamlit as st
# from dotenv import load_dotenv
# import os
# import shelve

# # # myKey :- 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

# # #gemini api key :- AIzaSyBHo_8h-snWyN0_L6WByQDNvottq10TLpk

# load_dotenv()

# st.title("Streamlit Chatbot Interface")

# USER_AVATAR = "👤"
# BOT_AVATAR = "🤖"
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # Ensure openai_model is initialized in session state
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"


# # Load chat history from shelve file
# def load_chat_history():
#     with shelve.open("chat_history") as db:
#         return db.get("messages", [])


# # Save chat history to shelve file
# def save_chat_history(messages):
#     with shelve.open("chat_history") as db:
#         db["messages"] = messages


# # Initialize or load chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = load_chat_history()

# # Sidebar with a button to delete chat history
# with st.sidebar:
#     if st.button("Delete Chat History"):
#         st.session_state.messages = []
#         save_chat_history([])

# # Display chat messages
# for message in st.session_state.messages:
#     avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
#     with st.chat_message(message["role"], avatar=avatar):
#         st.markdown(message["content"])

# # Main chat interface
# if prompt := st.chat_input("How can I help?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user", avatar=USER_AVATAR):
#         st.markdown(prompt)

#     with st.chat_message("assistant", avatar=BOT_AVATAR):
#         message_placeholder = st.empty()
#         full_response = ""
#         for response in client.chat.completions.create(
#             model=st.session_state["openai_model"],
#             messages=st.session_state["messages"],
#             stream=True,
#         ):
#             full_response += response.choices[0].delta.content or ""
#             message_placeholder.markdown(full_response + "|")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})

# # Save chat history after each interaction
# save_chat_history(st.session_state.messages)

#--------------------------------------------------------------------------------------------------------------------------------------------------------

# from dotenv import load_dotenv
# import streamlit as st
# import os
# import google.generativeai as ggi

# load_dotenv(".env")

# fetcheed_api_key = os.getenv("API_KEY")
# ggi.configure(api_key = fetcheed_api_key)

# model = ggi.GenerativeModel("gemini-pro") 
# chat = model.start_chat()

# def LLM_Response(question):
#     response = chat.send_message(question,stream=True)
#     return response

# st.title("Chat Application using Gemini Pro")

# user_quest = st.text_input("Ask a question:")
# btn = st.button("Ask")

# if btn and user_quest:
#     result = LLM_Response(user_quest)
#     st.subheader("Response : ")
#     for word in result:
#         st.text(word.text)

#--------------------------------------------------------------------------------------------------------------------------------------------------------


# import streamlit as st
# from dotenv import load_dotenv
# import os
# import shelve
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Set up Gemini API key from environment variable
# genai.configure(api_key=os.getenv("API_KEY"))

# st.title("Health Care ChatBot")

# USER_AVATAR = "👤"
# BOT_AVATAR = "🤖"

# # Initialize or load chat history
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# # Sidebar with a button to delete chat history
# with st.sidebar:
#     if st.button("Delete Chat History"):
#         st.session_state.messages = []

# # Display chat messages
# for message in st.session_state.messages:
#     avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
#     with st.chat_message(message["role"], avatar=avatar):
#         st.markdown(message["content"])

# # Function to call the Gemini API
# def get_gemini_response(prompt):
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     response = model.generate_content(prompt)
#     return response.text

# # Main chat interface
# if prompt := st.chat_input("How can I help?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user", avatar=USER_AVATAR):
#         st.markdown(prompt)

#     # Call Gemini API for assistant response
#     with st.chat_message("assistant", avatar=BOT_AVATAR):
#         message_placeholder = st.empty()
#         full_response = get_gemini_response(prompt)
#         message_placeholder.markdown(full_response)

#     st.session_state.messages.append({"role": "assistant", "content": full_response})


#--------------------------------------------------------------------------------------------------------------------------------------------------------


# import streamlit as st
# from dotenv import load_dotenv
# import os
# import shelve
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Set up Gemini API key from environment variable
# genai.configure(api_key=os.getenv("API_KEY"))


# st.title("Health Care ChatBot")
# #🩺
# USER_AVATAR = "👤"
# BOT_AVATAR = "🧑🏻‍⚕️" 

# # Initialize or load chat history
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# # Sidebar with a button to delete chat history
# with st.sidebar:
#     if st.button("Delete Chat History"):
#         st.session_state.messages = []

# # Display chat messages
# for message in st.session_state.messages:
#     avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
#     with st.chat_message(message["role"], avatar=avatar):
#         st.markdown(message["content"])

# # Function to call the Gemini API
# def get_gemini_response(prompt):
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     response = model.generate_content(prompt)
#     return response.text

# # Main chat interface
# if prompt := st.chat_input("How can I help?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user", avatar=USER_AVATAR):
#         st.markdown(prompt)

#     # Call Gemini API for assistant response
#     with st.chat_message("assistant", avatar=BOT_AVATAR):
#         message_placeholder = st.empty()
#         full_response = get_gemini_response(prompt)
#         message_placeholder.markdown(full_response)

#     st.session_state.messages.append({"role": "assistant", "content": full_response})









import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
import wave
import io
import base64

def chat_bot():
    # Load environment variables
    load_dotenv()

    # Set up Gemini API key from environment variable
    genai.configure(api_key=os.getenv("API_KEY"))

    st.title("Health Care ChatBot")
    # 🩺
    USER_AVATAR = "👤"
    BOT_AVATAR = "🧑🏻‍⚕️"

    # Initialize or load chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Sidebar with a button to delete chat history
    with st.sidebar:
        if st.button("Delete Chat History"):
            st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Function to call the Gemini API
    def get_gemini_response(prompt):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text

    # Function to record audio in Python
    def record_audio(duration=3, sample_rate=44100):
        import sounddevice as sd
        audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Wait until recording is finished
        return audio_data

    # Function to convert recorded audio to text using SpeechRecognition
    def audio_to_text(audio_data):
        # Convert numpy array audio to a WAV format in-memory buffer
        audio_io = io.BytesIO()
        wav_file = wave.open(audio_io, 'wb')
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(44100)
        wav_file.writeframes(audio_data)
        wav_file.close()
        audio_io.seek(0)

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_io) as source:
            audio_content = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_content)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand the audio.")
            return None
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")
            return None

    # Microphone button to trigger audio recording
    if st.button("🎤 Record Voice"):
        st.write("Recording...")
        audio_data = record_audio()
        st.write("Recording complete.")
        
        # Convert the audio to text
        text_input = audio_to_text(audio_data)
        
        if text_input:
            # Append user input to chat
            st.session_state.messages.append({"role": "user", "content": text_input})
            
            # Display the user input message
            with st.chat_message("user", avatar=USER_AVATAR):
                st.markdown(text_input)

            # Call Gemini API for assistant response
            with st.chat_message("assistant", avatar=BOT_AVATAR):
                message_placeholder = st.empty()
                full_response = get_gemini_response(text_input)
                message_placeholder.markdown(full_response)

            st.session_state.messages.append({"role": "assistant", "content": full_response})


    # Allow users to input text via text box
    if prompt := st.chat_input("How can I help?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(prompt)

        # Call Gemini API for assistant response
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            message_placeholder = st.empty()
            full_response = get_gemini_response(prompt)
            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})
