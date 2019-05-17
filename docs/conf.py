# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../backend/"))
sys.path.insert(0, os.path.abspath("../client/"))


# -- Project information -----------------------------------------------------

project = "Maisie"
copyright = "2019, Zofia Kochutek, Łukasz Kleczaj, Marek Kochanowski"
author = "Zofia Kochutek, Łukasz Kleczaj, Marek Kochanowski"

# The full version, including alpha/beta/rc tags
release = "0.1.1"
html_title = "Maisie Documentation"
html_short_title = "Maisie"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinxcontrib.autoprogram",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.autohttp.flask",
    "sphinxcontrib.autohttp.flaskqref",
    "sphinx_click.ext",
    "sphinx_autodoc_typehints",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Theme

import maisie_sphinx_theme

html_theme_path = maisie_sphinx_theme.html_theme_path()
html_theme = "maisie_sphinx_theme"
html_sidebars = {"**": ["logo-text.html", "globaltoc.html", "searchbox.html"]}
# Register the theme as an extension to generate a sitemap.xml
extensions.append("maisie_sphinx_theme")

# Maisie theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "Maisie"
}


def setup(app):
    app.add_stylesheet("css/overwrite.css")

