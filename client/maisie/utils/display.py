import click
from terminaltables import SingleTable
from maisie.utils.misc import Transform
from colorama import Fore


class Display:
    def __init__(self, context, response, attributes, title):
        self.response = response
        self.attributes = attributes
        self.title = title
        self.context = context

    def set_colors(self, table):
        schema = [None] * len(self.attributes)
        for counter, attribute in enumerate(self.attributes):
            if attribute == "user" or attribute == "login":
                schema[counter] = Fore.MAGENTA
            elif attribute == "created":
                schema[counter] = Fore.GREEN
        table = Transform().apply_beautiful_colors(obj=table, schema=schema)
        return table

    def create_table(self):
        table = Transform().api_response_to_terminaltables(
            self.response, include=self.attributes
        )
        table = self.set_colors(table)
        table = SingleTable(table)
        table.inner_row_border = True
        table.title = self.title
        return table.table

    def display_response(self):
        content_to_display = self.response
        if not self.context.obj["output"] == "json":
            content_to_display = self.create_table()
        click.echo(content_to_display)
