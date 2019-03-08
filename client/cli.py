import click


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--workspace", prompt="Workspace name", help="Name of the selected workspace"
)
@click.option("--project", prompt="Project name", help="Name of the selected project")
@click.option("--version", prompt="Model version", help="Version of the selected model")
@click.option("--model", prompt="Model filename", help="Filename of the selected model")
def download(workspace, project, version, model):
    """Downloads requested model."""
    print("Downloading model...")


@click.command()
@click.option(
    "--workspace", prompt="Workspace name", help="Name of the model to upload"
)
@click.option("--project", prompt="Project name", help="Name of the model to upload")
@click.option("--version", prompt="Model version", help="Version of the model to upload")
@click.option("--model", prompt="Model filename", help="Filename of model to upload")
def upload(workspace, project, version, model):
    """Uploads a given model."""
    print("Uploading model...")


@click.command()
# @click.argument('--list/--graph', default=False,
# help="Lists all available workspaces")
def workspaces():
    """Lists available workspaces."""
    print("Listing workspaces...")


cli.add_command(upload)
cli.add_command(download)
cli.add_command(workspaces)

if __name__ == "__main__":
    cli()
