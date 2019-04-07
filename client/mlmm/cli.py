import ago
import click
import dateutil.parser
from datetime import datetime, timezone
from terminaltables import SingleTable

from mlmm import Models


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
    models = Models()
    models.download(model)


@click.command()
@click.option(
    "--name", prompt="Model (human-readable) name", help="Name of the model to upload"
)
@click.option("--model", prompt="Model (file)", help="Filename of the model to upload")
@click.option(
    "--hyperparameters",
    prompt="Hyperparameters (file)",
    help="Filename of the hyperparameters bound to model",
)
@click.option(
    "--parameters",
    prompt="Parameters (file)",
    help="Filename of the parameters bound to model",
)
@click.option(
    "--metrics", prompt="Metrics (file)", help="Filename of the metrics bound to model"
)
@click.option(
    "--dataset_name", prompt="Dataset name", help="Name of the dataset udes in model"
)
def upload(name, model, hyperparameters, parameters, metrics, dataset_name):
    """Uploads a given model."""
    status = upload_model(
        name=name,
        model=model,
        hyperparameters=hyperparameters,
        parameters=parameters,
        metrics=metrics,
        dataset_name=dataset_name,
        dataset_description="default opis",
        user_id=1,
        project_id=1,
    )
    if status:
        click.echo("Model sent successfuly")


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


@click.command()
def debug():
    models = Models(
        {
            "api_url": "https://ml.kochanowski.dev/api/v1",
            "auth_user_login": "Nokia",
            "auth_user_password": "Nokiademo2019",
        }
    ).get_all()
    table = SingleTable(
        transform_to_terminatables(
            models, include=["id", "user", "visibility", "created", "hyperparameters", "parameters", "metrics"]
        )
    )
    table.title = "Most recently uploaded models (1 to 20)"
    click.echo(table.table)

def transform_single_value(obj):
    if isinstance(obj, dict):
        return dict_to_multiline_string(obj)
    if isinstance(obj, str) and is_date(obj):
        return timestamp_to_human_readable(obj)
    return obj

def is_date(string, fuzzy=False):
    try: 
        dateutil.parser.parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def timestamp_to_human_readable(obj: str) -> str:
    delta = datetime.now(timezone.utc) - dateutil.parser.parse(obj)
    print()
    return ago.human(delta)


def dict_to_multiline_string(obj: dict) -> str:
    result = []

    for key, value in obj.items():
        result.append(f"{key}: {value}")

    return "\n".join(result)


def transform_to_terminatables(obj: list, include=None):
    """Assuming every element of the list contains the same keys."""
    result = []
    for index, entry in enumerate(obj):
        filtered_dict = {key: entry[key] for key in entry if key in include}
        if index == 0:
            result.append(filtered_dict.keys())
        values = filtered_dict.values()
        values = list(
            map(
                lambda x: transform_single_value(x),
                values,
            )
        )
        result.append(values)

    return result


cli.add_command(upload)
cli.add_command(download)
cli.add_command(projects)
cli.add_command(models)
cli.add_command(graph)
cli.add_command(debug)

if __name__ == "__main__":
    cli()
