# Configuration file for the Sphinx documentation builder.
from datetime import datetime

# -- Project information -----------------------------------------------------
project = "olist-deep-dive"
copyright = f"{datetime.now().year}, Pavel Grigoryev"
author = "Pavel Grigoryev"
language = "en"
# -- General configuration ---------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "myst-markdown",
    ".ipynb": "myst-nb",
}

extensions = [
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx.ext.intersphinx",
]

# Plotly configuration
plotly_include_source = True
plotly_html_show_formats = False
plotly_html_show_sourcelink = False
plotly_preview = True

# MyST-NB configuration for Jupyter notebooks
nb_execution_mode = "auto"
nb_execution_timeout = -1
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_admonition",
    "html_image",
    "colon_fence",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]


templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "_pre_run.ipynb",
    "_post_run.ipynb",
]

html_sidebars = {}

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_title = "🌊 Olist Deep Dive"
html_short_title = "🌊 Olist Deep Dive"
# Theme options

html_theme_options = {
    "use_edit_page_button": False,
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "home_page_in_toc": False,
    "use_fullscreen_button": True,
    "use_download_button": True,
    "use_repository_button": True,
    "path_to_docs": "",
    "repository_url": "https://github.com/PavelGrigoryevDS/olist-deep-dive",
    "logo": {
        "image_light": "_static/logo-light.png",
        "image_dark": "_static/logo-dark.png",
    },
    "toc_title": "On this page",
    "pygments_light_style": "tango",
    "pygments_dark_style": "monokai",
}


def setup(app):
    app.add_css_file("custom.css")
    app.add_js_file("custom.js")
