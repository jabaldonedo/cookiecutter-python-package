"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
from pathlib import Path
from sys import path
from toml import load


conf_path = Path(__file__)
main_path = conf_path.parent.joinpath("../../").resolve().absolute()
package_path = main_path.joinpath("src")
pyproject_path = main_path.joinpath("pyproject.toml")
path.insert(0, str(package_path))

project = "{{cookiecutter.friendly_name}}"
copyright = "{{cookiecutter.copyright_year}}, {{cookiecutter.author}}"  # noqa: A001
author = "{{cookiecutter.author}}"

# The full version, including alpha/beta/rc tags
release = load(pyproject_path)["tool"]["poetry"]["version"]

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.napoleon"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

numfig = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# A boolean that decides whether module names are prepended to all object names
add_module_names = False

python_use_unqualified_type_names = True
