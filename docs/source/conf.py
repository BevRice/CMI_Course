# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Counter Malign Influence: Strategies, Insights, and Tools'
copyright = 'Chaminade University'
author = 'Beverly Rice'
release = '7 March 2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'nbsphinx',
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
html_theme = "sphinx_rtd_theme"

nbsphinx_allow_errors = True  # Allow notebook conversion even with minor errors
nbsphinx_execute = 'always'   # Execute notebooks and generate outputs
html_static_path = ['_static']  # Ensures Sphinx copies static files


