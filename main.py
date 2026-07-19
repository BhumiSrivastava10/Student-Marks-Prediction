import streamlit as st
import joblib

st.title("Student Marks Predictor !")
sh=st.number_input("Enter study hours")
btn=st.button("Predict!!")
if btn:
    if sh>=4 and sh<=12 :
        model=joblib.load("smp.pkl")
        res=model.predict([[sh]])[0][0].round(2)
        st.success(f"Predicted Marks:{res}")
    else:
        st.warning("Invalid Input")
        