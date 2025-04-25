
import streamlit as st
from chatbot_logic import get_response

st.set_page_config(page_title="ArayuBot", page_icon="🌿")

st.title("🤖 ArayuBot - Your Ayurveda Companion")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input
user_input = st.text_input("💬 Ask me anything (Hindi or English):", key="user_input")

if user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append(("🧑‍⚕️ You", user_input))
    st.session_state.chat_history.append(("🌿 ArayuBot", response))

# Display conversation
for speaker, msg in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {msg}")
