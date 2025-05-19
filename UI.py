import streamlit as st 
import joblib 
def loading_model(): 
    m=joblib.load(r"C:\Users\HP\Documents\NareshIT\ML_PipeLine\PipeLine\model_file\lr_model.joblib") 
    st.session_state.model=m 
@st.fragment 
def header(): 
    st.title(":orange[Wine Quality Model Prediction]") 
 
@st.fragment 
def Creating_input_field(): 
    with st.form(key="wine_form"): 
        st.number_input("fixed acidity",value=None,key="acidity") 
        st.number_input("residual sugar",value=None,key="suger") 
        st.number_input("free sulfur dioxide",value=None,key="sulpher") 
        st.number_input("total sulfur dioxide",value=None,key="T_sulpher") 
        st.number_input("alcohol",value=None,key="alcohol") 
        predict_BTN=st.form_submit_button("Predict") 
 
        if predict_BTN: 
            acid=st.session_state.acidity 
            suger=st.session_state.suger 
            sul=st.session_state.sulpher 
            t_sul=st.session_state.T_sulpher 
            alco=st.session_state.alcohol 
            user_data=[[acid,suger,sul,t_sul,alco]] 
            lr_model=st.session_state.model 
            pred=lr_model.predict(user_data) 
            st.success(f"Wine quality is {pred[0]}") 
   
loading_model() 
header() 
Creating_input_field()