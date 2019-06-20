import click

from colorama import init as colorama_init

from maisie.cli.models import models
from maisie.cli.projects import projects
from maisie.cli.users import users
from maisie.cli.workspaces import workspaces
from maisie.cli.config import config


@click.group()
@click.option(
    "--output_json", is_flag=True, help="Display output in pure json instead of a table"
)
@click.pass_context
def cli(context, output_json):
    context.obj = {}
    context.obj["output_json"] = False
    if output_json:
        context.obj["output_json"] = True


cli.add_command(models)
cli.add_command(projects)
cli.add_command(users)
cli.add_command(workspaces)
cli.add_command(config)

if __name__ == "__main__":
    colorama_init()
    cli()
