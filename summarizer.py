import streamlit as st
from transformers import pipeline

# Initialize the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit App Title
st.title("Text Summarization Tool")

# Text input from user
input_text = st.text_area("Enter your text here:", height=200)

# Summary length settings
max_len = st.slider("Maximum Summary Length", 50, 300, 100)
min_len = st.slider("Minimum Summary Length", 20, 100, 30)

# Button to generate summary
if st.button("Summarize"):
    if input_text.strip():  # Check if text is entered
        summary = summarizer(input_text, max_length=max_len, min_length=min_len, do_sample=False)
        st.subheader("Summarized Text:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
