import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#MongoDB Connection
uri = "mongodb+srv://mdmoazzamali984:amug786@cluster0.jzrdt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Diabetes']
collection = db["Diabetes_pred"]
#load model
@st.cache_resource
def load_model():
    with open("diabetes_lr_final_model.pkl",'rb') as file:
        models,scaler=pickle.load(file)
    return models,scaler

#preprocessing function
def preprocessing_input_data(data,scaler):
    df = pd.DataFrame([data])
    df["SEX"] = df["SEX"].replace({"Male": 1, "Female": 0})  # Convert categorical to numerical
    df_transformed = scaler.transform(df)
    return df_transformed

#prediction function
def predict_data(data,model_name):
    models,scaler=load_model()
    processed_data=preprocessing_input_data(data,scaler)
    if model_name=="Ridge Regression":
        prediction=models["ridge_model1"].predict(processed_data)
    else:
        prediction=models["lasso_model1"].predict(processed_data)
    return prediction

#main streamlit app
def main():
    st.set_page_config(page_title="🔬 Diabetes Predictor", page_icon="🩺", layout="wide")
    st.title("🚀 **AI-Based Diabetes Progression Prediction**")
    st.markdown("🔬 **Using Machine Learning to Estimate Diabetes Progression Over Time**")
    
    #Custom Background Styling
    st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #ffefba, #ffffff);
        }
        div.stButton > button:first-child {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
    )
    # Sidebar Layout
    st.sidebar.header("⚙️ **Configuration**")
    st.sidebar.write("Select the prediction model.")
    model_choice = st.sidebar.radio("Choose Model", ["🤖 Ridge Regression", "🧮 Lasso Regression"])
    st.sidebar.markdown("---") 
    st.sidebar.header("📋 **Patient Data Input**")
    st.sidebar.write("Fill in the details below to predict diabetes progression.")
    age = st.sidebar.slider("🎂 Age of Patient", 18, 80, 25)
    sex = st.sidebar.selectbox("⚤ Sex of Patient", ["Male", "Female"])
    bmi = st.sidebar.slider("⚖️ BMI of Patient", 18.0, 43.0, 25.0)
    bp = st.sidebar.slider("💉 Blood Pressure", 60, 180, 120)
    s1 = st.sidebar.slider("🩸 Total Serum Cholesterol", 90, 400, 200)
    s2 = st.sidebar.slider("🧪 Low-Density Lipoproteins (LDL)", 50, 250, 100)
    s3 = st.sidebar.slider("💊 High-Density Lipoproteins (HDL)", 20, 100, 50)
    s4 = st.sidebar.slider("🔗 Total Cholesterol / HDL Ratio", 1.5, 10.0, 4.5)
    s5 = st.sidebar.slider("🩺 Log of Serum Triglycerides", 3.0, 6.5, 5.2)
    s6 = st.sidebar.slider("🩸 Blood Sugar Level", 50, 600, 99)
    user_data = {
        "AGE": age,
        "SEX": sex,
        "BMI": bmi,
        "BP": bp,
        "S1": s1,
        "S2": s2,
        "S3": s3,
        "S4": s4,
        "S5": s5,
        "S6": s6
    }
    # Predict Button
    if st.button("Predict Score"):
        with st.spinner("🕒 Processing your input... Please wait"):
            time.sleep(2)  # Simulate a loading delay
            model_name="Ridge Regression" if model_choice=="🤖 Ridge Regression" else "Lasso Regression"
            prediction = predict_data(user_data,model_name)
            st.success(f"🎯 The predicted diabetes progression is: {prediction[0]}")
            user_data["Prediction"] = prediction[0]
            for key, value in user_data.items():
                if isinstance(value, np.ndarray):
                    user_data[key] = value.tolist()
            collection.insert_one(user_data)
            st.write("Prediction stored in database!")


if __name__ == "__main__":
    main()