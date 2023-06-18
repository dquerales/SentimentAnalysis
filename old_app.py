import streamlit as st
import joblib

#load model
model = joblib.load(open('Models/pipe_clf_model_checkpoint.joblib', 'rb'))
model_clf = model['pipeline_clf']

#app title
st.title('Sentiment Analysis')

#input
text = st.text_input('Write your text review:')

#predict
if st.button('Predict Sentiment', use_container_width=True):
    prediction = model_clf.predict([text])
    if prediction == 1:
        output = 'Positive'
    else:
        output = 'Negative' 
    st.success(f'The predicted sentiment is {output}')

with st.sidebar:
    st.subheader('About')
    st.markdown('Made by [Daniel Querales](https://www.linkedin.com/in/danielquerales/)')
