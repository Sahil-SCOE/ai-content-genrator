import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Content Generator", page_icon="✍️")
st.title("✍️ Automated AI Content Generator")
st.markdown("**Built by Sahil Shaikh**")

api_key = st.text_input("Enter OpenAI API Key", type="password")

if api_key:
    client = OpenAI(api_key=api_key)

    content_type = st.selectbox("What do you want to generate?", 
        ["Blog Post", "LinkedIn Post", "YouTube Script", "Twitter Thread", "Email Newsletter"])

    topic = st.text_input("Enter Topic / Title")
    audience = st.text_input("Target Audience (optional)", "General Audience")
    tone = st.selectbox("Tone", ["Professional", "Casual", "Funny", "Inspirational", "Technical"])

    if st.button("Generate Content"):
        if topic:
            with st.spinner("Generating amazing content..."):
                prompt = f"""
                Write a high-quality {content_type} about "{topic}".
                Target Audience: {audience}
                Tone: {tone}
                Make it engaging, well-structured and valuable.
                """

                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.8
                )
                
                st.subheader(f"Generated {content_type}")
                st.write(response.choices[0].message.content)
        else:
            st.error("Please enter a topic")