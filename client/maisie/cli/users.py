import click
import logging
from terminaltables import SingleTable

from maisie import Users
from maisie.utils.misc import Transform


DEFAULT_DISPLAY_ATTRIBUTES = ["id", "login", "name", "email"]


@click.group()
def users():
    pass


@click.command()
@click.option("-l", "--login", prompt="User's login", help="Login of the user to add")
@click.option(
    "-n", "--name", prompt="User's name", help="Description of the project to add"
)
@click.option("-e", "--email", prompt="User's email", help="Email of user to add")
@click.password_option()
def add(login, name, email, password):
    user = Users().create(login, name, email, password)
    table = SingleTable(
        Transform().api_response_to_terminaltables(
            user, include=DEFAULT_DISPLAY_ATTRIBUTES
        )
    )
    table.inner_row_border = True
    table.title = "List of users"
    click.echo(table.table)


@click.command()
def rm():
    pass


@click.command()
@click.option(
    "-id", "--id", default=None, type=int, help="Returns user with a specified id"
)
def ls(id):
    if id:
        users = Users().get(id)
    else:
        users = Users().get_all()

    if users:
        table = SingleTable(
            Transform().api_response_to_terminaltables(
                users, include=DEFAULT_DISPLAY_ATTRIBUTES
            )
        )
        table.inner_row_border = True
        table.title = "List of users"
        click.echo(table.table)


users.add_command(add)
users.add_command(rm)
users.add_command(ls)
