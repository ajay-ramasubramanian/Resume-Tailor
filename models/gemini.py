import json
import os

import google.generativeai as genai
import streamlit as st

from .base import AIModel


class GeminiModel(AIModel):
    """Google Gemini Model Implementation."""
    AVAILABLE_MODELS = {
        "gemini-2.0-flash": "Gemini 2.0 Flash (Fastest)",
        "gemini-2.0-pro": "Gemini 2.0 Pro (Balanced)",
        "gemini-2.0-ultra": "Gemini 2.0 Ultra (Most Capable)",
        "gemini-2.5-flash": "Gemini 2.5 Flash (Latest, Fast)",
        "gemini-2.5-pro": "Gemini 2.5 Pro (Latest, Balanced)",
        "gemini-2.0-vision": "Gemini 2.0 Vision (Vision Specialized)"
    }

    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            st.error("Google API key is missing. Please set the GOOGLE_API_KEY in your environment variables.")
            return
        self.model_name = "gemini-2.0-flash"
        genai.configure(api_key=self.api_key)
        self._refresh_model()

    def _refresh_model(self):
        self.model = genai.GenerativeModel(self.model_name)

    def set_model(self, model_name):
        if model_name in self.AVAILABLE_MODELS:
            self.model_name = model_name
            self._refresh_model()
            return True
        return False

    @classmethod
    def get_available_models(cls):
        return cls.AVAILABLE_MODELS

    def generate_content(self, inputs):
        if not self.api_key:
            return "Error: Google API key is missing"
        try:
            response = self.model.generate_content(inputs)
            return response.text
        except Exception as e:
            return f"Error generating content with Gemini: {str(e)}"

    def get_json_response(self, inputs):
        if not self.api_key:
            return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], "Missing Skills": [], "Suggestions": []}
        try:
            response = self.model.generate_content(inputs)
            return json.loads(response.text[8:-4])
        except Exception as e:
            st.error(f"Failed to parse JSON response from Gemini: {str(e)}")
            return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], "Missing Skills": [], "Suggestions": []} 