import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# Load the trained model
# -------------------------------
model_path = "best_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="🚢 Titanic Survival Prediction", page_icon="🌊", layout="centered")
st.title("🚢 Titanic Survival Prediction App")
st.write("Enter passenger details below to check survival chances on the Titanic.")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.number_input("Age", min_value=0, max_value=100, value=29)
    sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)

with col2:
    parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
    fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.2)
    embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

# -------------------------------
# Encode categorical variables
# -------------------------------
# Match LabelEncoder’s alphabetical order used during training
sex_mapping = {"female": 0, "male": 1}
embarked_mapping = {"C": 0, "Q": 1, "S": 2}

sex_encoded = sex_mapping[sex]
embarked_encoded = embarked_mapping[embarked]

# -------------------------------
# Prepare Input Data
# -------------------------------
input_data = pd.DataFrame({
    "Pclass": [pclass],
    "Sex": [sex_encoded],
    "Age": [age],
    "SibSp": [sibsp],
    "Parch": [parch],
    "Fare": [fare],
    "Embarked": [embarked_encoded]
})

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Survival"):
    try:
        prediction = model.predict(input_data)
        result = "🟢 Survived" if prediction[0] == 1 else "🔴 Did Not Survive"
        st.success(f"Prediction Result: {result}")

        # Display model confidence
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(input_data)[0][1]  # Probability of survival
            st.info(f"💡 Survival Probability: **{prob:.2f}**")

    except Exception as e:
        st.error(f"⚠️ Prediction Error: {e}")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Developed by **Edison Xavier | Titanic ML Project 🚀**")
