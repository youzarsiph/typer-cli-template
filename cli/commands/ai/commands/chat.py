""" AI Chat  """

from typing import Annotated, Dict, List, Literal, Optional
import typer
from huggingface_hub import InferenceClient
from rich import print


def chat(
    model: Annotated[
        Optional[str],
        typer.Option(
            "-m",
            "--model",
            help="The model to run inference with. Can be a model id hosted on the "
            "Hugging Face Hub, e.g. meta-llama/Meta-Llama-3-8B-Instruct or a URL "
            "to a deployed Inference Endpoint.",
        ),
    ] = "meta-llama/Meta-Llama-3-8B-Instruct",
) -> None:
    """
    Engage in a chat session with given model.

    Examples:

    ```shell
    # Start chatting
    typer-cli ai chat --

    # Change the model
    typer-cli ai chat -m meta-llama/Llama-3.1-8B-Instruct
    ```
    """

    client = InferenceClient(model)
    messages: List[Dict[Literal["role", "content"], str]] = []

    print("[bold green]AI[/bold green]: Hi, how I can assist you today?")

    while True:
        message = typer.prompt(typer.style("You", fg=typer.colors.MAGENTA, bold=True))

        if message.lower() in ("exit", "quit"):
            break

        messages.append({"role": "user", "content": message})

        try:
            response = client.chat_completion(messages=messages, max_tokens=2048)
            llm_message = str(response.choices[0].message.content)
            messages.append({"role": "assistant", "content": llm_message})

            print(f"[bold green]AI[/bold green]: {llm_message}")

        except Exception as error:
            print(f"[bold red]Error[/bold red]: {error}")
            break
