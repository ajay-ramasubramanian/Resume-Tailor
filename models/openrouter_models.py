"""
Most used model in OpenRouter
"""
OPEN_ROUTER_AVAILABLE_MODELS = {
    # Free Models
    "meta-llama/llama-3.3-70b-instruct:free": "Llama 3.3 70B Instruct (Free)",
    "qwen/qwq-32b:free": "Qwen QwQ 32b (Reasoning model, Free)",
    "meta-llama/llama-3-8b-instruct:free": "Llama 3 8B Instruct (Free)",
    "mistralai/mistral-7b-instruct:free": "Mistral 7B Instruct (Free)",
    "openchat/openchat-7b:free": "OpenChat 7B (Free)",
    "google/gemma-7b-it:free": "Gemma 7B IT (Free)",
    "openrouter/cinematika-7b:free": "Cinematika 7B (Free)",
    "nousresearch/nous-capybara-7b:free": "Nous Capybara 7B (Free)",
    "gryphe/mythomist-7b:free": "Mythomist 7B (Free)",
    "undi95/toppy-m-7b:free": "Toppy M 7B (Free)",
    "nvidia/llama-3.1-nemotron-nano-8b-v1:free": "Llama 3.1 Nemotron Nano 8B (NVIDIA Optimized, Free)",
    
    # Company Specific Models - Anthropic
    "anthropic/claude-3-opus": "Claude 3 Opus (Most Powerful)",
    "anthropic/claude-3-sonnet": "Claude 3 Sonnet (Balanced)",
    "anthropic/claude-3-haiku": "Claude 3 Haiku (Fast)",
    "anthropic/claude-3.5-sonnet": "Claude 3.5 Sonnet (Latest Sonnet)",
    "anthropic/claude-2": "Claude 2 (Legacy)",
    "anthropic/claude-2.0": "Claude 2.0 (Legacy)",
    "anthropic/claude-2.1": "Claude 2.1 (Legacy)",
    "anthropic/claude-instant-1": "Claude Instant 1 (Fast Legacy)",
    
    # Company Specific Models - OpenAI
    "openai/gpt-4o": "GPT-4o (Vision Capable)",
    "openai/gpt-4-vision": "GPT-4 Vision (Specialized Vision)",
    "openai/gpt-3.5-turbo": "GPT-3.5 Turbo (Fast)",
    "openai/gpt-3.5-turbo-0125": "GPT-3.5 Turbo 0125 (Updated)",
    "openai/gpt-3.5-turbo-1106": "GPT-3.5 Turbo 1106",
    "openai/gpt-3.5-turbo-0613": "GPT-3.5 Turbo 0613",
    "openai/gpt-3.5-turbo-0301": "GPT-3.5 Turbo 0301",
    "openai/gpt-3.5-turbo-16k": "GPT-3.5 Turbo 16K (Extended Context)",
    "openai/gpt-4o-2024-05-13": "GPT-4o 2024-05-13 (Latest)",
    "openai/gpt-4-turbo": "GPT-4 Turbo (Fast GPT-4)",
    "openai/gpt-4-turbo-preview": "GPT-4 Turbo Preview",
    "openai/gpt-4-1106-preview": "GPT-4 1106 Preview",
    "openai/gpt-4": "GPT-4 (Original)",
    "openai/gpt-4-0314": "GPT-4 0314",
    "openai/gpt-4-32k": "GPT-4 32K (Extended Context)",
    "openai/gpt-4-32k-0314": "GPT-4 32K 0314",
    "openai/gpt-3.5-turbo-instruct": "GPT-3.5 Turbo Instruct",
    
    # Company Specific Models - Google
    "google/gemini-pro-vision": "Gemini Pro Vision (Google's Vision Model)",
    "google/gemini-pro": "Gemini Pro (Text Only)",
    "google/gemini-pro-1.5": "Gemini Pro 1.5 (Latest)",
    "google/palm-2-chat-bison": "Palm 2 Chat Bison",
    "google/palm-2-codechat-bison": "Palm 2 CodeChat Bison",
    "google/palm-2-chat-bison-32k": "Palm 2 Chat Bison 32K (Extended Context)",
    "google/palm-2-codechat-bison-32k": "Palm 2 CodeChat Bison 32K (Extended Context)",
    
    # Company Specific Models - Meta
    
    "meta-llama/llama-3-70b-instruct": "Llama 3 70B (Open Source, Powerful)",
    "meta-llama/llama-3.1-405b-vision": "Llama 3.1 405B Vision (Vision Capable)",
    "meta-llama/llama-3-8b-instruct-extended": "Llama 3 8B Instruct Extended",
    "meta-llama/llama-3-8b": "Llama 3 8B (Base)",
    "meta-llama/llama-guard-2-8b": "Llama Guard 2 8B (Safety)",
    "meta-llama/codellama-34b-instruct": "Codellama 34B Instruct (Coding)",
    "meta-llama/llama-3-lumimaid-8b": "Llama 3 Lumimaid 8B",
    "meta-llama/llama-3-lumimaid-8b-extended": "Llama 3 Lumimaid 8B Extended",
    
    # Company Specific Models - MistralAI
    "mistralai/mixtral-8x7b": "Mixtral 8x7B (Mixture of Experts)",
    "mistralai/mixtral-8x7b-instruct-nitro": "Mixtral 8x7B Instruct Nitro",
    
    # Company Specific Models - Qwen
    "qwen/qwen-110b-chat": "Qwen 110B Chat (Large)",
    "qwen/qwen-32b-chat": "Qwen 32B Chat",
    "qwen/qwen-14b-chat": "Qwen 14B Chat",
    "qwen/qwen-7b-chat": "Qwen 7B Chat",
    "qwen/qwen-4b-chat": "Qwen 4B Chat",
    "qwen/qwen-2-72b-instruct": "Qwen 2 72B Instruct",
    "qwen/qwen3-235b-a22b:free": "Qwen 3 235B A22B (Free)",
    
    # Company Specific Models - Perplexity
    "perplexity/llama-3-sonar-small-32k-chat": "Llama 3 Sonar Small 32K Chat",
    "perplexity/llama-3-sonar-small-32k-online": "Llama 3 Sonar Small 32K Online",
    "perplexity/llama-3-sonar-large-32k-chat": "Llama 3 Sonar Large 32K Chat",
    "perplexity/llama-3-sonar-large-32k-online": "Llama 3 Sonar Large 32K Online",
    
    # Company Specific Models - OpenRouter
    "openrouter/auto": "OpenRouter Auto (Automatic Selection)",
    "openrouter/cinematika-7b": "Cinematika 7B",
    "openrouter/optimus-alpha": "Optimus Alpha (API-optimized)",
    "openrouter/quasar-alpha": "Quasar Alpha (Reasoning-focused)",
    
    # Company Specific Models - NousResearch
    "nousresearch/nous-capybara-7b": "Nous Capybara 7B",
    "nousresearch/nous-hermes-yi-34b": "Nous Hermes YI 34B",
    "nousresearch/nous-hermes-2-mixtral-8x7b-sft": "Nous Hermes 2 Mixtral 8x7B SFT",
    "nousresearch/nous-hermes-2-mistral-7b-dpo": "Nous Hermes 2 Mistral 7B DPO",
    
    # Company Specific Models - Gryphe
    "gryphe/mythomist-7b": "Mythomist 7B",
    "gryphe/mythomax-l2-13b-extended": "Mythomax L2 13B Extended",
    
    # Company Specific Models - Undi95
    "undi95/remm-slerp-l2-13b-extended": "Remm Slerp L2 13B Extended",
    "undi95/remm-slerp-l2-13b": "Remm Slerp L2 13B",
    
    # Company Specific Models - TogetherComputer
    "togethercomputer/stripedhyena-nous-7b": "StripedHyena Nous 7B",
    "togethercomputer/stripedhyena-hessian-7b": "StripedHyena Hessian 7B",
    
    # Company Specific Models - 01.ai
    "01-ai/yi-34b-chat": "YI 34B Chat",
    "01-ai/yi-34b": "YI 34B",
    "01-ai/yi-6b": "YI 6B",
    
    # Other Models
    "koboldai/psyfighter-13b-2": "Psyfighter 13B 2",
    "intel/neural-chat-7b": "Neural Chat 7B",
    "pygmalionai/mythalion-13b": "Mythalion 13B",
    "xwin-lm/xwin-lm-70b": "Xwin LM 70B",
    "alpindale/goliath-120b": "Goliath 120B",
    "neversleep/noromaid-20b": "Noromaid 20B",
    "sophosympatheia/midnight-rose-70b": "Midnight Rose 70B",
    "sao10k/fimbulvetr-11b-v2": "Fimbulvetr 11B V2",
    "mancer/weaver": "Weaver",
    "open-orca/mistral-7b-openorca": "Mistral 7B OpenOrca",
    "teknium/openhermes-2-mistral-7b": "OpenHermes 2 Mistral 7B",
    "databricks/dbrx-instruct": "DBRX Instruct",
    "allenai/olmo-7b-instruct": "Olmo 7B Instruct",
    "snowflake/snowflake-arctic-instruct": "Snowflake Arctic Instruct",
    "fireworks/firellava-13b": "Firellava 13B",
    "xai/grok-2": "Grok 2"
}
