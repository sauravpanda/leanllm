from typing import Any, Dict, Optional, Union
import importlib

from .config import load_config
from .routing import route_request
from .ratelimiting import handle_rate_limiting
from .batching import batch_requests
from .caching import get_cached_response, cache_response

def call_llm(
    prompt: str,
    config: Optional[Dict[str, Any]] = None,
    provider: Optional[str] = None,
    batch_size: Optional[int] = None,
    **kwargs
) -> Union[str, Dict[str, Any]]:
    """
    Call a Large Language Model (LLM) API provider with the given prompt.

    Args:
        prompt (str): The prompt or input text to send to the LLM API.
        config (Optional[Dict[str, Any]]): A dictionary containing the configuration settings.
        provider (Optional[str]): The name of the LLM API provider to use.
        batch_size (Optional[int]): The number of requests to batch together.
        **kwargs: Additional keyword arguments to pass to the LLM API provider.

    Returns:
        Union[str, Dict[str, Any]]: The response from the LLM API provider.
    """
    # Load configuration
    config = load_config(config)

    # Check cache for existing response
    cached_response = get_cached_response(prompt, config)
    if cached_response:
        return cached_response

    # Route request to the appropriate provider
    provider_name, provider_config = route_request(provider, config)

    # Handle rate limiting
    handle_rate_limiting(provider_name, provider_config)

    # Batch requests if batch_size is provided
    if batch_size:
        prompt = batch_requests(prompt, batch_size, provider_name, provider_config)

    # Call the LLM API provider
    response = call_provider(provider_name, prompt, provider_config, **kwargs)

    # Cache the response
    cache_response(prompt, response, config)

    return response

def call_provider(
    provider_name: str,
    prompt: str,
    provider_config: Dict[str, Any],
    **kwargs
) -> Union[str, Dict[str, Any]]:
    """
    Call the specified LLM API provider with the given prompt and configuration.

    Args:
        provider_name (str): The name of the LLM API provider to call.
        prompt (str): The prompt or input text to send to the LLM API.
        provider_config (Dict[str, Any]): The configuration settings for the LLM API provider.
        **kwargs: Additional keyword arguments to pass to the LLM API provider.

    Returns:
        Union[str, Dict[str, Any]]: The response from the LLM API provider.
    """
    # Import the provider module dynamically
    provider_module = importlib.import_module(f".providers.{provider_name}", package=__name__)

    # Call the provider's API with the prompt and configuration
    response = provider_module.call_api(prompt, provider_config, **kwargs)

    return response