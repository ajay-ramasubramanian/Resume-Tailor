from abc import ABC, abstractmethod


class AIModel(ABC):
    """Abstract base class for all AI models."""
    @abstractmethod
    def generate_content(self, inputs):
        pass

    @abstractmethod
    def get_json_response(self, inputs):
        pass 