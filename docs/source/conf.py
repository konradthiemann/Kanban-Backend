import os
import sys
import django


sys.path.insert(0, os.path.abspath('../../'))
# line below is recommended by copilot
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kanbanBackend.settings")
# line below is recommended by chatgpt
# os.environ['DJANGO_SETTINGS_MODULE'] = 'kanbanBackend.settings'
django.setup()

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Kanban Backend'
copyright = '2024, Konrad Thiemann'
author = 'Konrad Thiemann'
release = '31.05.2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
