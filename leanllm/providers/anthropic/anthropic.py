from typing import Any, Dict, Optional

from ..base import BaseLLMProvider

class AnthropicProvider(BaseLLMProvider):
    """
    LLM API provider for Anthropic.
    """

    def call_api(self, prompt: str, **kwargs) -> Optional[Dict[str, Any]]:
        """
        Call the Anthropic LLM API with the given prompt and additional parameters.

        Args:
            prompt (str): The prompt or input text to send to the Anthropic LLM API.
            **kwargs: Additional keyword arguments to pass to the Anthropic LLM API.

        Returns:
            Optional[Dict[str, Any]]: The response from the Anthropic LLM API, or None if an error occurs.
        """
        endpoint = self.config["endpoint"]
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.config["api_key"],
        }
        data = {
            "prompt": prompt,
            "max_tokens_to_sample": kwargs.get("max_tokens", 100),
            "stop_sequences": kwargs.get("stop", []),
            "temperature": kwargs.get("temperature", 0.7),
        }

        response = self._make_request(endpoint, headers=headers, json=data)
        return response