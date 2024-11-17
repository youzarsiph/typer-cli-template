""" AI app """

import typer

from cli.commands.ai.commands import ai_commands


# AI app
ai = typer.Typer(
    name="ai",
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="[bold]AI[/bold] subcommand",
)

for command in ai_commands:
    ai.command(no_args_is_help=True)(command)
