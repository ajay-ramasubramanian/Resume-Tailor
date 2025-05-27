import os

import streamlit as st

from models import (AIModelFactory, GeminiModel, OpenRouterModel,
                    PerplexityModel)
from prompts.prompts import (EXECUTIVE_SUMMARY_PROMPT,
                             KEYWORDS_ANALYSIS_PROMPT, MATCH_PERCENTAGE_PROMPT,
                             TAILOR_RESUME_PROMPT)
from providers.selection import (check_provider_availability,
                                 get_provider_capabilities)
from utils.cache import (get_ai_response, get_ai_response_keywords,
                         get_ai_response_tailor)
from utils.pdf_utils import pdf_to_base64_images

st.set_page_config(page_title="Resume Tailor/Analyzer", layout="wide")
st.header("Resume Tailor/Analyzer")

# Sidebar for configuration
with st.sidebar:
    st.header("AI Provider Settings")
    st.subheader("API Provider Stats")
    provider_option = st.session_state.get("model_provider", "Google Gemini")
    provider_capabilities = get_provider_capabilities()
    capabilities = provider_capabilities.get(provider_option, {})
    if capabilities:
        for capability, rating in capabilities.items():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.text(f"{capability}:")
            with col2:
                st.text(rating)
    api_key_var = {
        "Google Gemini": "GOOGLE_API_KEY",
        "OpenRouter": "OPENROUTER_API_KEY",
        "Perplexity": "PERPLEXITY_API_KEY"
    }.get(provider_option)
    api_key_available = os.getenv(api_key_var, "") != ""
    col1, col2 = st.columns(2)
    with col1:
        if api_key_available:
            st.success("API Key: Available")
        else:
            st.error("API Key: Missing")
    with col2:
        try:
            model = AIModelFactory.get_model(provider_option)
            st.success("Model: Ready")
        except Exception as e:
            st.error("Model: Error")
    provider_option = st.selectbox(
        "Select AI Provider",
        ["Google Gemini", "OpenRouter", "Perplexity"],
        index=0,
        help="Choose which AI provider to use for analysis"
    )
    if 'model_provider' not in st.session_state or st.session_state.model_provider != provider_option:
        st.session_state.model_provider = provider_option
    st.subheader("API Key Configuration")
    if provider_option == "Google Gemini":
        if not os.getenv("GOOGLE_API_KEY"):
            st.error("Google API key is missing. Please set GOOGLE_API_KEY in your .env file.")
        gemini_models = GeminiModel.get_available_models()
        model_keys = list(gemini_models.keys())
        model_names = list(gemini_models.values())
        selected_model_name = st.selectbox(
            "Select Gemini Model",
            options=model_names,
            index=0,
            format_func=lambda x: x,
            help="Choose which Gemini model to use for analysis"
        )
        selected_model_key = model_keys[model_names.index(selected_model_name)]
        if 'gemini_model' not in st.session_state or st.session_state.gemini_model != selected_model_key:
            st.session_state.gemini_model = selected_model_key
            model_instance = AIModelFactory.get_model("Google Gemini")
            model_instance.set_model(selected_model_key)
    elif provider_option == "OpenRouter":
        if not os.getenv("OPENROUTER_API_KEY"):
            st.error("OpenRouter API key is missing. Please set OPENROUTER_API_KEY in your .env file.")
        openrouter_models = OpenRouterModel.get_available_models()
        model_keys = list(openrouter_models.keys())
        model_names = list(openrouter_models.values())
        selected_model_name = st.selectbox(
            "Select OpenRouter Model",
            options=model_names,
            index=0,
            format_func=lambda x: x,
            help="Choose which model to use with OpenRouter"
        )
        selected_model_key = model_keys[model_names.index(selected_model_name)]
        if 'openrouter_model' not in st.session_state or st.session_state.openrouter_model != selected_model_key:
            st.session_state.openrouter_model = selected_model_key
            model_instance = AIModelFactory.get_model("OpenRouter")
            model_instance.set_model(selected_model_key)
        st.info("OpenRouter allows you to access various AI models through a single API. Some models support vision capabilities better than others.")
    elif provider_option == "Perplexity":
        if not os.getenv("PERPLEXITY_API_KEY"):
            st.error("Perplexity API key is missing. Please set PERPLEXITY_API_KEY in your .env file.")
        perplexity_models = PerplexityModel.get_available_models()
        model_keys = list(perplexity_models.keys())
        model_names = list(perplexity_models.values())
        selected_model_name = st.selectbox(
            "Select Perplexity Model",
            options=model_names,
            index=0,
            format_func=lambda x: x,
            help="Choose which model to use with Perplexity"
        )
        selected_model_key = model_keys[model_names.index(selected_model_name)]
        if 'perplexity_model' not in st.session_state or st.session_state.perplexity_model != selected_model_key:
            st.session_state.perplexity_model = selected_model_key
            model_instance = AIModelFactory.get_model("Perplexity")
            model_instance.set_model(selected_model_key)
        st.warning("Note: Perplexity API doesn't directly support image input. Resume analysis will be limited with this provider.")
    st.info("""
    Set your API keys in a .env file:
    ```
    GOOGLE_API_KEY=your_key_here
    OPENROUTER_API_KEY=your_key_here
    PERPLEXITY_API_KEY=your_key_here
    ```
    """)
    with st.expander("📋 Model Selection Guide"):
        st.markdown("""
        ### Model Selection Tips
        #### Google Gemini
        - **Gemini 2.0 Flash**: Fastest model, good for quick assessments
        - **Gemini 2.0 Pro**: Balanced performance and quality
        - **Gemini 2.0 Ultra**: Highest capability, best for detailed analysis
        - **Gemini 2.5 Pro/Flash**: Latest models with improved capabilities
        #### OpenRouter
        - **Claude 3 Opus**: Most capable for resume analysis
        - **Claude 3 Sonnet**: Good balance of speed and quality
        - **GPT-4o**: Excellent vision capabilities for resume parsing
        - **Llama models**: Open source alternatives
        #### Perplexity
        - **Sonar Medium**: Recommended for most uses
        - **Sonar Large**: Most powerful option
        - **Note**: Perplexity has limited resume image processing capabilities
        ### Which provider is best?
        - For resume parsing: OpenRouter with Claude 3 or GPT-4o models
        - For fastest results: Google Gemini with Flash models
        - For detailed analysis: Claude 3 Opus via OpenRouter
        """)
        st.warning("Note that each provider requires its own API key and may have different pricing models.")

# Main app area
provider = st.session_state.model_provider
model_instance = AIModelFactory.get_model(provider)
if provider == "Google Gemini" and 'gemini_model' in st.session_state:
    model_instance.set_model(st.session_state.gemini_model)
elif provider == "OpenRouter" and 'openrouter_model' in st.session_state:
    model_instance.set_model(st.session_state.openrouter_model)
elif provider == "Perplexity" and 'perplexity_model' in st.session_state:
    model_instance.set_model(st.session_state.perplexity_model)
selected_model_name = ""
if provider == "Google Gemini" and 'gemini_model' in st.session_state:
    model_dict = GeminiModel.get_available_models()
    if st.session_state.gemini_model in model_dict:
        selected_model_name = model_dict[st.session_state.gemini_model]
elif provider == "OpenRouter" and 'openrouter_model' in st.session_state:
    model_dict = OpenRouterModel.get_available_models()
    if st.session_state.openrouter_model in model_dict:
        selected_model_name = model_dict[st.session_state.openrouter_model]
elif provider == "Perplexity" and 'perplexity_model' in st.session_state:
    model_dict = PerplexityModel.get_available_models()
    if st.session_state.perplexity_model in model_dict:
        selected_model_name = model_dict[st.session_state.perplexity_model]
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])
if 'resume' not in st.session_state:
    st.session_state.resume = None
if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    st.session_state.resume = uploaded_file
if selected_model_name:
    st.caption(f"Using AI Provider: {provider} | Model: {selected_model_name}")
else:
    st.caption(f"Using AI Provider: {provider}")
col1, col2, col3, col4 = st.columns(4, gap="medium")
with col1:
    submit1 = st.button("Tell Me About the Resume")
with col2:
    submit2 = st.button("Get Keywords")
with col3:
    submit3 = st.button("Percentage match")
with col4:
    submit4 = st.button("Tailor Resume")
if submit1:
    if not st.session_state.resume:
        st.error("Please upload a resume before analyzing")
        st.stop()
    if not input_text:
        st.warning("Please provide a job description for better analysis")
    available, message = check_provider_availability(st.session_state.model_provider)
    if not available:
        st.error(f"Provider configuration issue: {message}")
        st.info("Please check your API key in the sidebar settings")
        st.stop()
    with st.spinner(f"Analyzing resume using {st.session_state.model_provider}..."):
        pdf_content = pdf_to_base64_images(st.session_state.resume)
        response = get_ai_response(EXECUTIVE_SUMMARY_PROMPT, pdf_content, input_text, st.session_state.model_provider)
        if isinstance(response, str) and response.startswith("Error:"):
            st.error(response)
        else:
            with st.expander("Resume Analysis", expanded=True):
                st.write(response)
elif submit2:
    if not st.session_state.resume:
        st.error("Please upload a resume before analyzing")
        st.stop()
    if not input_text:
        st.warning("Please provide a job description for better keyword extraction")
    available, message = check_provider_availability(st.session_state.model_provider)
    if not available:
        st.error(f"Provider configuration issue: {message}")
        st.info("Please check your API key in the sidebar settings")
        st.stop()
    with st.spinner(f"Extracting keywords using {st.session_state.model_provider}..."):
        pdf_content = pdf_to_base64_images(st.session_state.resume)
        response = get_ai_response_keywords(KEYWORDS_ANALYSIS_PROMPT, pdf_content, input_text, st.session_state.model_provider)
        if response is not None:
            st.subheader("Skills Analysis:")
            error_detected = False
            if "Suggestions" in response and response["Suggestions"]:
                for suggestion in response["Suggestions"]:
                    if isinstance(suggestion, str) and suggestion.startswith("Error:"):
                        st.error(suggestion)
                        error_detected = True
                        break
            if not error_detected:
                with st.expander("Technical Skills", expanded=True):
                    if "Technical Skills" in response and response["Technical Skills"]:
                        st.write(f"{', '.join(response['Technical Skills'])}")
                    else:
                        st.info("No technical skills identified")
                with st.expander("Analytical Skills", expanded=True):
                    if "Analytical Skills" in response and response["Analytical Skills"]:
                        st.write(f"{', '.join(response['Analytical Skills'])}")
                    else:
                        st.info("No analytical skills identified")
                with st.expander("Soft Skills", expanded=True):
                    if "Soft Skills" in response and response["Soft Skills"]:
                        st.write(f"{', '.join(response['Soft Skills'])}")
                    else:
                        st.info("No soft skills identified")
                if "Missing Skills" in response and response["Missing Skills"]:
                    with st.expander("Missing Skills", expanded=True):
                        st.write(f"{', '.join(response['Missing Skills'])}")
                if "Suggestions" in response and response["Suggestions"]:
                    with st.expander("Improvement Suggestions", expanded=True):
                        for suggestion in response["Suggestions"]:
                            st.write(f"• {suggestion}")
        else:
            st.error("Failed to extract keywords from the resume")
elif submit3:
    if not st.session_state.resume:
        st.error("Please upload a resume before calculating match percentage")
        st.stop()
    if not input_text:
        st.warning("Please provide a job description to calculate the match percentage")
    available, message = check_provider_availability(st.session_state.model_provider)
    if not available:
        st.error(f"Provider configuration issue: {message}")
        st.info("Please check your API key in the sidebar settings")
        st.stop()
    with st.spinner(f"Calculating match percentage using {st.session_state.model_provider}..."):
        pdf_content = pdf_to_base64_images(st.session_state.resume)
        response = get_ai_response(MATCH_PERCENTAGE_PROMPT, pdf_content, input_text, st.session_state.model_provider)
        if isinstance(response, str) and response.startswith("Error:"):
            st.error(response)
        else:
            st.subheader("Match Analysis")
            try:
                import re
                match = re.search(r'MATCH SCORE:\s*\[(\d+\.\d+)%\]', response)
                if match:
                    percentage = float(match.group(1))
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.metric("Match", f"{percentage}%")
                    if percentage >= 80:
                        with col2:
                            st.success("STRONG MATCH")
                    elif percentage >= 65:
                        with col2:
                            st.info("POTENTIAL MATCH")
                    elif percentage >= 50:
                        with col2:
                            st.warning("CONDITIONAL MATCH")
                    else:
                        with col2:
                            st.error("NOT RECOMMENDED")
            except Exception:
                pass
            st.write(response)
elif submit4:
    if not st.session_state.resume:
        st.error("Please upload a resume before getting tailoring suggestions")
        st.stop()
    if not input_text:
        st.error("Please provide a job description to tailor your resume effectively")
        st.stop()
    available, message = check_provider_availability(st.session_state.model_provider)
    if not available:
        st.error(f"Provider configuration issue: {message}")
        st.info("Please check your API key in the sidebar settings")
        st.stop()
    with st.spinner(f"Generating resume tailoring suggestions using {st.session_state.model_provider}..."):
        pdf_content = pdf_to_base64_images(st.session_state.resume)
        response = get_ai_response_tailor(TAILOR_RESUME_PROMPT, pdf_content, input_text, st.session_state.model_provider)
        if isinstance(response, str) and response.startswith("Error:"):
            st.error(response)
        else:
            st.subheader("🎯 Resume Tailoring Recommendations")
            st.success("✨ **Great news!** Your resume has strong potential. Here are personalized suggestions to optimize it for this specific role and boost your ATS compatibility!")
            
            # Display the tailored recommendations in an expandable format
            with st.expander("📋 Complete Tailoring Guide", expanded=True):
                st.markdown(response)
            
            # Add helpful tips section
            with st.expander("💡 Quick Implementation Tips", expanded=False):
                st.markdown("""
                ### How to Use These Suggestions:
                
                **🚀 Start with Quick Wins:**
                - Focus on the bullet point transformations first - these have immediate impact
                - Update your skills section with the recommended keywords
                - Revise your professional summary to include key terms
                
                **📝 Implementation Strategy:**
                1. **Copy your current resume** to a new document
                2. **Apply transformations one by one** - don't rush the process
                3. **Read each section aloud** to ensure it sounds natural
                4. **Keep the original meaning** of your achievements intact
                
                **✅ Quality Check:**
                - Ensure all new keywords are truthful and reflect your actual experience
                - Maintain consistency in terminology throughout your resume
                - Keep bullet points concise and impactful
                - Verify that industry-specific terms are used correctly
                
                **🎯 Remember:**
                - These suggestions enhance your existing story, not create a new one
                - Focus on highlighting transferable skills you actually possess
                - Tailor the suggestions further for each specific job application
                """)
            
            # Add encouragement section
            st.info("💪 **You've got this!** These optimizations will significantly improve your resume's performance with both ATS systems and human recruiters. Take your time implementing these changes - quality over speed!")
            
            # Add download suggestion
            st.markdown("---")
            st.markdown("**💾 Pro Tip:** Save these recommendations and refer back to them when applying to similar roles. Many of these optimizations can be reused for positions in the same field!")
