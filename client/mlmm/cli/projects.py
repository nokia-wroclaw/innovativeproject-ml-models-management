import click

from terminaltables import SingleTable

from mlmm import Projects
from mlmm.utils.misc import Transform

@click.group()
def projects():
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


projects.add_command(add)
projects.add_command(rm)
projects.add_command(ls)