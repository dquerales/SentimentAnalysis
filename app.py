import streamlit as st
import joblib

#load model
model = joblib.load(open('model/pipe_clf_model_checkpoint.joblib', 'rb'))
model_clf = model['pipeline_clf']

st.set_page_config(page_title="Sentiment Analysis App", page_icon="🤡")

#app title
st.title('🤡 Text Sentiment Analysis')

#input
text = st.text_input('📝 Write your text:')

#predict
if st.button('Predict Sentiment', use_container_width=True):
    prediction = model_clf.predict([text])
    if prediction == 1:
        output = '😀 Positive'
    else:
        output = '😓 Negative' 
    st.success(f'The predicted sentiment is {output}')

with st.sidebar:
    st.subheader('About')
    st.markdown('Made by [Daniel Querales](https://www.linkedin.com/in/danielquerales/)')
