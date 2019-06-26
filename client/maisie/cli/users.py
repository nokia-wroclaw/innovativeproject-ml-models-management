import click
import logging

from maisie import Users
from maisie.utils.display import Display


DEFAULT_DISPLAY_ATTRIBUTES = ["id", "login", "full_name", "email"]


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
@click.pass_context
def add(context, login, name, email, password):
    user = Users().create(login, name, email, password)
    title = "User"
    display = Display(
        context=context,
        response=users,
        attributes=DEFAULT_DISPLAY_ATTRIBUTES,
        title=title,
    )
    display.display_response()


@click.command()
def rm():
    pass


@click.command()
@click.option(
    "-id", "--id", default=None, type=int, help="Returns user with a specified id"
)
@click.pass_context
def ls(context, id):
    if id:
        users = Users().get(id)
    else:
        users = Users().get_all()

    if users:
        title = "List of users"
        display = Display(
            context=context,
            response=users,
            attributes=DEFAULT_DISPLAY_ATTRIBUTES,
            title=title,
        )
        display.display_response()


users.add_command(add)
users.add_command(rm)
users.add_command(ls)
