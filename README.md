🚢 Titanic Survival Prediction App

🎯 Predict whether a passenger survived the Titanic disaster using Machine Learning.

This project uses a trained Decision Tree / Random Forest / Logistic Regression model (saved as .pkl) built on the Titanic dataset from Kaggle. It’s deployed as a Streamlit web app for real-time survival prediction based on passenger details.

------------------------------------------------------------
📂 Project Structure
------------------------------------------------------------
📁 Titanic-Survival-Prediction/
├── Titanic.ipynb         -> Jupyter notebook (data analysis + model training)
├── best_model.pkl        -> Trained ML model
├── app.py                -> Streamlit web application
└── README.md             -> Project documentation

------------------------------------------------------------
⚙️ Tech Stack
------------------------------------------------------------
Language: Python
Frontend: Streamlit
ML Libraries: scikit-learn, pandas, numpy
Visualization: matplotlib, seaborn
Serialization: pickle

------------------------------------------------------------
🚀 How to Run Locally
------------------------------------------------------------

1️⃣ Clone this repository:
    git clone https://github.com/your-username/Titanic-Survival-Prediction.git
    cd Titanic-Survival-Prediction

2️⃣ Install dependencies:
    pip install -r requirements.txt

If you don’t have requirements.txt, create it using:
    pip install streamlit scikit-learn pandas numpy matplotlib seaborn
    pip freeze > requirements.txt

3️⃣ Run the Streamlit app:
    streamlit run app.py

Then open the local URL (usually http://localhost:8501).

------------------------------------------------------------
🧠 How It Works
------------------------------------------------------------
1. User enters details:
   - Passenger class (Pclass)
   - Sex (male / female)
   - Age
   - Siblings/Spouses (SibSp)
   - Parents/Children (Parch)
   - Fare
   - Port of Embarkation (C, Q, S)

2. The app encodes inputs numerically.

3. The trained model predicts:
   0 → Did Not Survive
   1 → Survived

4. The app also shows the survival probability.

------------------------------------------------------------
🧩 Sample Prediction
------------------------------------------------------------
Input Example:
  Pclass: 1
  Sex: female
  Age: 25
  SibSp: 0
  Parch: 0
  Fare: 75.5
  Embarked: S

Output:
  🟢 Survived
  💡 Survival Probability: 0.84

------------------------------------------------------------
📊 Model Training Summary
------------------------------------------------------------
- Data Source: Kaggle - Titanic: Machine Learning from Disaster
- Dropped columns: PassengerId, Cabin, Ticket, Name
- Encoded categorical features using LabelEncoder
- Scaled numeric features using StandardScaler
- Models Tested:
  Logistic Regression, Decision Tree, Random Forest, KNN, SVM, XGBoost, LightGBM
- Best model saved as best_model.pkl

------------------------------------------------------------
💻 Deployment Options
------------------------------------------------------------
You can deploy this app easily on:
- Streamlit Cloud → https://share.streamlit.io
- Render → https://render.com
- Hugging Face Spaces → https://huggingface.co/spaces

------------------------------------------------------------
👨‍💻 Developer
------------------------------------------------------------
Developed by: Edison Xavier
LinkedIn: https://www.linkedin.com/in/edisonxavier/
Quote: "Turning data into decisions, one model at a time."
Location: India

------------------------------------------------------------
⭐ Acknowledgments
------------------------------------------------------------
- Kaggle Titanic Dataset
- Streamlit
- scikit-learn

------------------------------------------------------------
🏁 License
------------------------------------------------------------
This project is open-source under the MIT License.
