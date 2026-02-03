import streamlit as st

st.set_page_config(page_title="EcoLens", page_icon="🌱", layout="wide")

st.title("🌱 EcoLens")

tab_greenscore, tab_chatbot, tab_about = st.tabs(["GreenScore", "AI Chatbot", "About"])

with tab_greenscore:
    st.header("🌿 GreenScore")
    st.write("Scan a product and get a sustainability score.")
    # TODO: put barcode input + scoring UI here

with tab_chatbot:
    st.header("🤖 AI Chatbot")
    st.write("Ask questions about ingredients, claims, and greener alternatives.")
    # TODO: put chatbot UI here

with tab_about:
    st.header("ℹ️ About")
    st.write("Built by **The Quantum Crew** for TISB Hacks.")
    # TODO: put team cards here
