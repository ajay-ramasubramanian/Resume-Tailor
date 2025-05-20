import streamlit as st

from models import AIModelFactory


@st.cache_data()
def get_ai_response(input_prompt, pdf_content, prompt, provider):
    """Get AI model response for a given provider."""
    try:
        model = AIModelFactory.get_model(provider)
        return model.generate_content([input_prompt, pdf_content[0], prompt])
    except Exception as e:
        return f"Error: Could not get response from {provider}. Please check your API key and model selection.\n\nTechnical details: {str(e)}"

@st.cache_data()
def get_ai_response_keywords(input_prompt, pdf_content, prompt, provider):
    """Get AI model keyword analysis response for a given provider."""
    try:
        model = AIModelFactory.get_model(provider)
        response = model.get_json_response([input_prompt, pdf_content[0], prompt])
        if not isinstance(response, dict):
            return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], 
                    "Missing Skills": [], "Suggestions": ["Error: Invalid response format from model"]}
        return response
    except Exception as e:
        return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], 
                "Missing Skills": [], "Suggestions": [f"Error: {str(e)}"]} 