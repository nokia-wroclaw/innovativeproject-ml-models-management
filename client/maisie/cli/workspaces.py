import click

from terminaltables import SingleTable

from maisie import Workspaces
from maisie.utils.misc import Transform

@click.group()
def workspaces():
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

workspaces.add_command(add)
workspaces.add_command(rm)
workspaces.add_command(ls)