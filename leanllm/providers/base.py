from typing import Any, Dict, Optional

import requests

from ..exceptions import LLMProviderError

class BaseLLMProvider:
    """
    Base class for LLM API providers.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    def call_api(self, prompt: str, **kwargs) -> Optional[Dict[str, Any]]:
        """
        Call the LLM API with the given prompt and additional parameters.

        Args:
            prompt (str): The prompt or input text to send to the LLM API.
            **kwargs: Additional keyword arguments to pass to the LLM API.

        Returns:
            Optional[Dict[str, Any]]: The response from the LLM API, or None if an error occurs.
        """
        raise NotImplementedError("This method must be implemented in a subclass.")

    def _make_request(self, endpoint: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Helper method to make a request to the LLM API endpoint.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (Dict[str, Any]): The data to send in the request body.

        Returns:
            Optional[Dict[str, Any]]: The response from the API, or None if an error occurs.
        """
        try:
            response = requests.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise LLMProviderError(f"Error calling LLM API: {str(e)}")
        except Exception as e:
            raise LLMProviderError(f"Error parsing LLM API response: {str(e)}")

        return None