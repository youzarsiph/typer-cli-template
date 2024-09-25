""" Hello command """

from typing import Annotated
import typer
from rich import print


def hello(
    name: Annotated[
        str, typer.Option("--name", "-n", help="Name to say hello to.")
    ] = None
) -> None:
    """
    Say hello to the given name.

    Args:
        name (str): Name to say hello to.
    """

    print(f"Hello, [bold green]{name}[/bold green]")
