from typing import Any, Dict, Optional

import requests

from ..base import BaseLLMProvider

class OpenAIProvider(BaseLLMProvider):
    """
    LLM API provider for OpenAI.
    """

    def call_api(self, prompt: str, **kwargs) -> Optional[Dict[str, Any]]:
        """
        Call the OpenAI LLM API with the given prompt and additional parameters.

        Args:
            prompt (str): The prompt or input text to send to the OpenAI LLM API.
            **kwargs: Additional keyword arguments to pass to the OpenAI LLM API.

        Returns:
            Optional[Dict[str, Any]]: The response from the OpenAI LLM API, or None if an error occurs.
        """
        endpoint = self.config["endpoint"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config['api_key']}",
        }
        data = {
            "prompt": prompt,
            "max_tokens": kwargs.get("max_tokens", 100),
            "n": kwargs.get("n", 1),
            "stop": kwargs.get("stop", None),
            "temperature": kwargs.get("temperature", 0.7),
        }

        response = self._make_request(endpoint, headers=headers, json=data)
        return response