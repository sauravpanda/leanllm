import os
from typing import Any, Dict, Optional

DEFAULT_CONFIG = {
    "providers": {
        "openai": {
            "api_key": os.environ.get("OPENAI_API_KEY"),
            "endpoint": "https://api.openai.com/v1/engines/text-davinci-003/completions",
        },
        "anthropic": {
            "api_key": os.environ.get("ANTHROPIC_API_KEY"),
            "endpoint": "https://api.anthropic.com/v1/complete",
        },
        "cohere": {
            "api_key": os.environ.get("COHERE_API_KEY"),
            "endpoint": "https://api.cohere.ai/v1/generate",
        },
    },
    "default_provider": "openai",
    "caching": {
        "enabled": True,
        "expiration": 3600,  # 1 hour
    },
}

def load_config(config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Load the configuration settings for the LLM API wrapper.

    Args:
        config (Optional[Dict[str, Any]]): A dictionary containing the configuration settings.
            If not provided, the default configuration will be used.

    Returns:
        Dict[str, Any]: The loaded configuration settings.
    """
    if config is None:
        config = DEFAULT_CONFIG
    else:
        # Merge the provided config with the default config
        merged_config = {**DEFAULT_CONFIG, **config}
        config = merged_config

    return config