import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
import datetime
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Resume Optimizer",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for futuristic design
st.markdown("""
<style>
    /* Futuristic Onyx Background */
    .stApp {
        background-color: #16191E;
        color: #00F0FF;
        font-family: 'Orbitron', sans-serif;
    }

    /* Neon Blue Buttons */
    .stButton > button {
        background-color: #00F0FF;
        color: #16191E;
        border: 2px solid #00F0FF;
        border-radius: 10px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        font-weight: bold;
    }

    .stButton > button:hover {
        background-color: #16191E;
        color: #00F0FF;
        box-shadow: 0 0 15px #00F0FF;
    }

    /* Dynamic 3D Cube Effect for Resume Generation */
    @keyframes rotate-cube {
        0% { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
        100% { transform: rotateX(360deg) rotateY(360deg) rotateZ(360deg); }
    }

    .cube-container {
        perspective: 1000px;
        width: 100%;
        height: 400px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .cube {
        width: 200px;
        height: 200px;
        position: relative;
        transform-style: preserve-3d;
        animation: rotate-cube 10s linear infinite;
    }

    .cube-face {
        position: absolute;
        width: 200px;
        height: 200px;
        opacity: 0.8;
        border: 2px solid #00F0FF;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgba(0, 240, 255, 0.1);
        color: #00F0FF;
        font-size: 16px;
        font-weight: bold;
        backface-visibility: visible;
        transform-style: preserve-3d;
    }

    .cube-face-front  { 
        transform: translateZ(100px) rotateY(0deg);
    }
    .cube-face-back   { 
        transform: rotateY(180deg) translateZ(100px);
    }
    .cube-face-right  { 
        transform: rotateY(90deg) translateZ(100px);
    }
    .cube-face-left   { 
        transform: rotateY(-90deg) translateZ(100px);
    }
    .cube-face-top    { 
        transform: rotateX(90deg) translateZ(100px);
    }
    .cube-face-bottom { 
        transform: rotateX(-90deg) translateZ(100px);
    }

    /* Ensure text is always readable */
    .cube-face-front, 
    .cube-face-back, 
    .cube-face-right, 
    .cube-face-left, 
    .cube-face-top, 
    .cube-face-bottom {
        backface-visibility: visible !important;
        transform-style: preserve-3d;
    }

    /* Responsive Design */
    @media (max-width: 600px) {
        .cube-container {
            height: 300px;
        }
        .cube, .cube-face {
            width: 150px;
            height: 150px;
        }
    }
</style>
""", unsafe_allow_html=True)

def generate_3d_cube_html():
    """Generate HTML for 3D rotating cube with readable text"""
    return """
    <div class="cube-container">
        <div class="cube">
            <div class="cube-face cube-face-front">AI Resume</div>
            <div class="cube-face cube-face-back">Optimizing</div>
            <div class="cube-face cube-face-right">Processing</div>
            <div class="cube-face cube-face-left">Generating</div>
            <div class="cube-face cube-face-top">Magic</div>
            <div class="cube-face cube-face-bottom">Working</div>
        </div>
    </div>
    """


def generate_resume(resume, job_description):
    # Initialize Groq client
    groq_api_key = os.getenv("GROQ_API_KEY")
    client = Groq(api_key=groq_api_key)
    
    # Generate resume
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "user", 
                "content": f"Build a custom resume for this job posting. Resume: {resume} Job Description: {job_description}"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    
    return completion.choices[0].message.content

def main():
    st.title("🚀 AI Resume Optimizer")
    st.subheader("Craft Your Perfect Resume with AI")

    # Input sections
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Upload Your Current Resume")
        resume_file = st.file_uploader("Choose Resume File", type=['txt'])
        resume_text = st.text_area("Or Paste Resume", height=200)

    with col2:
        st.markdown("### Job Description")
        job_description_file = st.file_uploader("Choose Job Description File", type=['txt'])
        job_description_text = st.text_area("Or Paste Job Description", height=200)

    # Determine resume and job description text
    if resume_file:
        resume = resume_file.getvalue().decode('utf-8')
    else:
        resume = resume_text

    if job_description_file:
        job_description = job_description_file.getvalue().decode('utf-8')
    else:
        job_description = job_description_text

    # Generate and Display Resume
    if st.button("✨ Optimize Resume"):
        if resume and job_description:
            # Create a placeholder for the 3D cube
            cube_placeholder = st.empty()
            
            # Display 3D cube during generation
            cube_placeholder.markdown(generate_3d_cube_html(), unsafe_allow_html=True)
            
            try:
                # Generate resume
                optimized_resume = generate_resume(resume, job_description)
                
                # Clear the cube placeholder
                cube_placeholder.empty()
                
                # Display generated resume
                st.text_area("Optimized Resume", value=optimized_resume, height=300)
                
                # Download Button
                st.download_button(
                    label="💾 Download Optimized Resume",
                    data=optimized_resume,
                    file_name=f"optimized_resume_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
            
            except Exception as e:
                # Clear the cube placeholder in case of error
                cube_placeholder.empty()
                st.error(f"An error occurred: {str(e)}")
        
        else:
            st.warning("Please provide both resume and job description.")

    # Clear Button
    if st.button("🔄 Clear All"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()


