Medical Report Simplifier

As we all know, medical language is complex and not understandable to a layperson due to the many medical terms. Which is why we often search for report findings on different platforms. This system is trying to fix this problem.

Model: 

This system used the LLaMA 4 Scout (a vision-capable model) through the Groq API to read the uploaded image and generate meaningful insights. I used Streamlit to build an interface for this system.

Features: 

 - Upload any medical report, such as a JPG or PNG
 - Get a structured explanation of the report: what it means, why it matters, what to do next

Setup

1.	Clone the repository below
    https://github.com/SanaN321/Medical-Report-Simplifier
2.	Install the dependencies
    pip install streamlit groq
3.	Add your Groq API
4.	Now run the app using
    Streamlit run medical.py









