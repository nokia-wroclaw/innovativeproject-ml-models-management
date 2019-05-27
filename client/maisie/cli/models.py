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


# @click.command()
# @click.option(
#     "-id", "--id", prompt="Model's id", type=int, help="Downloads model with a specified id"
# )
# def download(id):
#     model = Models().download(id)
#     with open('some_file.json', 'wb') as some_file:
#         pickle.dump(model, some_file)


@click.command()
@click.option(
    "-id", "--id", default=None, type=int, help="Returns model with a specified id"
)
@click.option(
    "-hp", "--hyperparameter", default=None, help="Sorts by given hyperparameter"
)
@click.option("-p", "--parameter", default=None, help="Sorts by given parameter")
@click.option("-s", "--sort", default=None, help="Sorts by given key : *key:desc*")
@click.option(
    "-d", "--download", prompt="Download model?[y/n]", help="Downloads chosen model "
)
def ls(id, hyperparameter, parameter, sort, download):
    if id:
        models = Models().get(id)
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
        if download in ("y", "Y", "yes", "Yes"):
            file_name = input("File name: ")
            with open(file_name, "wb") as file_name:
                pickle.dump(models, file_name)


models.add_command(upload)
# models.add_command(download)
models.add_command(ls)
