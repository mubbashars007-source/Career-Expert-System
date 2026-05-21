import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Career Counseling Expert System",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Career Counseling Expert System")

st.write("Fill the form below to get career recommendation.")

# Inputs
name = st.text_input("Enter Your Name")

maths = st.slider("Math Skills", 0, 100)
programming = st.slider("Programming Skills", 0, 100)
communication = st.slider("Communication Skills", 0, 100)
design = st.slider("Design Creativity", 0, 100)

interest = st.selectbox(
    "Choose Your Interest",
    [
        "Programming",
        "Artificial Intelligence",
        "Designing",
        "Business",
        "Networking"
    ]
)

# Button
if st.button("Get Recommendation"):

    st.subheader(f"Hello {name} 👋")

    # Expert System Rules
    if maths > 70 and programming > 70:
        career = "Software Engineering"

    elif interest == "Artificial Intelligence":
        career = "AI / Data Science"

    elif design > 70:
        career = "Graphic Designing"

    elif communication > 70 and interest == "Business":
        career = "Business Administration"

    elif interest == "Networking":
        career = "Cyber Security"

    else:
        career = "Information Technology"

    st.success(f"✅ Recommended Career: {career}")

    st.info("Recommendation generated using Expert System Rules.")

# Footer
st.markdown("---")
st.caption("MIS-703 Project | Expert System & Applied AI")