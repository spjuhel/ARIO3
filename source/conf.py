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
import os
import sys
sys.path.insert(0, os.path.abspath('../'))


# -- Project information -----------------------------------------------------

project = 'ARIO3'
copyright = '2022, Samuel Juhel'
author = 'Samuel Juhel'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon', 'sphinx.ext.intersphinx']

napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# automatically generate api references
autosummary_generate = ["api_references.rst"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The entries in this file are checked regularly for validity via the Github Action
# sited at github.com/bskinn/intersphinx-gist.
# Please feel free to post an issue at that repo if any of these mappings don't work for you,
# or if you're having trouble constructing a mapping for a project not listed here.
intersphinx_mapping = {
	"python": ('https://docs.python.org/3/', None),
	"matplotlib": ('https://matplotlib.org/stable/', None),
	"numpy": ('https://numpy.org/doc/stable/', None),
	"pandas": ('https://pandas.pydata.org/docs/', None),
	"pymrio": ('https://pymrio.readthedocs.io/en/latest/', None)
}

html_js_files = [
    'js/custom.js'
]

add_module_names = False