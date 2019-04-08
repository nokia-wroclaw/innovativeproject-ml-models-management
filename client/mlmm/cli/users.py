import click

from terminaltables import SingleTable

from mlmm import Users
from mlmm.utils.misc import Transform

@click.group()
def users():
    pass

@click.command()
def add():
    pass

@click.command()
def rm():
    pass

@click.command()
def ls():
    pass

users.add_command(add)
users.add_command(rm)
users.add_command(ls)