import click
import logging
from terminaltables import SingleTable

from maisie import Workspaces
from maisie.utils.misc import Transform

DEFAULT_DISPLAY_ATTRIBUTES = ["id", "name", "description", "created"]


@click.group()
def workspaces():
    pass


@click.option(
    "-n", "--name", prompt="Workspace's name", help="Name of workspace to add"
)
@click.option(
    "-d",
    "--description",
    prompt="Workspace's description",
    help="Description of workspace to add",
)
# @click.option("-git", "--git_url", prompt = "Git Repository (URL)", help = "Url of git repository")
@click.command()
def add(name, description):
    workspace = Workspaces().create(name, description)
    table = SingleTable(
        Transform().api_response_to_terminaltables(
            workspace, include=DEFAULT_DISPLAY_ATTRIBUTES
        )
    )
    table.inner_row_border = True
    table.title = "List of workspaces"
    click.echo(table.table)


@click.command()
def rm():
    pass


@click.command()
@click.option(
    "-id", "--id", default=None, type=int, help="Returns workspace with a specified id"
)
def ls(id):
    if id:
        workspaces = Workspaces().get(id)
    else:
        workspaces = Workspaces().get_all()

    if workspaces:
        table = SingleTable(
            Transform().api_response_to_terminaltables(
                workspaces, include=DEFAULT_DISPLAY_ATTRIBUTES
            )
        )
        table.inner_row_border = True
        table.title = "List of workspaces"
        click.echo(table.table)


workspaces.add_command(add)
workspaces.add_command(rm)
workspaces.add_command(ls)
