from typer.testing import CliRunner
from app import global_app

runner = CliRunner()

def test_say_hello():
    result = runner.invoke(global_app, ["say-hello", "Banana"])
    assert result.exit_code == 0
    assert "Hello Banana" in result.stdout