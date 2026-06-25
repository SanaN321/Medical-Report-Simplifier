import streamlit as st
import base64
from groq import Groq

client = Groq(api_key="Enter your Groq Key")

st.title("🏥 Medical Report Simplifier")
st.write("Upload a photo of your medical report and get a simple explanation")

uploaded_file = st.file_uploader("Upload Medical Report Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Report", width=400)
    
    if st.button("Simplify Report"):
        with st.spinner("Analyzing your report..."):
            image_data = base64.b64encode(uploaded_file.read()).decode("utf-8")
            
            response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_data}"
                                }
                            },
                            {
                                "type": "text",
                                "text": """You are a doctor explaining a medical report to a patient 
with no medical background. Look at this medical report image and explain it in simple language.
Structure as: What it means / Why it matters / What to do next."""
                            }
                        ]
                    }
                ]
            )
            
            result = response.choices[0].message.content
            st.success("Here is your simplified report:")
            st.write(result)