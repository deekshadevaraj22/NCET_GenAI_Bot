import streamlit as st
from groq import Groq

# Page config
st.set_page_config(page_title="PragyanAI Content Generator", layout="wide")

# Title and image
st.title("PragyanAI - Content Generator")
st.image("OIP.jpeg")

# Get GROQ API Key
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# User inputs
product = st.text_input("Product")
audience = st.text_input("Audience")

# Generate Content Button
if st.button("Generate Content"):
    if product and audience:
        prompt = f"Write marketing content for {product} targeting {audience}."
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        
        st.session_state.text = response.choices[0].message.content
    else:
        st.warning("Please enter both Product and Audience")

# Display generated content and download option
if "text" in st.session_state:
    content = st.text_area("Generated Content", st.session_state.text, height=300)
    
    st.download_button(
        label="⬇️ Download as TXT",
        data=content,
        file_name="marketing_copy.txt",
        mime="text/plain"
    )
else:
    st.info("Generate content first")
