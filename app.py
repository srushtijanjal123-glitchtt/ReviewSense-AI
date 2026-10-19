
import streamlit as st
import joblib

st.set_page_config(
    page_title="ReviewSense AI",
    page_icon="🍽️"
)


model = joblib.load("reviewsense_svm.pkl")

st.title("🍽️ ReviewSense AI")
st.subheader("Restaurant Review Analysis Using NLP")

st.write(
    "Enter a restaurant review below to predict "
    "whether the sentiment is positive or negative."
)

review = st.text_input(
    "Enter your restaurant review",
    placeholder="The food was delicious and the staff was friendly."
)

if st.button("Analyze Review"):
    if review.strip():
        prediction = model.predict([review])[0]

        if prediction == 1:
            st.success("Positive Review 😊")
        else:
            st.error("Negative Review 😞")
    else:
        st.warning("Please enter a review first.")
