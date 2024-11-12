
import joblib
import pandas as pd
import numpy as np
import streamlit as st
import imblearn

Model = joblib.load("Third_Group.pkl")
Inputs = joblib.load("inputs.pkl")

def prediction(Gender,Married,Dependents,Education,Self_Employed,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,LogTotalIncome,LogPaid_Amount_Per_Month,LogIncome_After_Loan):
    df = pd.DataFrame(columns=Inputs)
    df.at[0,"Gender"] = Gender
    df.at[0,"Married"] = Married
    df.at[0,"Dependents"] = Dependents
    df.at[0,"Education"] = Education
    df.at[0,"Self_Employed"] = Self_Employed
    df.at[0,"LoanAmount"] = LoanAmount
    df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    df.at[0,"Credit_History"] = Credit_History
    df.at[0,"Property_Area"] = Property_Area
    df.at[0,"LogTotalIncome"] = LogTotalIncome
    df.at[0,"LogPaid_Amount_Per_Month"] = LogPaid_Amount_Per_Month
    df.at[0,"LogIncome_After_Loan"] = LogIncome_After_Loan
    result = Model.predict(df)[0]
    return result

def Main():
    st.title("Loan Prediction")
    Gender = st.selectbox("Gender",['Male', 'Female'])
    Married = st.selectbox("Married",['No', 'Yes'])
    Dependents = st.selectbox("Dependents",[ '0',  '1',  '2',  '3+'])
    Education = st.selectbox("Education",['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox("Self_Employed",['No', 'Yes'])
    LoanAmount = st.slider("LoanAmount in Thousands",min_value=9.0 , max_value=700.0 , step=1.0,value = 10.0)
    Loan_Amount_Term = st.slider("Loan_Amount_Term",min_value=12.0 , max_value=480.0 , step=1.0,value = 10.0)
    Credit_History = st.selectbox("Credit_History",[1, 0])
    Property_Area = st.selectbox("Property_Area",['Urban', 'Rural', 'Semiurban'])
    ApplicantIncome = st.slider("ApplicantIncome",min_value=0.0 , max_value=81000.0 , step=5.0,value = 500.0)
    CoapplicantIncome = st.slider("CoapplicantIncome",min_value=0.0 , max_value= 41667.0 , step=5.0,value = 500.0)
    Total_Income = ApplicantIncome+CoapplicantIncome
    
    Loan_Amount_by_Month = LoanAmount * 1000 / Loan_Amount_Term
    
    Incomer_per_month_after_loan = ApplicantIncome - Loan_Amount_by_Month
    
    LogTotalIncome = np.log(Total_Income)
    
    LogPaid_Amount_Per_Month = np.log(Loan_Amount_by_Month)
    
    LogIncome_After_Loan = np.log(Incomer_per_month_after_loan)
    
    if st.button("Predict"):
        result = prediction(Gender,Married,Dependents,Education,Self_Employed,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,LogTotalIncome,LogPaid_Amount_Per_Month,LogIncome_After_Loan)
        list_result = ["Rejected" , "Accepted"]
        st.text(f"Your loan is {list_result[result]}")
Main()
