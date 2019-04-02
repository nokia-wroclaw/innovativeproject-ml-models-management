import click, requests

url = "http://nokia-projekt:5000"


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
    # print("Downloading model...")
    payload = {
        "workspace": workspace,
        "project": project,
        "model": model,
        "version": version,
    }
    r = requests.get(url, params=payload)
    model = r.text


@click.command()
@click.option(
    "--workspace", prompt="Workspace name", help="Name of the model to upload"
)
@click.option("--project", prompt="Project name", help="Name of the model to upload")
@click.option(
    "--version", prompt="Model version", help="Version of the model to upload"
)
@click.option(
    "--model", prompt="Model filename", help="Filename of the model to upload"
)
def upload(workspace, project, version, model):
    """Uploads a given model."""
    # print("Uploading model...")
    payload = {
        "workspace": workspace,
        "project": project,
        "model": model,
        "version": version,
    }
    r = requests.post(url, data=payload)


@click.command()
# @click.argument('--list/--graph', default=False,
# help="Lists all available workspaces")
def graph():
    r = requests.get(url)
    r_dict = r.json()
    click.echo(r.dict["form"])


@click.command()
@click.option(
    "--workspace",
    prompt="Workspace name",
    help="Name of the workspace, which projects will be listed",
)
def projects():
    payload = {"project": workspace}
    r = requests.get(url, params=payload)
    r_dict = r.json()
    click.echo(f"Projects of workspace: {workspace}: \n {r.dict['form']}")


@click.command()
@click.option(
    "--project",
    prompt="Project name",
    help="Name of the project, which models will be listed",
)
def models():
    payload = {"project": project}
    r = requests.get(url, params=payload)
    r_dict = r.json()
    click.echo(f"Models of project {project}: \n {r.dict['form']}")


cli.add_command(upload)
cli.add_command(download)
cli.add_command(projects)
cli.add_command(models)
cli.add_command(graph)

if __name__ == "__main__":
    cli()
