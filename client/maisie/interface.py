import click

from maisie.cli.models import models
from maisie.cli.projects import projects
from maisie.cli.users import users
from maisie.cli.workspaces import workspaces


@click.group()
def cli():
    pass


cli.add_command(models)
cli.add_command(projects)
cli.add_command(users)
cli.add_command(workspaces)

if __name__ == "__main__":
    cli()
