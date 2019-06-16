import configparser
import requests
import json
import os
import logging

from maisie import APP_ENV_PREFIX, DEFAULT_SETTINGS, PERMITTED_SETTINGS
from maisie.utils.auth import AuthManager
from maisie.utils.git import GitProvider
from maisie.utils.errors import (
    AuthenticationError,
    ConfigInitializationError,
    AuthInitializationError,
)

logger = logging.getLogger(__name__)


class Config:
    """Manages and pre-loads configuration from all available sources."""

    def __init__(self, filename=None, dictionary=None):
        self._fetch_from_dict(dictionary=DEFAULT_SETTINGS)
        self.fetch(filename=filename, dictionary=dictionary)
        self.__auth = None
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def __getattr__(self, name: str):
        logger.error(
            f"Configuration attribute `{name}` was requested but could not be found"
        )

    global source_dict
    source_dict = {}

    @staticmethod
    def _setsource(key, value):
        source_dict[key] = value

    @staticmethod
    def getsource(key):
        if key in source_dict:
            return source_dict[key]

    @property
    def headers(self):
        """Returns HTTP Headers present in all requests sent to the 
        specified target url."""
        return {"Authorization": f"Bearer {self.auth.token}"}

    @property
    def auth(self) -> AuthManager:
        """Authenticates and returns an instance of AuthManager."""
        if self.__auth == None:
            logging.debug("Performing AuthManager class initalization")
            try:
                self.__auth = AuthManager(
                    api_url=self.api_url,
                    login=self.auth_user_login,
                    password=self.auth_user_password,
                    app_token=self.auth_app_token,
                    ssh_key=self.auth_ssh_key,
                )
            except AuthInitializationError:
                logging.error(
                    "Could not authenticate the user using provided configuration"
                )
                raise ConfigInitializationError

        return self.__auth

    def fetch(
        self, filename: str = None, dictionary: dict = None, disable_env: bool = False
    ) -> None:
        """Populates the `Config()` object with attributes from multiple 
        sources.
        
        When both `filename` and `dicionary` are provided, the configuration 
        file is processed first and then the keys from the dictionary will 
        be evaluated.

        :param filename: path to the configuration file. Use of an absolute 
            instead of a relative path is recommended.
        :param dictionary: a structured key-value paired configuration object. 
            Keys not present in `PERMITTED_SETTINGS` will be omitted.
        :param disable_env: whether to disable fetching configuration from 
            environment variables.
        """
        logger.info(
            f"Fetching the configuration. (filename: {filename}, "
            + f"dictionary: {dictionary})"
        )
        if filename:
            self._fetch_from_file(filename)
        if dictionary:
            self._fetch_from_dict(dictionary)
        if filename == None and dictionary == None:
            logger.debug(
                "No custom parameters provided. "
                + "Looking for locally stored configuration"
            )
            self._fetch_scan_directory()
        if not disable_env:
            self._fetch_from_env_variables()
        logger.info("Finished fetching configuration")

    def _fetch_scan_directory(self) -> None:
        """Traverses the local directory tree in search of compatible 
        configuration files."""

        name = ".maisie"

        for root, dirs, files in os.walk(os.getcwd()):
            if name in files:
                filename = os.path.join(root, name)
                logging.debug(f"Found configuration file: {filename}")
                self._fetch_from_file(os.path.join(root, name))
                break

        logger.debug("No configuration files found")

    def _fetch_from_file(self, filename: str) -> None:
        """Populates the `Config()` object with attributes loaded from a given 
        file.

        :param filename: path to the configuration file. Use of an absolute 
            instead of a relative path is recommended.
        """
        logger.debug("Fetching configuration from a given file")
        omitted = []
        loaded = 0
        try:
            file_config = configparser.ConfigParser()
            file_config.read(filename)
            sections = file_config.sections()
            for section in sections:
                for setting in file_config[section]:
                    key = f"{section}_{setting}"
                    value = file_config[section][setting]
                    if key.lower() in PERMITTED_SETTINGS:
                        setattr(self, key, value)
                        self._setsource(key, filename)
                        loaded += 1
                    else:
                        omitted.append(key)

            logger.debug(
                f"Loaded {loaded} settings, omitted: {len(omitted)} "
                + (str(omitted) if omitted else "")
            )
        except FileNotFoundError:
            logger.error(
                f"Provided configuration file ({filename}) could not be found."
            )

    def _fetch_from_dict(self, dictionary: dict) -> None:
        """Populates the `Config()` object with attributes loaded from a given 
        dictionary.

        :param dictionary: a structured key-value paired configuration object. 
            Keys not present in `PERMITTED_SETTINGS` will be omitted.
        """
        logger.debug("Fetching configuration from a given dictionary")
        omitted = []
        for key in dictionary:
            if key.lower() in PERMITTED_SETTINGS:
                setattr(self, key, dictionary[key])
                self._setsource(key, "dictionary")
            else:
                omitted.append(key)

        logger.debug(
            f"Loaded {len(dictionary)} settings, omitted: {len(omitted)} "
            + (str(omitted) if omitted else "")
        )

    def _fetch_from_env_variables(self) -> None:
        """Populates the `Config()` object with attributes loaded from the 
        system's envioronment variables."""
        logger.debug("Fetching configuration from environment variables")

        changed = []
        for key in PERMITTED_SETTINGS:
            env_key = f"{APP_ENV_PREFIX}_{key}".upper()
            env_value = os.environ.get(env_key, None)
            if env_value:
                setattr(self, key, env_value)
                self._setsource(key, "environment")
                changed.append(env_key)

        logger.debug(
            f"Loaded {len(changed)} settings " + (str(changed) if changed else "")
        )


class BaseAction:
    """Base class for actions exposed both in package and for CLI."""

    def __init__(self, config=None):
        self.config = self.__check_config(config)

    def __check_config(self, config):
        try:
            if isinstance(config, str):
                config = Config(filename=config)
            elif isinstance(config, dict):
                config = Config(dictionary=config)
            elif not isinstance(config, Config):
                config = Config()
        except ConfigInitializationError:
            logger.error("Configuration could not be initalized")
        else:
            return config
