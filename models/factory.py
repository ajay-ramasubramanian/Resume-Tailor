from .gemini import GeminiModel
from .openrouter import OpenRouterModel
from .perplexity import PerplexityModel


class AIModelFactory:
    """Factory for creating and caching AI model instances."""
    _instances = {}

    @classmethod
    def get_model(cls, provider_name):
        if provider_name in cls._instances:
            return cls._instances[provider_name]
        if provider_name == "Google Gemini":
            cls._instances[provider_name] = GeminiModel()
        elif provider_name == "OpenRouter":
            cls._instances[provider_name] = OpenRouterModel()
        elif provider_name == "Perplexity":
            cls._instances[provider_name] = PerplexityModel()
        else:
            raise ValueError(f"Unknown provider: {provider_name}")
        return cls._instances[provider_name]

    @staticmethod
    def get_provider_models(provider_name):
        if provider_name == "Google Gemini":
            return GeminiModel.get_available_models()
        elif provider_name == "OpenRouter":
            return OpenRouterModel.get_available_models()
        elif provider_name == "Perplexity":
            return PerplexityModel.get_available_models()
        else:
            return {} 