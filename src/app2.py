import streamlit as st
import pickle

#load model
with open('src/model/model.pkl', 'rb') as fp:
    model = pickle.load(fp)

st.set_page_config(page_title="Sentiment Analysis App", page_icon="🤡")
st.title('🤡 Text Sentiment Analysis')
text = st.text_input('📝 Write your text:')

#predict
if st.button('Predict Sentiment', use_container_width=True):
    prediction = model.predict([text])
    if prediction == 1:
        output = '😀 Positive'
    else:
        output = '😓 Negative' 
    st.success(f'The predicted sentiment is {output}')

with st.sidebar:
    st.subheader('About')
    st.markdown('Made by [Daniel Querales](https://www.linkedin.com/in/danielquerales/)')
