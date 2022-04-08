# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sphinx_rtd_theme
import os
import sys

# Extra paths
sys.path.insert(0, os.path.abspath('_ext'))


# -- Project information -----------------------------------------------------

project = 'Wiki'
copyright = '2022, RewardMetin2'
author = 'RewardMetin2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'myst_parser',
	'sphinx_rtd_theme',
	'edit_on_github',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_context = {
  'display_github': True,
  'github_user': 'RewardMetin2',
  'github_repo': 'Wiki',
  'github_version': 'master/docs/',
}

html_logo = "_static/img/logos/128_icon.png"

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': False
}

# CSS Files
html_css_files = [
	'css/custom.css',
	'css/algolia.css',
	'https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css',
	'css/rtd_dark.css'
]

# Javascript files
html_js_files = [
    'js/external-hyperlinks.js'
]

# reST Options
rst_prolog = """
.. include:: <s5defs.txt>

"""


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Pygments configuration
pygments_style = "vs"

# Supress Warning
surpress_warnings = ['autosectionlabel.*']


# Edit on Github configuration
edit_on_github_project = 'username/reponame'
edit_on_github_branch = 'master'
