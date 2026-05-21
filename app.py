import streamlit as st
import pandas as pd
from fpdf import FPDF

# Page Configuration
st.set_page_config(
    page_title="Career Counseling Expert System",
    page_icon="🎓",
    layout="centered"
)

# Sidebar
st.sidebar.title("🎓 Expert System")
st.sidebar.info(
    """
    MIS-703 Project
    
    Expert System & Applied AI
    """
)

st.sidebar.success("Developed Using Python + Streamlit")

# Main Title
st.title("🎓 Student Career Counseling Expert System")

st.write("Fill the form below to get smart career recommendation.")

# User Inputs
name = st.text_input("👤 Enter Your Name")

maths = st.slider("📐 Math Skills", 0, 100)
programming = st.slider("💻 Programming Skills", 0, 100)
communication = st.slider("🗣 Communication Skills", 0, 100)
design = st.slider("🎨 Design Creativity", 0, 100)

interest = st.selectbox(
    "📌 Select Your Main Interest",
    [
        "Programming",
        "Artificial Intelligence",
        "Designing",
        "Business",
        "Networking"
    ]
)

# Recommendation Logic
if st.button("🚀 Get Recommendation"):

    st.subheader(f"Hello {name} 👋")

    # Expert Rules
    if maths > 70 and programming > 70:
        career = "Software Engineering"
        description = "You have strong programming and logical skills."

    elif interest == "Artificial Intelligence":
        career = "AI / Data Science"
        description = "You are suitable for Artificial Intelligence field."

    elif design > 70:
        career = "Graphic Designing"
        description = "You have excellent creativity and design skills."

    elif communication > 70 and interest == "Business":
        career = "Business Administration"
        description = "You have strong communication and management skills."

    elif interest == "Networking":
        career = "Cyber Security"
        description = "You are interested in networking and security."

    else:
        career = "Information Technology"
        description = "You are suitable for general IT fields."

    # Display Result
    st.success(f"✅ Recommended Career: {career}")

    st.info(description)

    # Skills Chart
    st.subheader("📊 Skills Analysis")

    data = pd.DataFrame({
        "Skills": [
            "Maths",
            "Programming",
            "Communication",
            "Design"
        ],
        "Score": [
            maths,
            programming,
            communication,
            design
        ]
    })

    st.bar_chart(data.set_index("Skills"))

    # PDF Report Generation
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Career Counseling Report", ln=True, align='C')

    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Recommended Career: {career}", ln=True)

    pdf.multi_cell(0, 10, txt=f"Description: {description}")

    pdf.ln(10)

    pdf.cell(200, 10, txt="Skills Scores:", ln=True)

    pdf.cell(200, 10, txt=f"Math Skills: {maths}", ln=True)
    pdf.cell(200, 10, txt=f"Programming Skills: {programming}", ln=True)
    pdf.cell(200, 10, txt=f"Communication Skills: {communication}", ln=True)
    pdf.cell(200, 10, txt=f"Design Skills: {design}", ln=True)

    pdf.output("career_report.pdf")

    # Download Button
    with open("career_report.pdf", "rb") as file:
        st.download_button(
            label="📥 Download PDF Report",
            data=file,
            file_name="career_report.pdf",
            mime="application/pdf"
        )

# Footer
st.markdown("---")
st.caption("Developed for MIS-703 | Expert System & Applied AI")
