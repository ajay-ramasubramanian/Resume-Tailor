import os

import streamlit as st

from models import (AIModelFactory, GeminiModel, OpenRouterModel,
                    PerplexityModel)

PROVIDER_API_KEY_MAP = {
    "Google Gemini": "GOOGLE_API_KEY",
    "OpenRouter": "OPENROUTER_API_KEY",
    "Perplexity": "PERPLEXITY_API_KEY"
}

def check_provider_availability(provider):
    """Check if a provider's API key is available and the model can be initialized."""
    api_key = os.getenv(PROVIDER_API_KEY_MAP.get(provider, ""))
    if not api_key:
        return False, f"No API key found for {provider}"
    try:
        AIModelFactory.get_model(provider)
        return True, f"{provider} is configured correctly"
    except Exception as e:
        return False, f"Error initializing {provider}: {str(e)}"

def get_provider_capabilities():
    """Return a dictionary of provider capabilities for UI display."""
    return {
        "Google Gemini": {
            "Resume Analysis": "✅ Excellent",
            "Vision Support": "✅ Yes",
            "Speed": "⚡ Fast",
            "Cost": "💰 Low"
        },
        "OpenRouter": {
            "Resume Analysis": "✅ Excellent",
            "Vision Support": "✅ Yes (model dependent)",
            "Speed": "🕒 Medium",
            "Cost": "💰💰 Medium"
        },
        "Perplexity": {
            "Resume Analysis": "✅ Good",
            "Vision Support": "❌ Limited",
            "Speed": "🕒 Medium",
            "Cost": "💰 Low"
        }
    } 