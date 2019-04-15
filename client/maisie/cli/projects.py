import click
import logging
from terminaltables import SingleTable

from maisie import Projects
from maisie.utils.misc import Transform

DEFAULT_DISPLAY_ATTRIBUTES = [
    "id",
    # "workspace_id",
    "name",
    "description",
    "git_url",
    "created",
]


@click.group()
def projects():
    pass


@click.command()
@click.option(
    "-n", "--name", prompt="Project's name", help="Name of the project to add"
)
@click.option(
    "-d",
    "--description",
    prompt="Project's description",
    help="Description of the project to add",
)
@click.option(
    "-git", "--git_url", prompt="Git Repository (URL)", help="Url of git repository"
)
def add(name, description, git_url):
    project = Projects()
    project = project.create(name, description, git_url)
    table = SingleTable(
        Transform().api_response_to_terminaltables(
            project, include=DEFAULT_DISPLAY_ATTRIBUTES
        )
    )
    table.inner_row_border = True
    table.title = "List of projects"
    click.echo(table.table)


@click.command()
def rm():
    pass


@click.command()
@click.option(
    "-id", "--id", default=None, type=int, help="Returns project with a specified id"
)
def ls(id):
    projects = Projects().get_all()

    table = SingleTable(
        Transform().api_response_to_terminaltables(
            projects, include=DEFAULT_DISPLAY_ATTRIBUTES
        )
    )
    table.inner_row_border = True
    table.title = "List of projects"
    click.echo(table.table)


#     if id:
#         projects = Projects().get(id)
#         include = [
#             "id"
#         ]
#     else:
#         projects = Projects().get_all()
#         include = DEFAULT_DISPLAY_ATTRIBUTES
#     if projects:
#         table = SingleTable(
#             Transform().api_response_to_terminaltables(
#                 projects, include=DEFAULT_DISPLAY_ATTRIBUTES
#             )
#         )
#         table.inner_row_border = True
#         table.title = "Most recently uploaded models"
#         click.echo(table.table)


projects.add_command(add)
projects.add_command(rm)
projects.add_command(ls)
