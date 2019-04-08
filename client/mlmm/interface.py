import click

from mlmm.cli.models import models
from mlmm.cli.projects import projects
from mlmm.cli.users import users
from mlmm.cli.workspaces import workspaces


@click.group()
def cli():
    pass


cli.add_command(models)
cli.add_command(projects)
cli.add_command(users)
cli.add_command(workspaces)

if __name__ == "__main__":
    cli()
