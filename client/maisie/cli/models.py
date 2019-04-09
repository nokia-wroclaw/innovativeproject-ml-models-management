import click

from terminaltables import SingleTable

from maisie import Models
from maisie.utils.misc import Transform


DISPLAY_ATTRIBUTES = [
    "id",
    "user",
    "name",
    "visibility",
    "created",
    "hyperparameters",
    "parameters",
    "metrics",
]


@click.group()
def models():
    pass


@click.command()
@click.option("-n", "--name", prompt="Model name", help="Name of the model to upload")
@click.option("-f", "--file", prompt="Model (file)", help="Filename of the model to upload")
@click.option(
    "-hp",
    "--hyperparameters",
    prompt="Hyperparameters (file)",
    help="Filename of the hyperparameters bound to the model",
)
@click.option(
    "-p",
    "--parameters",
    prompt="Parameters (file)",
    help="Filename of the parameters bound to the model",
)
@click.option(
    "-m",
    "--metrics", prompt="Metrics (file)", help="Filename of the metrics bound to model"
)
@click.option(
    "-d",
    "--dataset_name", prompt="Dataset name", help="Name of the dataset used in model"
)
def upload(name, file, hyperparameters, parameters, metrics, dataset_name):
    """Uploads a given model."""
    models = Models()
    models = models.upload(
        name=name,
        filename=file,
        hyperparameters=hyperparameters,
        parameters=parameters,
        metrics=metrics,
        dataset_name=dataset_name,
    )
    if models:
        table = SingleTable(
            Transform().api_response_to_terminaltables(
                models, include=DISPLAY_ATTRIBUTES
            )
        )
        table.inner_row_border = True
        table.title = "Uploaded model"
        click.echo(table.table)


@click.command()
def download():
    pass


@click.command()
@click.option("-id", "--id", default=None, type=int, help="ID of a selected model")
def ls(id):
    if id:
        models = Models().get(id)
    else: 
        models = Models().get_all()
    if models:
        table = SingleTable(
            Transform().api_response_to_terminaltables(
                models, include=DISPLAY_ATTRIBUTES
            )
        )
        table.inner_row_border = True
        table.title = "Most recently uploaded models"
        click.echo(table.table)


models.add_command(upload)
models.add_command(download)
models.add_command(ls)
