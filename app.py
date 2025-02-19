import streamlit as st
import google.generativeai as genai
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to fetch and extract text from a webpage
def fetch_webpage_content(url):
    try:
        response = requests.get(url, timeout=10)  # Fetch webpage
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return soup.get_text()  # Extract visible text
        else:
            return f"Failed to fetch the webpage. Status code: {response.status_code}"
    except Exception as e:
        return f"Error fetching webpage: {e}"

# Hardcoded blog link for now (replace with dynamic handling)
blog_url = "https://medium.com/@ravihimalayanwriterml/linear-regression-from-scratch-f19230fc6590"

# Fetch the blog content
blog_content = fetch_webpage_content(blog_url)

# Function to generate chatbot response
def get_gemini_response(input_prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([input_prompt])
        return response.text
    except Exception as e:
        return f"Error generating response from Gemini: {e}"

# Streamlit UI
st.set_page_config(page_title="AI Chatbot")
st.header("AI Chatbot")

if "conversation" not in st.session_state:
    st.session_state.conversation = []

def display_chat():
    for message in st.session_state.conversation:
        if message["role"] == "user":
            st.write(f"**You**: {message['content']}")
        else:
            st.write(f"**Bot**: {message['content']}")

user_message = st.text_input("You: ", "")

if st.button("Send") and user_message:
    st.session_state.conversation.append({"role": "user", "content": user_message})
    
    # Include blog content in chatbot prompt
    input_prompt = f"Based on the following blog content, answer the user's question:\n\n{blog_content}\n\nUser question: {user_message}"
    
    bot_response = get_gemini_response(input_prompt)
    
    if bot_response:
        st.session_state.conversation.append({"role": "bot", "content": bot_response})
    
    display_chat()

if not user_message and not st.session_state.conversation:
    st.write("Welcome to the AI Chatbot! Start the conversation by typing a message above.")
