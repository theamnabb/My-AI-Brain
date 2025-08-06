import streamlit as st

st.title("💪 BMI Calculator App")

# Input fields
weight = st.number_input("Enter your weight (in kg):", min_value=1.0)
height = st.number_input("Enter your height (in meters):", min_value=0.1)

# Button
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.success(f"✅ Your BMI is: {bmi:.2f}")

    # Category
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.info("You have a normal weight.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
