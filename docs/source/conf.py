# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'data-structures'
copyright = '2025, Emre Kahraman CANIKOGLU'
author = 'Emre Kahraman CANIKOGLU'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # For Google-style docstrings
    'sphinx_autodoc_typehints',
    "sphinx_rtd_theme",
    "sphinx.ext.githubpages",
]

# Set theme (optional but recommended)
html_theme = 'sphinx_rtd_theme'

# Add your project to the Python path
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))  # Adjust based on your project structure

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

import sphinx_rtd_theme

html_baseurl = "https://999-juicewrld.github.io/data_structures/"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "style_external_links": True,
}
