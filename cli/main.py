""" CodePilot CLI """

import typer
from cli.commands import command_list


# CLI
app = typer.Typer(
    name="code-pilot",
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="Typer CLI Template",
)

for command in command_list:
    app.command(no_args_is_help=True)(command)


if __name__ == "__main__":
    app()
