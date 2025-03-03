🔬 AI-Based Diabetes Progression Prediction

📌 Overview

This is a machine learning-powered web application built with Streamlit that predicts diabetes progression over time based on multiple clinical factors such as age, BMI, blood pressure, serum cholesterol, and more. The app utilizes Ridge Regression and Lasso Regression models for prediction and securely stores user input data in MongoDB.

🚀 Features

✅ User-Friendly Interface: Clean and interactive UI with light/dark mode support.
✅ Model Selection: Choose between Ridge Regression and Lasso Regression.
✅ Real-time Predictions: Predict diabetes progression instantly based on input parameters.
✅ Data Visualization: Displays user input data as a professional bar chart.
✅ Secure Data Storage: Saves user predictions in MongoDB for analysis.
✅ Themed UI: Adaptive color scheme based on Streamlit's theme.

🏗️ Installation

Prerequisites
Ensure you have the following installed:

Python 3.8+
pip (Python package manager)
MongoDB Atlas (or a local MongoDB instance)
Steps to Set Up
1️⃣ Clone the repository:

git clone https://github.com/your-repo/diabetes-prediction-app.git
cd diabetes-prediction-app
2️⃣ Create a virtual environment:

python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
3️⃣ Install dependencies:

pip install -r requirements.txt
4️⃣ Set up Streamlit Secrets for MongoDB:

Create a .streamlit/secrets.toml file and add:

[mongodb]
uri = "your_mongodb_connection_string"
database = "your_database_name"
collection = "your_collection_name"
5️⃣ Run the app:

streamlit run app.py
🎯 How to Use

1️⃣ Open the app in your browser after running it.
2️⃣ Select a prediction model from the sidebar.
3️⃣ Enter the patient details (age, sex, BMI, blood pressure, etc.).
4️⃣ Click Predict to generate a diabetes progression score.
5️⃣ View visualized data insights and predictions.
6️⃣ The data is stored in MongoDB for future reference.

📊 Model Details

Ridge Regression: Reduces overfitting by adding an L2 penalty.
Lasso Regression: Feature selection by applying an L1 penalty.
📦 Technologies Used

Frontend & Backend: Streamlit
Machine Learning Models: Scikit-learn
Database: MongoDB
Visualization: Matplotlib, Seaborn
🛠️ Future Enhancements

🚀 Integrate additional machine learning models
📊 Provide explanations using SHAP (SHapley Additive exPlanations)
☁️ Deploy to Streamlit Cloud or Heroku

📜 Disclaimer

🚨 This is a machine learning-based prediction tool and should not be used as a substitute for professional medical advice. Consult a doctor for an accurate clinical assessment.

👨‍💻 Author

Developed by Md Moazzam Ali with ❤️ using Streamlit.

✨ If you like this project, give it a ⭐ on GitHub! ✨

Let me know if you want any more modifications! 🚀
