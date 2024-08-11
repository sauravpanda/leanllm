class LLMProviderError(Exception):
    """
    Exception raised when there is an error with an LLM API provider.
    """
    pass

class InvalidProviderError(LLMProviderError):
    """
    Exception raised when an invalid LLM API provider is specified.
    """
    pass

class RateLimitError(LLMProviderError):
    """
    Exception raised when the rate limit has been exceeded for an LLM API provider.
    """
    pass