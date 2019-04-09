class ConfigInitializationError(Exception):
    """Configuration either could not be initalized or was not provided."""


class AuthInitializationError(Exception):
    """Authentication Manager object could not be initialized."""


class AuthenticationError(Exception):
    """Provided credentials could not satisfy the requirements for the purpose 
    of authentication."""
