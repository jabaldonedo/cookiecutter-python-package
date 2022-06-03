"""Nox configuration file."""

from nox import session
from nox.sessions import Session


locations = ["src", "test", "noxfile.py"]


@session
def tests(session: Session) -> None:
    """Run tests using pytest.

    :param session: The Session object
    """
    session.install("pytest", "pytest-cov", "toml")
    session.install(".")
    session.run("pytest", "--cov-report", "term-missing", "--cov", "{{cookiecutter.root_package}}.{{cookiecutter.package_name}}")


@session
def black(session: Session) -> None:
    """Run black code formatter.

    :param session: The Session object
    """
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@session()
def lint(session: Session) -> None:
    """Lint using flake8.

    :param session: The Session object.
    :type session: Session
    """
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-annotations",
        "flake8-black",
        "flake8-bandit",
        "flake8-bugbear",
        "flake8-builtins",
        "flake8-comprehensions",
        "flake8-docstrings",
        "flake8-import-order",
        "flake8-rst-docstrings",
        "isort",
        "pep8-naming",
    )
    session.run("isort", *args)
    session.run("flake8", *args)


@session
def mypy(session: Session) -> None:
    """Run static code analysis using mypy.

    :param session: The Session object
    """
    args = session.posargs or locations[:-1]
    session.install("mypy", "pytest", "types-toml")
    session.install(".")
    session.run("mypy", *args)


@session
def docs(session: Session) -> None:
    """Build documentation.

    :param session: The Session object
    """
    session.install("sphinx", "sphinx-autodoc-typehints", "furo", "toml")
    session.run("sphinx-build", "doc/src", "doc/build")
