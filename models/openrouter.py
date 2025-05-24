import json
import os
import dotenv
import requests
import streamlit as st
from .base import AIModel
from .openrouter_models import OPEN_ROUTER_AVAILABLE_MODELS
dotenv.load_dotenv()

class OpenRouterModel(AIModel):
    """OpenRouter Model Implementation."""
    OPEN_ROUTER_AVAILABLE_MODELS = OPEN_ROUTER_AVAILABLE_MODELS
    @classmethod
    def get_free_models(cls):
        free_keys = [
            "qwen/qwq-32b:free",
            "meta-llama/llama-3-8b-instruct:free",
            "mistralai/mistral-7b-instruct:free",
            "openchat/openchat-7b:free",
            "google/gemma-7b-it:free"
        ]
        return {k: v for k, v in cls.OPEN_ROUTER_AVAILABLE_MODELS.items() if k in free_keys}

    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        if not self.api_key:
            st.error("OpenRouter API key is missing. Please set the OPENROUTER_API_KEY in your environment variables.")
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model_name = "anthropic/claude-3-opus"

    def set_model(self, model_name):
        if model_name in self.OPEN_ROUTER_AVAILABLE_MODELS:
            self.model_name = model_name
            return True
        return False

    @classmethod
    def get_available_models(cls):
        return cls.OPEN_ROUTER_AVAILABLE_MODELS

    def generate_content(self, inputs):
        if not self.api_key:
            return "Error: OpenRouter API key is missing"
        system_prompt, image_data, user_prompt = inputs
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://application-tracking-system.streamlit.app",
            "X-Title": "ATS Resume Scanner"
        }
        if "anthropic" in self.model_name or "gpt-4" in self.model_name or "vision" in self.model_name:
            payload = {
                "model": self.model_name,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": [
                        {"type": "text", "text": user_prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data['data']}"}}
                    ]}
                ]
            }
        else:
            payload = {
                "model": self.model_name,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"[Image of resume attached]\n\nJob Description: {user_prompt}"}
                ]
            }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error accessing OpenRouter: {str(e)}"

    def get_json_response(self, inputs):
        text_response = self.generate_content(inputs)
        try:
            import re
            json_match = re.search(r'```json\s*(.*?)\s*```', text_response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(1))
            return json.loads(text_response)
        except Exception as e:
            st.error(f"Failed to parse JSON response from OpenRouter: {str(e)}")
            return {"Technical Skills": [], "Analytical Skills": [], "Soft Skills": [], "Missing Skills": [], "Suggestions": []} 