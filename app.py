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
    st.info('The data was obtained from: https://www.kaggle.com/ashishpatel26/sentimental-analysis-nlp for educational purposes only.')
    st.markdown('This webapp was made by Daniel Querales (d.querales@gmail.com) using **Streamlit**')
st.sidebar.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=50)
