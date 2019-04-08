import click

from terminaltables import SingleTable

from mlmm import Models
from mlmm.utils.misc import Transform


@click.group()
def models():
    pass


@click.command()
def upload(name, model, hyperparameters, parameters, metrics, dataset_name):
    """Uploads a given model."""
    models = Models(
        {
            "api_url": "https://ml.kochanowski.dev/api/v1",
            "auth_user_login": "Nokia",
            "auth_user_password": "Nokiademo2019",
            "selected_project": 1,
        }
    )
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
    models = Models(
        {
            "api_url": "https://ml.kochanowski.dev/api/v1",
            "auth_user_login": "Nokia",
            "auth_user_password": "Nokiademo2019",
        }
    )
    table = SingleTable(
        Transform().api_response_to_terminaltables(
            models.get_all(),
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
