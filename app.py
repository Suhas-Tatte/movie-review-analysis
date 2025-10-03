import streamlit as st
import joblib

#preprocessing function
#Note: we are using a simplified version here.
def preprocess_text(text):
    import re
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+|@\w+|#\w+|[^a-z\s]', '', text)
    words = text.split()
    stop_words = {'the', 'a', 'is', 'in', 'it', 'to', 'and'}
    filtered_words = [word for word in words if word not in stop_words and len(word) > 1]
    return ' '.join(filtered_words)

st.title("Sentiment Analysis App")
st.write("Enter a movie review below and we'll predict its sentiment (positive or negative).")

try:
    #load the trained model and TF-IDF vectorizer
    model = joblib.load('sentiment_model.pkl')
    tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
except Exception as e:
    #'load' error handling
    st.error(f"Error loading model or vectorizer: {e}")
    st.stop()

#input text area
user_input = st.text_area("Enter your review here:")

if st.button("Predict"):
    if user_input:
        #preprocess the user input
        cleaned_input = preprocess_text(user_input)
        #vectorize the input
        vectorized_input = tfidf_vectorizer.transform([cleaned_input])
        #predict sentiment
        prediction = model.predict(vectorized_input)
        #get prediction probability
        prediction_proba = model.predict_proba(vectorized_input)[0]
        #display prediction result
        if prediction[0] == 1:
            st.success("Prediction: Positive Review 👍 (Confidence : {prediction_proba[1]*100:.2f}%)")
        else:
            st.error("Prediction: Negative Review 👎 (Confidence : {prediction_proba[0]*100:.2f}%)")
    else:
        st.warning("Please enter some text to analyze.")