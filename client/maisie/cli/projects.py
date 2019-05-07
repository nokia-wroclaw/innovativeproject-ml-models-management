import click
import logging
from terminaltables import SingleTable
from colorama import Fore

from maisie import Projects
from maisie.utils.misc import Transform

from textwrap import wrap

import os


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
    if id:
        projects = Projects().get(id)
    else:
        projects = Projects().get_all()
    if projects:
        table_to_display = Transform().api_response_to_terminaltables(
            projects, include=DEFAULT_DISPLAY_ATTRIBUTES
        )
        table_to_display = Transform().apply_beautiful_colors(
            obj=table_to_display, schema=[None, Fore.YELLOW, None, None, Fore.GREEN]
        )

        table = SingleTable(table_to_display)
        table.inner_row_border = True
        table.max_width = 10
        table.title = "List of projects"
        ts = os.get_terminal_size()
        terminal_width = ts.columns
        description_width = (3 / 10) * int(terminal_width)
        rest_width = (2 / 10) * int(terminal_width)

        click.echo(table.column_max_width)
        click.echo(table.column_widths)

        for i in range(1, len(table_to_display)):
            for j in range(1, len(table_to_display[i])):
                text_to_wrap = table_to_display[i][j]
                if not text_to_wrap is None:
                    if j == 2:
                        max_width = int(description_width)
                    else:
                        max_width = int(rest_width)
                    wrapped_string = "\n".join(wrap(text_to_wrap, max_width))
                    table.table_data[i][j] = wrapped_string

        click.secho(table.table)


projects.add_command(add)
projects.add_command(rm)
projects.add_command(ls)
