import configparser
import requests
import json
import os
import logging

from mlmm import APP_ENV_PREFIX, DEFAULT_SETTINGS, PERMITTED_SETTINGS
from mlmm.utils.auth import AuthManager
from mlmm.utils.git import GitProvider
from mlmm.utils.errors import AuthenticationError, ConfigInitializationError, AuthInitializationError

logger = logging.getLogger(__name__)


class Config:
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

    @property
    def headers(self):
        """Returns HTTP Headers present in all requests sent to the 
        specified target url."""
        return {"Authorization": f"Bearer {self.auth.token}"}
    
    @property
    def auth(self):
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

        # TODO: Implement traversing through user's directory tree
        logger.debug("No configuration files found")

    def _fetch_from_file(self, filename: str) -> None:
        """Populates the `Config()` object with attributes loaded from a given 
        file.

        :param filename: path to the configuration file. Use of an absolute 
            instead of a relative path is recommended.
        """
        try:
            file_config = configparser.ConfigParser()
            file_config.read(filename)
            # TODO: Populate local attributes with values from file_config
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
                changed.append(env_key)

        logger.debug(f"Loaded {len(changed)} settings " + (str(changed) if changed else ""))


class BaseAction:
    def __init__(self, config = None):
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


# def upload_model(
#     name,
#     model,
#     user_id,
#     project_id,
#     dataset_name,
#     dataset_description,
#     hyperparameters,
#     parameters,
#     metrics,
#     private=False,
# ):
#     url = f"{URL}/models/"
#     git = GitProvider()
#     try:
#         files = {"file": open(model, "rb")}
#         if isinstance(hyperparameters, str):
#             with open(hyperparameters, "rb") as hp_file:
#                 hyperparameters = json.load(hp_file)
#         if isinstance(parameters, str):
#             with open(parameters, "rb") as p_file:
#                 parameters = json.load(p_file)
#         if isinstance(metrics, str):
#             with open(metrics, "rb") as m_file:
#                 metrics = json.load(m_file)

#     except FileNotFoundError:
#         print(f"Some of the requested files were not found")

#     payload = {
#         "name": name,
#         "project_id": project_id,
#         "user_id": user_id,
#         "hyperparameters": hyperparameters,
#         "parameters": parameters,
#         "metrics": metrics,
#         "dataset_name": dataset_name,
#         "dataset_description": dataset_description,
#         "git_active_branch": git.active_branch,
#         "git_commit_hash": git.latest_commit,
#         "private": private,
#     }

#     #print("PAYLOAD:", payload)
#     #auth = requests.get("https://ml.kochanowski.dev/api/v1/auth/token/", data={"login":"Nokia", "password": "Nokiademo2019"}
#     #`token = auth.body['data']['access_token']
#     r = requests.post(url, files=files, data=payload)

# if __name__ == "__main__":
#     cli()
