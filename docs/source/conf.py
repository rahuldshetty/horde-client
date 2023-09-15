# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from datetime import datetime

project = 'horde-client'
copyright = f'{datetime.now().year}, Rahul D Shetty'
author = 'Rahul D Shetty'

source_suffix = ".md"
master_doc = "index"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser"
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

templates_path = ['_templates']
exclude_patterns = ["_build"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Theme based options
# https://alabaster.readthedocs.io/en/latest/customization.html
html_theme_options = {
    "description": "Easy-to-use Python Interface for KoboldAI Horde",
    'github_button': True,
    'github_user': 'rahuldshetty',
    'github_repo': 'horde-client',


    "fixed_sidebar": True,
    'sidebar_width': '220px',

    'base_text': '#3E4349',
    'body_text': '#3E4349',
    'font_family': 'Georgia, serif',
    'font_size': '17px',
    'head_font_family': 'Georgia, serif',
}