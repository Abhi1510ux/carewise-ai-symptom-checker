import streamlit as st
import google.generativeai as genai

# Configure Google Gemini API Key
genai.configure(api_key="AIzaSyDqAaXNuHHLXM_xLpI-Wi97vkuezmqnr6A")

# Load Gemini Model
model = genai.GenerativeModel("gemini-pro")

# Streamlit App UI
st.set_page_config(page_title="CareWise: AI Symptom Checker", layout="centered")
st.title("🤖 CareWise: AI Symptom Checker & Treatment Advisor")
st.write("Enter your symptoms below, and AI will analyze possible diseases and treatments.")

# User Input
user_input = st.text_area("Describe your symptoms:", placeholder="E.g., fever, headache, fatigue")

# Process Input and Generate AI Response
if st.button("Analyze Symptoms"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter symptoms before analyzing.")
    else:
        with st.spinner("Analyzing symptoms... 🔍"):
            try:
                prompt = f"User Symptoms: {user_input}. What are possible diseases and treatments?"
                response = model.generate_content(prompt)
                st.subheader("🩺 Possible Conditions & Treatments")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown("---")
st.write("🚀 Powered by Google Gemini AI | Built for the Hackathon")

