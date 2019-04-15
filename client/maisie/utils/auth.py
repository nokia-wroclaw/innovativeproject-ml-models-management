import logging
import requests

from maisie.utils.errors import AuthInitializationError, AuthenticationError

logger = logging.getLogger(__name__)


class AuthManager:
    def __init__(
        self,
        api_url: str,
        login: str,
        password: str = None,
        app_token: str = None,
        ssh_key: str = None,
        enforce_ssh: bool = False,
    ):
        self.api_url = api_url
        self.login = login
        self.password = password
        self.app_token = app_token
        self.ssh_key = ssh_key
        self.enforce_ssh = enforce_ssh
        self.__access_token = None
        self.__access_token_expiry = None
        if not password and not app_token and not ssh_key:
            raise AuthInitializationError

    @property
    def user_id(self) -> int:
        pass

    @property
    def logged_in(self) -> bool:
        return False

    @property
    def token_active(self) -> bool:
        return True

    @property
    def token(self) -> str:
        if not self.__access_token:
            logger.debug("Access token not set")
            self.retrieve_token()
        elif not self.token_active:
            logger.debug("Access token not active")
            self.refresh_token(self.__access_token)
        # logger.debug(f"Returning access token: {self.__access_token}")
        return self.__access_token

    def perform_auth(self, channels=["ssh_key", "app_token", "password"]):
        logger.info("Performing authentication")
        # try:
        # if "ssh_key" in channels and self.ssh_key:
        #     logger.debug("SSH Key present")
        #     self._auth_via_ssh_key()
        # if "app_token" in channels and self.app_token:
        #     logger.debug("APP Token present")
        #     self._auth_via_app_token()
        if "password" in channels and self.password:
            logger.debug("Password present")
            self._auth_via_password()
        # except AuthenticationError:

    def retrieve_token(self) -> None:
        """Retrieves the token via available authentication methods."""
        self.perform_auth()

    def refresh_token(self, old_token: str) -> str:
        """Refreshes the token using the old one.

        :param old_token:
        :returns: a refreshed JWT. 
        """
        new_token = old_token
        request = requests.get(
            f"{self.api_url}/auth/token/",
            headers={"Authorization": f"Bearer: {old_token}"},
        )
        data = request.json()["data"]
        logger.debug(data)

        self.__access_token = data["access_token"]

    def _auth_via_password(self):
        logger.debug("Attempting authentication via password")
        request = requests.post(
            f"{self.api_url}/auth/login/",
            data={"login": self.login, "password": self.password},
        )
        if "data" not in request.json():
            logger.error("Could not authenticate. Is the login and password correct?")
        else:
            data = request.json()["data"]
            logger.debug(data)

            self.__access_token = data["access_token"]

    def _auth_via_app_token(self):
        logger.debug("Attempting authentication via app token")
        raise AuthenticationError

    def _auth_via_ssh_key(self):
        logger.debug("Attempting authentication via ssh")
        raise AuthenticationError
