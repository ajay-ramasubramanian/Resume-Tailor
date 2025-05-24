import json
import os

import dotenv
import requests
import streamlit as st

from .base import AIModel
from .perplexity_models import PERPLEXITY_AVAILABLE_MODELS
dotenv.load_dotenv()


class PerplexityModel(AIModel):
    """Perplexity Model Implementation."""
    PERPLEXITY_AVAILABLE_MODELS = PERPLEXITY_AVAILABLE_MODELS

    def __init__(self):
        self._api_key = os.getenv("PERPLEXITY_API_KEY")
        if not self._api_key:
            st.error("Perplexity API key is missing. Please set the PERPLEXITY_API_KEY in your environment variables.")
        self.api_url = "https://api.perplexity.ai/chat/completions"
        self.model_name = "sonar-low-online"

    def set_model(self, model_name):
        if model_name in self.PERPLEXITY_AVAILABLE_MODELS:
            self.model_name = model_name
            return True
        return False

    @classmethod
    def get_available_models(cls):
        return cls.PERPLEXITY_AVAILABLE_MODELS

    def generate_content(self, inputs):
        if not self._api_key:
            return "Error: Perplexity API key is missing"
        system_prompt, image_data, user_prompt = inputs
        headers = {
            "Authorization": f"Bearer {self._api_key}",
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