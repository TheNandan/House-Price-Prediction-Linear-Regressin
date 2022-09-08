from optparse import Option
import streamlit as st
import pickle


st.title("🏠 House Price Prediction Web App ")

st.header("Select the ML Model ?")

Options = st.selectbox('Simple / Multi Linear Regression Model',('Simple Linear Regression','Multi Linear Regression'))

if Options == 'Simple Linear Regression':
    st.subheader('You have selected Simple Linear Regression ')
    area = st.slider('Enter Area in Square feet',1000,5000,2200)
    m1 = pickle.load(open("linearmodel.pkl","rb"))
    if st.button('Get Prediction'):
        res = m1.predict([[area]])
        st.balloons()
        st.success(f"Price Prediction is : {res} 🎉")
else :
    st.subheader('You have selected Multi Linear Regression ')
    area = st.slider('Enter Area in Square feet',1000,5000,2200)
    bedroom = st.slider('Enter No of Bedrooms',1,10,2)
    age = st.number_input("Enter the age",21)
    m2 = pickle.load(open('multilinear.pkl','rb'))
    if st.button('Get Prediction'):
        res = m2.predict([[area,bedroom,age]])
        st.snow()
        st.success(f"Price Prediction is : {res}...🎉")
    