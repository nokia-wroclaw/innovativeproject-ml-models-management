import click

from maisie import Models
from maisie.utils.display import Display


import pickle


DEFAULT_DISPLAY_ATTRIBUTES = ["id", "user", "name", "metrics", "visibility", "created"]


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
@click.pass_context
def upload(context, name, file, hyperparameters, parameters, metrics, dataset_name):
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
        title = "Uploaded model"
        display = Display(
            context=context,
            response=models,
            attributes=DEFAULT_DISPLAY_ATTRIBUTES,
            title=title,
        )
        display.display_response()


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
@click.pass_context
def ls(context, model_id, hyperparameter, parameter, sort):
    if model_id:
        models = Models().get(model_id)
        include = ["hyperparameters", "parameters", "metrics", "_links", "git"]
    else:
        models = Models().get_all()
        include = DEFAULT_DISPLAY_ATTRIBUTES
    if models:
        title = "Most recently uploaded models"
        display = Display(
            context=context, response=models, attributes=include, title=title
        )
        display.display_response()


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
