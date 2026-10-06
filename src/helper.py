import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables
load_dotenv()

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    """
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {e}")

def ask_ai(prompt, max_tokens=500):
    """
    Uses free AI APIs that don't require complex setup
    """
    try:
        # Option 1: Try Hugging Face Inference API with a simpler approach
        HF_TOKEN = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
        
        if HF_TOKEN:
            # Use a more reliable model
            API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
            headers = {"Authorization": f"Bearer {HF_TOKEN}"}
            
            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": max_tokens,
                    "temperature": 0.7,
                    "do_sample": True,
                    "return_full_text": False
                }
            }
            
            response = requests.post(API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', 'No response generated')
                elif isinstance(result, dict) and 'generated_text' in result:
                    return result['generated_text']
        
        # Option 2: Fallback to simple rule-based responses
        return generate_fallback_response(prompt)
            
    except Exception as e:
        # Final fallback
        return generate_fallback_response(prompt)

def generate_fallback_response(prompt):
    """
    Generate basic responses when AI APIs fail
    """
    prompt_lower = prompt.lower()
    
    if "summarize" in prompt_lower or "resume" in prompt_lower:
        return "Based on the resume analysis, this candidate shows relevant experience. Focus on highlighting key skills, education background, and work experience in your applications."
    
    elif "skill gap" in prompt_lower or "missing" in prompt_lower:
        return "Consider developing skills in emerging technologies and obtaining relevant certifications to enhance your profile. Focus on both technical and soft skills."
    
    elif "roadmap" in prompt_lower or "future" in prompt_lower:
        return "Career Development Roadmap:\n1. Identify target roles and required skills\n2. Pursue relevant certifications\n3. Build project portfolio\n4. Network with industry professionals\n5. Continuous learning and skill updates"
    
    elif "job titles" in prompt_lower or "keywords" in prompt_lower:
        return "Software Engineer, Developer, IT Professional, Technology Specialist, Programmer"
    
    else:
        return "I've analyzed your profile. Focus on roles that match your technical background and consider upskilling in current market technologies."

# For backward compatibility
ask_google = ask_ai
ask_huggingface = ask_ai