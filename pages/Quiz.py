import streamlit as st

def run_diabetes_assessment():
    st.set_page_config(page_title="Diabetes Risk Assessment", layout="centered")
    st.title("🩺 Diabetes Risk Assessment Quiz")
    st.write("Answer the following questions to assess diabetes risk:")

    # Questions
    questions = [
        "Has the patient ever been pregnant?",
        "Is their glucose level 100 or above?",
        "Do they have a low blood pressure?",
        "Do they have their skin thickness over or equal to 30?",
        "Do they have a high insulin level?",
        "Is their BMI over 30?",
        "Do they have a high BMI? (over 30)",
        "Are they 30 years old or older?"
    ]

    # Store answers
    answers = {}
    st.subheader("Select Yes or No for each question:")
    for i, question in enumerate(questions):
        answers[question] = st.radio(question, ["Yes", "No"], index=1, key=f"q{i}")

    # Calculate score
    number_of_diag = sum(1 for ans in answers.values() if ans == "Yes")

    # Display result dynamically
    st.markdown("---")
    st.write(f"**Total score:** {number_of_diag} / {len(questions)}")
    if number_of_diag >= 3:
        st.error("⚠️ Based on the score, the patient has a HIGH RISK of diabetes.")
    else:
        st.success("✅ Based on the score, the patient has a LOW RISK of diabetes.")

if __name__ == "__main__":
    run_diabetes_assessment()
