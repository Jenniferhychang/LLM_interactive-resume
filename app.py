import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Jennifer Chang - Resume", layout="wide")

# -------------------------
# HEADER
# -------------------------
st.title("Jennifer Chang")
st.subheader("Master of Management Analytics | Data & AI")

st.markdown("---")

# -------------------------
# SIDEBAR (INTERACTIVE WIDGETS)
# -------------------------
st.sidebar.header("Customize Resume")

section = st.sidebar.selectbox(
    "Choose Section",
    ["Overview", "Skills", "Experience", "Education"]
)

experience_filter = st.sidebar.slider(
    "Minimum Years of Experience",
    0, 5, 1
)

show_chart = st.sidebar.checkbox("Show Skills Chart", value=True)

# -------------------------
# OVERVIEW
# -------------------------
if section == "Overview":
    st.header("Professional Summary")
    st.write("""
    Analytics professional with experience in revenue optimization,
    simulation modeling, and AI-powered dashboards.
    """)

# -------------------------
# SKILLS
# -------------------------
elif section == "Skills":
    st.header("Technical Skills")

    skills = pd.DataFrame({
        "Skill": ["Python", "SQL", "Power BI", "R", "Machine Learning"],
        "Proficiency (1-10)": [9, 8, 8, 7, 8]
    })

    st.table(skills)  # REQUIRED TABLE

    if show_chart:
        fig, ax = plt.subplots()
        ax.bar(skills["Skill"], skills["Proficiency (1-10)"])
        ax.set_ylim(0, 10)
        ax.set_ylabel("Proficiency")
        st.pyplot(fig)  # REQUIRED CHART

# -------------------------
# EXPERIENCE
# -------------------------
elif section == "Experience":
    st.header("Work Experience")

    experience = pd.DataFrame({
        "Role": [
            "Analytics Practicum - Indigo",
            "Case Competition Winner",
            "Research Assistant"
        ],
        "Years": [2, 1, 1]
    })

    filtered = experience[experience["Years"] >= experience_filter]

    st.dataframe(filtered)

# -------------------------
# EDUCATION
# -------------------------
elif section == "Education":
    st.header("Education")

    education = pd.DataFrame({
        "Degree": [
            "Master of Management Analytics",
            "Honours BSc - Molecular Biology"
        ],
        "Institution": [
            "University of Toronto",
            "University of Toronto"
        ],
        "CGPA": ["3.68/4.00", "3.94/4.00"]
    })

    st.table(education)

st.markdown("---")
st.write("Built with Streamlit")