# Typer CLI Template

![Continuous Integration](https://github.com/youzarsiph/typer-cli-template/actions/workflows/ci.yml/badge.svg)
![Continuous Deployment](https://github.com/youzarsiph/typer-cli-template/actions/workflows/cd.yml/badge.svg)
![Code Style: Black](https://github.com/youzarsiph/typer-cli-template/actions/workflows/black.yml/badge.svg)
![Code Quality: Ruff](https://github.com/youzarsiph/typer-cli-template/actions/workflows/ruff.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Introduction

The Typer CLI Template is a robust framework designed to expedite the development of command-line interfaces (CLIs) using the [Typer](https://typer.tiangolo.com/) library. This template is meticulously crafted to offer an optimal development experience, equipped with features that align with contemporary software engineering practices.

## Key Features

- **Intuitive Design**: Minimizes the learning curve, making it accessible to users of all levels.
- **Enhanced Console Output**: Utilizes [Rich](https://rich.readthedocs.io/) for visually appealing and informative console displays.
- **Automated CI/CD Pipelines**: Ensures seamless integration and deployment with comprehensive testing workflows.
- **Code Quality Assurance**: Automated lint checks powered by [Ruff](https://ruff.rs/) maintain high code standards.
- **Consistent Code Formatting**: Adheres to style guidelines enforced by [Black](https://black.readthedocs.io/).

## Getting Started

### Prerequisites

Ensure the following prerequisites are installed on your system:

- **Python 3.10 or Later**: Essential for running the application.
- **Git**: Facilitates source control management.

### Repository Cloning

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/youzarsiph/typer-cli-template.git
cd typer-cli-template
```

### Dependency Installation

1. **Install Poetry**: Manage dependencies and packaging efficiently with Poetry. Install it using pip:

   ```bash
   pip install poetry
   ```

2. **Install Project Dependencies**: Use Poetry to install the necessary dependencies and build the package:

   ```bash
   poetry install
   poetry build
   ```

3. **Activate Virtual Environment**: Activate the virtual environment with the following command:

   ```bash
   poetry shell
   ```

### Executing the Application

Run the application and access the help command to view available options:

```bash
typer-cli --help
```

## Project Structure

The project is organized as follows:

```plaintext
typer-cli-template/
├── .gitignore
├── LICENSE
├── poetry.lock
├── pyproject.toml
│   └── Contains project metadata, dependencies, and other configurations.
├── README.md
├── .github/
│   └── workflows/
│       ├── black.yml
│       ├── cd.yml
│       ├── ci.yml
│       └── ruff.yml
│           └── GitHub Actions configurations for CI/CD and code quality.
└── cli/
    ├── __init__.py
    ├── __main__.py
    │   └── Entry point for executing the application as a module.
    ├── main.py
    │   └── Central entry point for the CLI application.
    └── commands/
        ├── echo.py
        ├── hello.py
        ├── ls.py
        └── __init__.py
            └── Registers available commands.
```

## Extending Functionality

### Adding a New Command

To introduce new functionality, create a Python file within the `cli/commands` directory:

```bash
touch cli/commands/ls.py
```

#### Implementing the Command

Here is an example implementation for a command to list files in a specified directory:

```python
"""List all files in the specified path"""

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
            help="Specify the directory from which to list files.",
        ),
    ] = "."
) -> None:
    """
    Lists files within the specified directory path.
    """
    print(f"Files in {path.resolve()}:")
    print("-------------------------")
    for file in os.listdir(path):
        print(file)
```

#### Registering the Command

To make the new command accessible, add it to the `command_list` in `cli/commands/__init__.py`:

```python
"""Command Definitions"""

from cli.commands.echo import echo
from cli.commands.hello import hello
from cli.commands.ls import ls  # Include the newly added command

# List of available commands
command_list = [echo, hello, ls]
```

### Testing the New Command

Run the application to verify that the new functionality is operational:

```bash
typer-cli --help
```

## Contributing

Contributions from the community are highly encouraged. To contribute to the Typer CLI Template, follow these steps:

1. **Fork the Repository**: Create a fork of the repository.
2. **Create a Branch**: Develop your changes in a new branch.
3. **Commit Changes**: Stage and commit your modifications.
4. **Push Changes**: Upload your changes to your fork.
5. **Submit a Pull Request**: Provide a detailed description of your changes.

## Licensing

The Typer CLI Template is released under the MIT License. For full licensing details, please see the [LICENSE](LICENSE) file.

## Contact

For inquiries or feedback, contact us via:

- **GitHub Issues**: [Open an issue](https://github.com/youzarsiph/typer-cli-template/issues) for bug reports or feature requests.
- **Maintainer**: Yousuf Abu Shanab

---

For additional support and documentation, visit the [project repository on GitHub](https://github.com/youzarsiph/typer-cli-template).
