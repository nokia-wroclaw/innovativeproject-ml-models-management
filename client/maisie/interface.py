import click

from colorama import init as colorama_init

from maisie.cli.models import models
from maisie.cli.projects import projects
from maisie.cli.users import users
from maisie.cli.workspaces import workspaces
from maisie.cli.config import config


@click.group()
@click.option("--output", help="Specify format of the output as e.g. json")
@click.pass_context
def cli(context, output):
    context.obj = {}
    context.obj["output"] = output


cli.add_command(models)
cli.add_command(projects)
cli.add_command(users)
cli.add_command(workspaces)
cli.add_command(config)

if __name__ == "__main__":
    colorama_init()
    cli()
