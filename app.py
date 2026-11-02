```python
import streamlit as st
from pypdf import PdfReader

from main import ResumeScreeningPipeline


# Page configuration
st.set_page_config(
    page_title="SmartHireAI",
    page_icon="🎯",
    layout="wide"
)


# Application heading
st.title("🎯 SmartHireAI")
st.subheader("AI-Powered Resume Screening")
st.write(
    "Upload a resume and provide a job description "
    "to evaluate candidate skills and job suitability."
)

st.divider()


# Resume upload
st.header("1. Upload Candidate Resume")

uploaded_resume = st.file_uploader(
    "Choose a resume (PDF)",
    type=["pdf"]
)

resume_text = ""

if uploaded_resume is not None:
    try:
        reader = PdfReader(uploaded_resume)

        resume_text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        ).strip()

        if resume_text:
            st.success("Resume uploaded and text extracted successfully.")
            with st.expander("Preview extracted resume text"):
                st.text(resume_text[:5000])
        else:
            st.warning(
                "No readable text was found. "
                "This PDF may be scanned or image-based."
            )

    except Exception as error:
        st.error(f"Could not read the PDF: {error}")


# Job description
st.header("2. Enter Job Description")

job_description = st.text_area(
    "Paste the job description below",
    height=250,
    placeholder=(
        "Example: We are looking for a Java developer "
        "with knowledge of Java, Spring Boot, SQL, REST APIs, "
        "and Git."
    )
)


# Run screening
st.header("3. Evaluate Candidate")

if st.button("🚀 Analyze Resume", type="primary"):

    if not uploaded_resume:
        st.warning("Please upload a candidate resume first.")

    elif not resume_text:
        st.warning(
            "The resume contains no extractable text. "
            "Please upload a text-based PDF."
        )

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        try:
            with st.spinner(
                "Analyzing skills and matching job requirements..."
            ):
                pipeline = ResumeScreeningPipeline()

                report = pipeline(
                    resume_text=resume_text,
                    job_description=job_description.strip()
                )

            st.success("Resume screening completed!")

            # Candidate analysis
            candidate = report["candidate_analysis"]
            job_match = report["job_match"]

            st.divider()
            st.header("📋 Candidate Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Technical Skills")
                st.write(candidate["skills"])

                st.subheader("Suitable Roles")
                st.write(candidate["suitable_roles"])

            with col2:
                st.subheader("Experience Summary")
                st.write(candidate["experience_summary"])

                st.subheader("Resume Evidence")
                st.write(candidate["evidence"])

            # Job matching results
            st.divider()
            st.header("🎯 Job Match Results")

            score = job_match["suitability_score"]

            st.metric(
                label="Estimated Job Match",
                value=f"{score}/100"
            )

            st.progress(score / 100)

            st.subheader("Matching Skills")
            st.write(job_match["matching_skills"])

            st.subheader("Missing or Unverified Skills")
            st.write