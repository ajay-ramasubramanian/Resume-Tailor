import json
import os

import requests
import streamlit as st

from .base import AIModel


class PerplexityModel(AIModel):
    """Perplexity Model Implementation."""
    AVAILABLE_MODELS = {
        "sonar-medium-online": "Sonar Medium Online (Recommended)",
        "sonar-small-online": "Sonar Small Online (Faster)",
        "sonar-large-online": "Sonar Large Online (Most Powerful)",
        "mixtral-8x7b-instruct": "Mixtral 8x7B (Open Source)",
        "llama-3-70b-instruct": "Llama 3 70B (Meta)",
        "codellama-70b-instruct": "CodeLlama 70B (Code Specialized)"
    }

    def __init__(self):
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        if not self.api_key:
            st.error("Perplexity API key is missing. Please set the PERPLEXITY_API_KEY in your environment variables.")
        self.api_url = "https://api.perplexity.ai/chat/completions"
        self.model_name = "sonar-medium-online"

    def set_model(self, model_name):
        if model_name in self.AVAILABLE_MODELS:
            self.model_name = model_name
            return True
        return False

    @classmethod
    def get_available_models(cls):
        return cls.AVAILABLE_MODELS

    def generate_content(self, inputs):
        if not self.api_key:
            return "Error: Perplexity API key is missing"
        system_prompt, image_data, user_prompt = inputs
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": f"{system_prompt}\n\nNote: The resume is provided as a description since image processing isn't directly supported."},
                {"role": "user", "content": f"I'm analyzing a resume for a job. Here's the job description:\n\n{user_prompt}\n\nPlease analyze as if you could see the resume and provide detailed feedback based on the job description."}
            ]
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error accessing Perplexity API: {str(e)}"

    def get_json_response(self, inputs):
        text_response = self.generate_content(inputs)
        try:
            import re
            json_match = re.search(r'```json\s*(.*?)\s*```', text_response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(1))
            return json.loads(text_response)
        except Exception as e:
            st.error(f"Failed to parse JSON response from Perplexity: {str(e)}")
            return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], "Missing Skills": [], "Suggestions": []} 