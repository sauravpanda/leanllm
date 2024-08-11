from typing import Any, Dict, Optional, Tuple

from ..exceptions import InvalidProviderError

def route_request(
    provider: Optional[str],
    config: Dict[str, Any]
) -> Tuple[str, Dict[str, Any]]:
    """
    Route the request to the appropriate LLM API provider based on the configuration.

    Args:
        provider (Optional[str]): The name of the LLM API provider to use. If not provided,
            the default provider from the configuration will be used.
        config (Dict[str, Any]): The configuration settings for the LLM API wrapper.

    Returns:
        Tuple[str, Dict[str, Any]]: A tuple containing the name of the selected LLM API provider
            and its configuration settings.

    Raises:
        InvalidProviderError: If the specified provider is not found in the configuration.
    """
    if not provider:
        provider = config.get("default_provider")

    provider_config = config["providers"].get(provider)
    if not provider_config:
        raise InvalidProviderError(f"Provider '{provider}' is not configured.")

    return provider, provider_config