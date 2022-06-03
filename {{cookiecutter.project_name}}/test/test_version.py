"""Test cases for checking versions consistence across project."""
from pathlib import Path
from toml import loads
from {{cookiecutter.root_package}}.{{cookiecutter.package_name}} import __version__


def test_versions() -> None:
    """Test that version is consistent both at __version__ variable and at pyproject."""
    pyproject_toml_path = Path(__file__).parent.joinpath("..", "pyproject.toml").resolve().absolute()
    with open(str(pyproject_toml_path)) as fd:
        content = loads(fd.read())

        assert content["tool"]["poetry"]["version"] == __version__
