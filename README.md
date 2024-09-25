# Typer CLI Template

[![Continuous Integration](https://github.com/youzarsiph/typer-cli-template/actions/workflows/ci.yml/badge.svg)](https://github.com/youzarsiph/typer-cli-template/actions/workflows/ci.yml)
[![Continuous Deployment](https://github.com/youzarsiph/typer-cli-template/actions/workflows/cd.yml/badge.svg)](https://github.com/youzarsiph/typer-cli-template/actions/workflows/cd.yml)
[![Black](https://github.com/youzarsiph/typer-cli-template/actions/workflows/black.yml/badge.svg)](https://github.com/youzarsiph/typer-cli-template/actions/workflows/black.yml)
[![Ruff](https://github.com/youzarsiph/typer-cli-template/actions/workflows/ruff.yml/badge.svg)](https://github.com/youzarsiph/typer-cli-template/actions/workflows/ruff.yml)

This template is designed to accelerate the development of command-line interfaces (CLI) using Typer.

## Features

- User-friendly implementation
- Enhanced color and style options
- Integrated CI/CD capabilities
- Automated lint checks
- Format validation

## Getting Started

To initiate your project, clone the repository:

```bash
git clone https://github.com/youzarsiph/typer-cli-template
cd typer-cli-template
```

### Install Poetry

First, install Poetry, a dependency management tool for Python:

```bash
pip install poetry
```

### Install Dependencies

Next, install the necessary dependencies:

```bash
poetry install
poetry build
poetry shell
```

### Running the Application

You can run the application and access the help command via:

```bash
typer-cli --help
```

## Project Structure

The project is organized as follows:

```plaintext
typer-cli-template
│   .gitignore
│   LICENSE
│   poetry.lock
│   pyproject.toml  # Contains project metadata such as name, version, and dependencies
│   README.md
│
├───.github
│   └───workflows  # Directory for GitHub Actions
│           black.yml
│           cd.yml
│           ci.yml
│           ruff.yml
│
└───cli
    │   main.py  # Central hub for your CLI application
    │   __init__.py
    │   __main__.py  # Enables execution via `python -m typer-cli-template`
    │
    └───commands  # Directory for individual command implementations
            echo.py
            hello.py
            __init__.py
```

## Adding a New Command

To create a new command, generate a new file within the `cli/commands` directory:

```bash
touch cli/commands/ls.py
```

### Implementing the Command

Here’s an example of a function to list files in a specified directory:

```python
""" List all files in the specified path """

import os
from pathlib import Path
from typing import Annotated
import typer
from rich import print


def ls(
    path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            dir_okay=True,
            help="Specify the path to list files.",
        ),
    ] = "."
) -> None:
    """
    Lists files within the specified path.

    Args:
        path (Path): The directory path to list files.
    """

    print(f"Files in {path.resolve()}:")
    print("-------------------------")
    for file in os.listdir(path):
        print(file)
```

### Registering the Command

To make the command accessible, edit the `command_list` in `cli/commands/__init__.py`:

```python
""" Command Definitions """

from cli.commands.echo import echo
from cli.commands.hello import hello
from cli.commands.ls import ls  # Register the new command

# Compile a list of available commands
command_list = [echo, hello, ls]
```

### Running the Application Again

Finally, you can run the application to see the newly added command:

```bash
typer-cli --help
```

## License

This project is licensed under the MIT License.
