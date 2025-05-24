"""
All models available through Perplexity API
"""
PERPLEXITY_AVAILABLE_MODELS = {
    # Sonar Models (Search-enabled)
    "perplexity/sonar-pro": "Sonar Pro (Advanced search model with 8k max output tokens, 200k context)",
    "perplexity/sonar": "Sonar (Lightweight search model, 128k context, cost-effective)",
    "perplexity/sonar-reasoning-pro": "Sonar Reasoning Pro (Premier reasoning model with Chain of Thought, 128k context)",
    "perplexity/sonar-reasoning": "Sonar Reasoning (Fast real-time reasoning model, 128k context)",
    "perplexity/sonar-deep-research": "Sonar Deep Research (Expert-level research model, 128k context)",
    
    # Offline Models
    "perplexity/r1-1776": "R1-1776 (Offline chat model, no search, 128k context)",
    
    # Llama-based Sonar Models (via OpenRouter)
    "perplexity/llama-3.1-sonar-small-128k-online": "Llama 3.1 Sonar Small 128k Online (Real-time information)",
    "perplexity/llama-3.1-sonar-large-128k-online": "Llama 3.1 Sonar Large 128k Online (Real-time information)",
    "perplexity/llama-3.1-sonar-huge-128k-online": "Llama 3.1 Sonar Huge 128k Online (Real-time information)",
    "perplexity/llama-3.1-sonar-small-128k-chat": "Llama 3.1 Sonar Small 128k Chat",
    "perplexity/llama-3.1-sonar-large-128k-chat": "Llama 3.1 Sonar Large 128k Chat",
    "perplexity/llama-3-sonar-small-32k-chat": "Llama 3 Sonar Small 32K Chat",
    "perplexity/llama-3-sonar-small-32k-online": "Llama 3 Sonar Small 32K Online",
    "perplexity/llama-3-sonar-large-32k-chat": "Llama 3 Sonar Large 32K Chat",
    "perplexity/llama-3-sonar-large-32k-online": "Llama 3 Sonar Large 32K Online",
    
    # Perplexity Pro Subscription Models
    "perplexity/sonar-large": "Sonar Large (Built on LlaMa 3.1 70B, optimized for search)",
    "perplexity/default": "Default (Optimized for speed and web browsing)",
    "perplexity/o3-mini": "O3-mini (OpenAI's reasoning model for complex tasks)",
    "perplexity/r1": "DeepSeek's R1 (Open-source reasoning model)"
}
