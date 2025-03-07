import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="Prediction of Disease Outbreaks",
    layout="centered",
    page_icon="🧑‍⚕️⚕️"
)

# Cache model loading to improve performance
@st.cache_data
def load_models(working_dir):
    """Load pre-trained models from the working directory."""
    try:
        diabetes_model = pickle.load(open(f'{working_dir}/SVM/diabetes_svm.pkl', 'rb'))
        heart_disease_model = pickle.load(open(f'{working_dir}/SVM/heart_svm.pkl', 'rb'))
        parkinsons_model = pickle.load(open(f'{working_dir}/RF/parkinsons_rf.pkl', 'rb'))
        return diabetes_model, heart_disease_model, parkinsons_model
    except FileNotFoundError as e:
        st.error(f"Model file not found: {e}")
        return None, None, None
    except pickle.UnpicklingError:
        st.error("Model file is corrupted.")
        return None, None, None

# Function to predict diabetes
def predict_diabetes(user_input, model):
    """Predict diabetes based on user input."""
    try:
        user_input = [float(x) for x in user_input]
        prediction = model.predict([user_input])
        return "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Function to predict heart disease
def predict_heart_disease(user_input, model):
    """Predict heart disease based on user input."""
    try:
        user_input = [float(x) for x in user_input]
        prediction = model.predict([user_input])
        return "The person has heart disease" if prediction[0] == 1 else "The person does not have heart disease"
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Function to predict Parkinson's disease
def predict_parkinsons(user_input, model):
    """Predict Parkinson's disease based on user input."""
    try:
        user_input = [float(x) for x in user_input]
        prediction = model.predict([user_input])
        return "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
    except ValueError:
        return "Invalid input. Please enter numeric values."

# Main function to run the app
def main():
    # Get the working directory
    working_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Load models
    diabetes_model, heart_disease_model, parkinsons_model = load_models(working_dir)
    
    if diabetes_model is None or heart_disease_model is None or parkinsons_model is None:
        st.error("Failed to load one or more models. Please check the model files.")
        return
    
    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction"],
            icons=["activity", "heart", "person"],
            default_index=0,
        )
    


    # Diabetes Prediction Page
    if selected == "Diabetes Prediction":
        st.title("Diabetes Prediction")
        st.write("Please enter the following details:")
        
        # Input fields for diabetes prediction
        pregnancies = st.text_input("No. of Pregnancies")
        glucose = st.text_input("Glucose Level")
        blood_pressure = st.text_input("Blood Pressure")
        skin_thickness = st.text_input("Skin Thickness")
        insulin = st.text_input("Insulin Level")
        bmi = st.text_input("BMI")
        diabetes_pedigree = st.text_input("Diabetes Pedigree Function")
        age = st.text_input("Age")
        
        if st.button("Predict Diabetes"):
            user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
            result = predict_diabetes(user_input, diabetes_model)
            st.success(result)
    


    # Heart Disease Prediction Page
    if selected == "Heart Disease Prediction":
        st.title("Heart Disease Prediction")
        st.write("Please enter the following details:")
        
        # Input fields for diabetes prediction
        age = st.text_input("Age")
        sex = st.text_input("Sex")
        cpt = st.text_input("Chest Pain Types")
        resting_blood_pressure = st.text_input("Resting Blood Pressure")
        chol = st.text_input("Serum Cholestrol in mg/dl")
        fbs = st.text_input("Fasting Blood Sugar >120 mg/dl")
        restecg = st.text_input("Resting Electro cardiographic results")
        maxhr = st.text_input("MAximun Heart Rate Achieved")
        exang = st.text_input("Exercise Induced Angina")
        ST = st.text_input("ST depression indiced by exercise")
        slope = st.text_input("Slope of the peak exercise ST segment")
        mjr_vessels = st.text_input("Major vessels colored by fluroscopy")
        thal = st.text_input("Thalassemia: 0 = normal, 1 = fixed defect, 2 = reversable defect")
        
        if st.button("Predict Heart Disease"):
            user_input = [age, sex, cpt, resting_blood_pressure,chol,fbs,restecg,maxhr,exang,ST,slope,mjr_vessels,thal]
            result = predict_diabetes(user_input, diabetes_model)
            st.success(result)



    # Parkinson's Disease Prediction Page
    if selected == "Parkinson's Prediction":
        st.title("Parkinson's Disease Prediction")
        st.write("Please enter the following details (in numerical values:")
        
        # Input fields for Parkinson's disease prediction
        Fo = st.text_input("Fo(Hz)")
        Fhi = st.text_input("Fhi(Hz)")
        Flo = st.text_input("Flo(Hz)")
        Jitter = st.text_input("Jitter(%)")
        Jitter_Abs = st.text_input("Jitter(Abs)(%)")
        RAP = st.text_input("RAP")
        PPQ = st.text_input("PPQ")
        DDP = st.text_input("DDP")
        Shimmer = st.text_input("Shimmer")
        Shimmer_dB = st.text_input("Shimmer(dB)")
        APQ3 = st.text_input("APQ3")
        APQ5 = st.text_input("APQ5")
        APQ = st.text_input("APQ")
        DDA = st.text_input("DDA")
        NHR = st.text_input("NHR")
        HNR = st.text_input("HNR")
        RPDE = st.text_input("RPDE")
        DFA = st.text_input("DFA")
        spred1 = st.text_input("spread1")
        spred2 = st.text_input("spread2")
        D2 = st.text_input("D2")
        PPE = st.text_input("PPE")

        if st.button("Predict Parkinson's Disease"):
            user_input = [Fo, Fhi, Flo, Jitter, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spred1, spred2, D2, PPE]
            result = predict_parkinsons(user_input, parkinsons_model)
            st.success(result)

if __name__ == "__main__":
    main()