"""Test cases for the __main__ module."""
from click.testing import CliRunner
from pytest import fixture
from {{cookiecutter.root_package}}.{{cookiecutter.package_name}} import __main__


@fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0
