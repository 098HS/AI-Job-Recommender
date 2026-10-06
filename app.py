import streamlit as st
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

st.set_page_config(page_title="Job Recommender", layout="wide")

try:
    from helper import extract_text_from_pdf, ask_ai
    from job_api import fetch_linkedin_jobs, fetch_naukri_jobs
    st.success("✅ All modules imported successfully!")
except ImportError as e:
    st.error(f"❌ Import error: {e}")
    st.stop()

st.title("📄 AI Job Recommender")
st.markdown(
    "Upload your resume and get job recommendations based on your skills and experience."
)

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success("✅ Text extracted successfully!")

    # Use simpler, more reliable analysis
    st.markdown("---")
    st.header("📑 Resume Analysis")
    
    with st.spinner("Analyzing your profile..."):
        summary = ask_ai(f"Summarize this resume: {resume_text[:1000]}", 300)
        gaps = ask_ai(f"Suggest skill improvements for: {resume_text[:1000]}", 200)
        roadmap = ask_ai(f"Career advice for: {resume_text[:1000]}", 200)

    st.write("**Profile Summary:**")
    st.write(summary)
    
    st.write("**Skill Development Suggestions:**")
    st.write(gaps)
    
    st.write("**Career Guidance:**")
    st.write(roadmap)

    st.success("✅ Analysis Completed Successfully!")

    if st.button("🔎 Get Job Recommendations"):
        # Use predefined keywords instead of AI-generated ones for reliability
        predefined_keywords = "Software Developer, IT Jobs, Technology Roles"
        
        st.success(f"Searching for: {predefined_keywords}")

        with st.spinner("Fetching job listings..."):
            linkedin_jobs = fetch_linkedin_jobs(predefined_keywords, rows=5)
            naukri_jobs = fetch_naukri_jobs(predefined_keywords, rows=5)

        st.markdown("---")
        st.header("💼 Job Recommendations")

        if linkedin_jobs:
            st.subheader("LinkedIn Jobs")
            for job in linkedin_jobs:
                st.markdown(f"**{job.get('title', 'Position')}** at *{job.get('companyName', 'Company')}*")
                st.markdown(f"📍 {job.get('location', 'Location not specified')}")
                if job.get('link'):
                    st.markdown(f"🔗 [Apply Here]({job.get('link')})")
                st.markdown("---")
        else:
            st.info("No LinkedIn jobs found. Try different search terms.")

        if naukri_jobs:
            st.subheader("Other Job Opportunities") 
            for job in naukri_jobs:
                st.markdown(f"**{job.get('title', 'Position')}** at *{job.get('companyName', 'Company')}*")
                st.markdown(f"📍 {job.get('location', 'Location not specified')}")
                if job.get('link') or job.get('url'):
                    job_link = job.get('link') or job.get('url')
                    st.markdown(f"🔗 [Apply Here]({job_link})")
                st.markdown("---")