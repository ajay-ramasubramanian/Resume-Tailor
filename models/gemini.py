import json
import os
from typing import Any, Dict, List, Optional

import dotenv
import google.generativeai as genai
import streamlit as st

from .base import AIModel
from .gemini_models import GEMINI_AVAILABLE_MODELS

dotenv.load_dotenv()

class GeminiModel(AIModel):
    """Google Gemini Model Implementation."""
    GEMINI_AVAILABLE_MODELS = GEMINI_AVAILABLE_MODELS

    def __init__(self):
        self._api_key = os.getenv("GOOGLE_API_KEY")
        if not self._api_key:
            st.error("Google API key is missing. Please set the GOOGLE_API_KEY in your environment variables.")
            return
        self.model_name = "gemini-2.0-flash"
        genai.configure(api_key=self._api_key)
        self._refresh_model()

    def _refresh_model(self):
        try:
            self.model = genai.GenerativeModel(self.model_name)
        except Exception as e:
            st.error(f"Failed to initialize Gemini model: {str(e)}")
            raise

    def set_model(self, model_name):
        if model_name in self.GEMINI_AVAILABLE_MODELS:
            self.model_name = model_name
            self._refresh_model()
            return True
        return False

    @classmethod
    def get_available_models(cls):
        return cls.GEMINI_AVAILABLE_MODELS

    def generate_content(self, inputs):
        if not self._api_key:
            return "Error: Google API key is missing"
        try:
            response = self.model.generate_content(inputs)
            return response.text
        except Exception as e:
            return f"Error generating content with Gemini: {str(e)}"

    def get_json_response(self, inputs):
        if not self._api_key:
            return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], "Missing Skills": [], "Suggestions": []}
        try:
            response = self.model.generate_content(inputs)
            return json.loads(response.text[8:-4])
        except Exception as e:
            st.error(f"Failed to parse JSON response from Gemini: {str(e)}")
            return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], "Missing Skills": [], "Suggestions": []} 