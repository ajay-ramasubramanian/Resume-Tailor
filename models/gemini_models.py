"""
All models available through Gemini API
"""
GEMINI_AVAILABLE_MODELS = {
    # Gemini 2.0 Models (Stable)
    "gemini-2.0-flash": "Gemini 2.0 Flash (Latest stable, multimodal with 1M token context)",
    "gemini-2.0-flash-001": "Gemini 2.0 Flash 001 (Stable version, multimodal with 1M token context)",
    "gemini-2.0-flash-lite-001": "Gemini 2.0 Flash-Lite 001 (Fastest and most cost efficient Flash model)",
    
    # Gemini 2.5 Models (Preview)
    "gemini-2.5-pro-preview-05-06": "Gemini 2.5 Pro Preview (Most advanced reasoning model)",
    "gemini-2.5-flash-preview-05-20": "Gemini 2.5 Flash Preview (Latest preview, balanced price/performance)",
    "gemini-2.5-flash-preview-04-17": "Gemini 2.5 Flash Preview (Previous preview version)",
    
    # Gemini 2.0 Live Models
    "gemini-2.0-flash-live-001": "Gemini 2.0 Flash Live 001 (Low-latency bidirectional voice/video)",
    "gemini-2.0-flash-live-preview-04-09": "Gemini 2.0 Flash Live Preview (Streaming multimodal I/O)",
    
    # Gemini Image Generation
    "gemini-2.0-flash-preview-image-generation": "Gemini 2.0 Flash Preview Image Generation",
    "gemini-2.0-flash-exp-image-generation": "Gemini 2.0 Flash Experimental Image Generation (Deprecated)",
    
    # Embedding Models
    "embedding-001": "Embedding 001 (Text embeddings with 768 dimensions)",
    "text-embedding-004": "Text Embedding 004 (Experimental SOTA embedding model)",
    
    # Special Purpose Models
    "aqa": "AQA (Attributed Question-Answering over documents)",
    
    # Previous Experimental Models (Now Replaced)
    "gemini-2.0-flash-thinking-exp-01-21": "Gemini 2.0 Flash Thinking Experimental (Replaced)",
    "gemini-2.0-pro-exp-02-05": "Gemini 2.0 Pro Experimental (Replaced)",
    "gemini-2.0-flash-exp": "Gemini 2.0 Flash Experimental (Replaced)",
    "gemini-exp-1206": "Gemini Experimental 1206 (Replaced)",
    "gemini-2.0-flash-thinking-exp-1219": "Gemini 2.0 Flash Thinking Experimental 1219 (Replaced)",
    "gemini-exp-1121": "Gemini Experimental 1121 (Replaced)",
    "gemini-exp-1114": "Gemini Experimental 1114 (Replaced)",
    
    # Gemini 1.5 Models (Older)
    "gemini-1.5-pro-exp-0827": "Gemini 1.5 Pro Experimental 0827 (Replaced)",
    "gemini-1.5-pro-exp-0801": "Gemini 1.5 Pro Experimental 0801 (Replaced)",
    "gemini-1.5-flash-8b-exp-0924": "Gemini 1.5 Flash-8B Experimental 0924 (Replaced)",
    "gemini-1.5-flash-8b-exp-0827": "Gemini 1.5 Flash-8B Experimental 0827 (Replaced)",
    "gemini-1.5-flash-8b": "Gemini 1.5 Flash-8B (Older stable version)",
    
    # Imagen 3 Models (Image Generation)
    "imagen-3.0-generate-002": "Imagen 3.0 Generate 002 (High-quality image generation)",
    "imagen-3.0-fast-generate-001": "Imagen 3.0 Fast Generate 001 (Fast image generation)"
}
