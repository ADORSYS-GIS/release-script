from typer import Typer

app = Typer()


@app.command()
def create(
    version: str,
    description: str = "",
    branch: str = "",
    commit: str = ""
):
    """
    Create a new release.

    Args:
        version (str): Version of the release.
        description (str, optional): Description message of the release.
        branch (str, optional): Branch name of the release.
        commit (str, optional): Commit associated to the release.
    """
    pass


@app.command()
def revert(version: str, branch: str):
    pass
