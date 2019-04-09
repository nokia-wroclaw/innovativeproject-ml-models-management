import click

from terminaltables import SingleTable

from maisie import Models
from maisie.utils.misc import Transform


@click.group()
def models():
    pass


@click.command()
@click.option(
    "--name", prompt="Model name", help="Name of the model to upload"
)
@click.option("--model", prompt="Model (file)", help="Filename of the model to upload")
@click.option(
    "--hyperparameters",
    prompt="Hyperparameters (file)",
    help="Filename of the hyperparameters bound to the model",
)
@click.option(
    "--parameters",
    prompt="Parameters (file)",
    help="Filename of the parameters bound to the model",
)
@click.option(
    "--metrics", prompt="Metrics (file)", help="Filename of the metrics bound to model"
)
@click.option(
    "--dataset_name", prompt="Dataset name", help="Name of the dataset used in model"
)
def upload(name, model, hyperparameters, parameters, metrics, dataset_name):
    """Uploads a given model."""
    models = Models()
    models.upload(
        name=name,
        filename=model,
        hyperparameters=hyperparameters,
        parameters=parameters,
        metrics=metrics,
        dataset_name=dataset_name,
    )


@click.command()
def download():
    pass


@click.command()
def ls():
    models = Models().get_all()
    if models:
        table = SingleTable(
            Transform().api_response_to_terminaltables(
                models,
                include=[
                    "id",
                    "user",
                    "visibility",
                    "created",
                    "hyperparameters",
                    "parameters",
                    "metrics",
                ],
            )
        )
        table.inner_row_border = True
        table.title = "Most recently uploaded models (1 to 20)"
        click.echo(table.table)


models.add_command(upload)
models.add_command(download)
models.add_command(ls)
