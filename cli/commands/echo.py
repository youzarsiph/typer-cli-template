""" Echo command """

from typing import Annotated
import typer
from rich import print


def echo(text: Annotated[str, typer.Argument(help="Text to echo")]) -> None:
    """
    Echo given text.

    Args:
        text (str): Text to echo.
    """

    print(text)
