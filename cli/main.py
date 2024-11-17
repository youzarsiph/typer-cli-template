""" Typer CLI Template """

import typer
from cli.commands import command_list
from cli.commands.ai.app import ai


# CLI
app = typer.Typer(
    name="typer-cli",
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="Typer CLI Template",
)

# Add ai subcommand
app.add_typer(ai)

for command in command_list:
    app.command(no_args_is_help=True)(command)


if __name__ == "__main__":
    app()
