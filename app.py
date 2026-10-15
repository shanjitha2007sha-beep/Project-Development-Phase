import streamlit as st
import google generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="FitBuddy", page_icon="💪")

st.title("💪 FitBuddy - Your AI Fitness Partner")
st.caption("Indian Diet + Home Workout - No Gym Needed!")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=15, max_value=60, value=20)

with col2:
    weight = st.number_input("Weight kg", min_value=30, max_value=150, value=65)

with col3:
    height = st.number_input("Height cm", min_value=120, max_value=200, value=170)

goal = st.selectbox(
    "Goal Enna?",
    ["Weight Loss", "Muscle Gain", "Weight Gain", "Stay Fit"]
)

diet_type = st.selectbox(
    "Diet Preference",
    ["Veg", "Non-Veg", "Eggetarian"]
)

workout_place = st.radio("Workout Enga?", ["Home", "Gym"])
medical = st.text_input("Any health issues? (Ex: None, Asthma)")

if st.button("🔥 Generate My Plan"):
    with st.spinner("Plan create panrom..."):
        prompt = f"""
Create a general fitness plan for {age} years old.
Weight: {weight} kg
Height: {height} cm
Goal: {goal}
Diet: {diet_type}
Workout place: {workout_place}
Health issues: {medical}

Give:
1. BMI calculation
2. 7-day Indian diet chart with meals
3. 7-day beginner workout plan
4. Water and sleep tips
Use simple Tamil-English mix.
Keep advice safe and general.
"""

try:
            res = model.generate_content(prompt)
            st.write(res.text)
        except Exception as e:
            st.error(f"Error generating plan: {e}")
