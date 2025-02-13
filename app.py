import os
import streamlit as st
import pickle
from streamlit_option_menu import option_menu
st.set_page_config(page_title = 'Prediction Of Disease Outbreaks',
                   layout = 'wide',
                   page_icon= 'doctor'
                   )


diabetes_model = pickle.load(open(r"C:\Users\KUMUD SHARMA\OneDrive\Desktop\prediction_of_disease_outbreaks\training_models\diabetes_predicton_model.sav",'rb'))
heart_model = pickle.load(open(r"C:\Users\KUMUD SHARMA\OneDrive\Desktop\prediction_of_disease_outbreaks\training_models\heartdisease_predicton_model.sav" , 'rb'))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreak systen' ,
                           ['Diabetes Prediction', 'Heart Disease Prediction' , 'Parkinsons Prediction'],
                           menu_icon = 'hospital-fill' , icons = ['activity', 'heart' , 'person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('number Of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose_level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value') 
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value ')
    with col1:
        DiabetesPedigreeFFunction = st.text_input('Diabtes Pedigree Function')
    with col2:
        Age = st.text_input('Age Of Person')



diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    user_input = [Pregnancies , Glucose , Bloodpressure , SkinThickness,Insulin,BMI,DiabetesPedigreeFFunction,Age]
    user_input = [float(x) for x in user_input]
    diab_prediction = diabetes_model.predict([user_input])
    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)