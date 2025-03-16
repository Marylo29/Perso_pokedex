import sys
import os

sys.path.insert(0, os.path.abspath('../../'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pokedex'
copyright = '2025, COLLIN Nicolas'
author = 'COLLIN Nicolas'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',       # Pour générer la documentation à partir des docstrings
    'sphinx.ext.viewcode',      # Pour ajouter des liens vers le code source
    'sphinx.ext.napoleon'       # Pour prendre en charge les docstrings au format Google ou NumPy
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Thème HTML
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options pour les extensions ---------------------------------------------

# Configuration de l'extension autodoc
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# Configuration de l'extension napoleon
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True