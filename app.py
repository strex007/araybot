import streamlit as st
from chatbot_logic import get_response

st.set_page_config(page_title="ArayuBot", page_icon="🌿")

# Language toggle
language = st.selectbox("Choose Language / भाषा चुनें", ["English", "हिंदी"])

st.image("assets/logo.png", width=100)
st.title("🌿 ArayuBot – Your Ayurvedic Buddy")

# Input from user
query = st.text_input("Enter your symptoms here / अपने लक्षण यहाँ दर्ज करें:")

if st.button("Consult / परामर्श लें"):
    if query:
        response = get_response(query, language)
        st.markdown(response, unsafe_allow_html=True)
    else:
        st.warning("Please enter some symptoms.")
