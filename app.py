import streamlit as st
from analysis.review_analyzer import analyze_review

# Page config
st.set_page_config(
    page_title="Fake Review Detection",
    
    layout="centered"
)

st.title(" Fake Review Detection System")
st.write(
    "Analyze product reviews to detect potentially **fake or promotional content** "
    "using sentiment analysis and smart heuristics."
)

st.divider()

# Input fields
review_text = st.text_area(
    "Enter the product review",
    placeholder="Type or paste the review here...",
    height=150
)

rating = st.slider(
    "Select the rating",
    min_value=1,
    max_value=5,
    value=5
)

# Analyze button
if st.button("Analyze Review"):
    if review_text.strip() == "":
        st.warning("Please enter a review before analyzing.")
    else:
        result = analyze_review(review_text, rating)

        st.subheader("Result")
        st.json(result)

      
        if result["is_suspicious"]:
            st.error("⚠️ This review looks **suspicious or promotional**.")
        else:
            st.success("✅ This review appears **genuine**.")

st.divider()

st.caption(
    "Built with Python, TextBlob, Pytest, and Streamlit · Fake Review Detection Project"
)
