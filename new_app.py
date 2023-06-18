import streamlit as st
import joblib
from transformers import pipeline

#load model
sentiment_pipeline = pipeline("sentiment-analysis")

#app title
st.title('Sentiment Analysis')

#input
text = st.text_input('Write your text review:')

#predict
if st.button('Predict Sentiment', use_container_width=True):
   st.write(sentiment_pipeline(text))


with st.sidebar:
    st.subheader('About')
    st.markdown('Made by [Daniel Querales](https://www.linkedin.com/in/danielquerales/)')
