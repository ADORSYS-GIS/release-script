from src.realease import app as release_app
from typer import Typer

global_app = Typer()

# https://typer.tiangolo.com/tutorial/subcommands/nested-subcommands/
# Adding a subcommand to a subcommand is done by calling add_typer() on the parent app.
global_app.add_typer(release_app, name="release")

@global_app.command()
def say_hello(to: str) -> None:
    """
    Say hello to TO, optionally with a

    Args:
        to (str): The person to say hello to
    """
    print(f"Hello {to}")

if __name__ == '__main__':
    global_app()