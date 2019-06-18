import click

from terminaltables import SingleTable

from maisie import Models
from maisie.utils.misc import Transform
from colorama import Fore

import pickle


DEFAULT_DISPLAY_ATTRIBUTES = ["id", "user", "name", "created", "metrics", "visibility"]


@click.group()
def models():
    pass


@click.command()
@click.option("-n", "--name", prompt="Model name", help="Name of the model to upload")
@click.option(
    "-f", "--file", prompt="Model (file)", help="Filename of the model to upload"
)
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
    "--metrics",
    prompt="Metrics (file)",
    help="Filename of the metrics bound to model",
)
@click.option(
    "-d",
    "--dataset_name",
    prompt="Dataset name",
    help="Name of the dataset used in model",
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
                models, include=DEFAULT_DISPLAY_ATTRIBUTES
            )
        )
        table.inner_row_border = True
        table.title = "Uploaded model"
        click.echo(table.table)


@click.command()
@click.option(
    "-id",
    "--model_id",
    default=None,
    type=int,
    help="Returns model with a specified id",
)
@click.option(
    "-hp", "--hyperparameter", default=None, help="Sorts by given hyperparameter"
)
@click.option("-p", "--parameter", default=None, help="Sorts by given parameter")
@click.option("-s", "--sort", default=None, help="Sorts by given key : *key:desc*")
def ls(model_id, hyperparameter, parameter, sort):
    if model_id:
        models = Models().get(model_id)
        include = ["hyperparameters", "parameters", "metrics", "_links", "git"]
    else:
        models = Models().get_all()
        include = DEFAULT_DISPLAY_ATTRIBUTES
    if models:
        table = Transform().api_response_to_terminaltables(
            models, include=DEFAULT_DISPLAY_ATTRIBUTES
        )
        table = Transform().apply_beautiful_colors(
            obj=table, schema=[None, Fore.MAGENTA, Fore.YELLOW, None, None, Fore.GREEN]
        )
        table = SingleTable(table)
        table.inner_row_border = True
        table.title = "Most recently uploaded models"
        click.echo(table.table)


@click.command()
@click.option(
    "-id", "--model_id", prompt="Id of model: ", help="Id of model to download"
)
@click.option("-p", "--path", default=None, help="Path to the folder")
def download(model_id, path):
    Models().download(model_id, path)
    click.echo("Model downloaded successfully")


models.add_command(upload)
models.add_command(download)
models.add_command(ls)
