import click
import os

from terminaltables import SingleTable

from maisie.utils.misc import Transform
from terminaltables import SingleTable
from maisie import PERMITTED_SETTINGS, APP_ENV_PREFIX, Config


@click.group()
def config():
    pass


@click.command()
def ls():
    table_to_display = [("key", "value", "source")]
    # os.environ['MAISIE_API_PAGE'] = '20'
    # os.environ['MAISIE_API_PER_PAGE'] = '19'
    config = Config()
    for config_name in PERMITTED_SETTINGS:
        config_name_full = f"{APP_ENV_PREFIX}_{config_name.upper()}"
        value = getattr(config, config_name)
        source = config.getsource(config_name)
        table_to_display.append((config_name_full, value, source))
    table = SingleTable(table_to_display)
    table.inner_row_border = True
    click.echo(table.table)


@click.command()
@click.option(
    "-url",
    "--api_url",
    prompt="Api url",
    default=None,
    type=str,
    help="Provide api url",
)
@click.option(
    "-page",
    "--api_page",
    prompt="Number of api page",
    default=1,
    type=int,
    help="Provide number of api page",
)
@click.option(
    "-per_page",
    "--api_per_page",
    prompt="Number of objects to display",
    default=10,
    type=int,
    help="Provide number of projects to display",
)
@click.option(
    "-repo",
    "--git_local_repo",
    prompt="Git local repository",
    default=None,
    type=str,
    help="Provide git local repository",
)
@click.option(
    "-login",
    "--auth_user_login",
    prompt="User login",
    default=None,
    type=str,
    help="Provide user login",
)
@click.option(
    "-password",
    "--auth_user_password",
    prompt="User password",
    default=None,
    type=str,
    help="Provide user password",
)
@click.option(
    "-token",
    "--auth_app_token",
    prompt="App token",
    default=None,
    type=str,
    help="Provide app token",
)
@click.option(
    "-key",
    "--auth_ssh_key",
    prompt="Ssh key",
    default=None,
    type=str,
    help="Provide ssh key",
)
@click.option(
    "-enable",
    "--logging_enable",
    prompt="Logging enable",
    default=True,
    type=bool,
    help="Boolean value",
)
@click.option(
    "-level",
    "--logging_level",
    prompt="Logging level",
    default="INFO",
    type=str,
    help="CRITICAL/ERROR/WARNING/INFO/DEBUG",
)
@click.option(
    "-logging_file",
    "--logging_file",
    prompt="Logging file",
    default=None,
    type=str,
    help="Path to logging file",
)
@click.option(
    "-project",
    "--selected_project",
    prompt="Selected project",
    default=None,
    type=str,
    help="Selected project",
)
@click.option(
    "-workspace",
    "--selected_workspace",
    prompt="Selected workspace",
    default=None,
    type=str,
    help="Selected workspace",
)
@click.option(
    "-file",
    "--config_file_path",
    prompt="Path to configuration file",
    default=os.getcwd(),
    type=str,
    help="Path to file where this configuration settings will be saved",
)
def generate(
    api_url,
    api_page,
    api_per_page,
    git_local_repo,
    auth_user_login,
    auth_user_password,
    auth_app_token,
    auth_ssh_key,
    logging_enable,
    logging_level,
    logging_file,
    selected_project,
    selected_workspace,
    config_file_path,
):

    content = f"""[api] \n url = {api_url} \n api_page = {api_page} \n api_per_page = {api_per_page} \n
[links] \n git_local_repo = {git_local_repo} \n
[auth] \n auth_user_login = {auth_user_login} \n auth_user_password = {auth_user_password} 
 auth_app_token = {auth_app_token} \n auth_ssh_key = {auth_ssh_key} \n 
[logging] \n logging_enable = {logging_enable} \n logging_level = {logging_level} \n logging_file = {logging_file} \n 
[selected] \n selected_project = {selected_project} \n selected_workspace = {selected_workspace} \n """

    with open(f"{config_file_path}\\.maisie", "w") as configuration_file:
        configuration_file.write(content)
        print("Configuration file successfully created")


@click.command()
def edit():
    name = ".maisie"
    for root, dirs, files in os.walk(os.getcwd()):
        if name in files:
            filename = os.path.join(root, name)

            # logging.debug(f"Found configuration file: {filename}")
            # self._fetch_from_file(os.path.join(root, name))
            # break

    click.edit(require_save=True, filename=filename)


config.add_command(ls)
config.add_command(generate)
config.add_command(edit)
