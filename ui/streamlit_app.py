import sys
import os

# Fix import paths
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st

from workflow.resume_workflow import app
from parsers.resume_parser import extract_resume_text


# Page configuration
st.set_page_config(
    page_title="AI Resume Optimizer",
    page_icon="📄",
    layout="wide"
)


# Title
st.title("📄 AI Resume Optimizer")
st.write(
    "Upload your resume and paste the job description to get an ATS-optimized resume."
)


# Job Description Input
job_description = st.text_area(
    "Paste Job Description",
    height=250
)


# Resume Upload
uploaded_resume = st.file_uploader(
    "Upload Your Resume",
    type=["pdf", "docx", "txt"]
)


# Optimize Button
if st.button("Optimize Resume"):

    # Validation
    if not job_description:
        st.error("Please enter a job description.")

    elif not uploaded_resume:
        st.error("Please upload your resume.")

    else:
        # Extract resume text
        current_resume = extract_resume_text(
            uploaded_resume
        )

        # Initial state for LangGraph
        initial_state = {
            "messages": [],

            "job_description": job_description,

            "current_resume": current_resume,

            "candidate_information": "",

            "questions_asked": 0,
            "generated_questions": [],
            "user_answers": [],

            "jd_analysis": "",

            "skill_gap_analysis": "",
            "missing_skills": [],
            "suggested_skills": [],

            "optimized_resume": "",

            "resume_score": 0,
            "improvement_feedback": "",

            "completed": False
        }


        # Run AI Workflow
        with st.spinner(
            "AI agents are analyzing your resume..."
        ):
            result = app.invoke(initial_state)


        st.success(
            "Resume Optimization Completed Successfully!"
        )


        # Display Results
        tab1, tab2 = st.tabs(
            [
                "Optimized Resume",
                "Resume Review"
            ]
        )


        with tab1:
            st.subheader("📄 ATS Optimized Resume")
            st.write(
                result["optimized_resume"]
            )


        with tab2:
            st.subheader("📊 Resume Analysis")
            st.write(
                result["improvement_feedback"]
            )