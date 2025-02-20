# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Counter Malign Influence: Strategies, Insights, and Tools'
copyright = '2025, Beverly Rice'
author = 'Beverly Rice'
release = '7 March 2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'nbsphinx',
    'sphinx_rtd_theme',
    'sphinx_thebe'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
html_theme = "sphinx_rtd_theme"

#nbsphinx_execute = 'always'  # Forces execution of notebooks, generating output
#nbsphinx_allow_errors = True  # Allows the site to build even with minor errors
#nbsphinx_output_prompt = 'hidden'  # Hides input/output prompts to clean the display

nbsphinx_allow_errors = True  # Allow notebook conversion even with minor errors
nbsphinx_execute = 'always'   # Execute notebooks and generate outputs
html_static_path = ['_static']  # Ensures Sphinx copies static files


thebe_config = {
    "use_thebe": True,
    "selector": "div.cell",  # Matches Jupyter cells
    "repository_url": "https://github.com/bmgag/CMI_Course",  # Update with your GitHub repo
    "branch": "main",  # Change to the correct branch
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
#html_static_path = ['_static']

