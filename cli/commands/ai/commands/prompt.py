""" Optimize the database """

from typing import Annotated, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print


def prompt(
    prompt: Annotated[str, typer.Argument(help="Prompt.")],
    output: Annotated[
        Optional[typer.FileTextWrite],
        typer.Option(
            "--output",
            "-o",
            help="Output file to write the response to.",
            encoding="utf-8",
        ),
    ] = None,
    model: Annotated[
        Optional[str],
        typer.Option(
            "--model",
            "-m",
            help="The model to run inference with. Can be a model id hosted on the "
            "Hugging Face Hub, e.g. meta-llama/Meta-Llama-3-8B-Instruct or a URL "
            "to a deployed Inference Endpoint.",
        ),
    ] = "meta-llama/Meta-Llama-3-8B-Instruct",
) -> None:
    """
    Prompt typer-cli AI.

    Examples:

    ```console
    # Interact with typer-cli AI
    typer-cli ai prompt "How to install Rust?"

    # Interact with typer-cli AI using a specific model
    typer-cli ai prompt "Build a PyTorch KNN classifier" -m meta-llama/Llama-3.2-3B-Instruct
    ```
    """

    client = InferenceClient(model)

    try:
        response = client.chat_completion(
            messages=[{"role": "user", "content": prompt}], max_tokens=2048
        )

        if output:
            with output as file:
                file.write(response.choices[0].message.content)

            print(f"Output [bold green]saved[/bold green] to {output.name}.")
            return

        print(f"[bold green]AI[/bold green]: {response.choices[0].message.content}")

    except Exception as error:
        print(f"[bold red]Error[/bold red]: {error}")
