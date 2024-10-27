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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Notebooks for Operations Research'
title = 'Notebooks for Operations Research'
subtitle = 'A practical guide to operations research with Python'
copyright = '2024, Francisco Fraile'
author = 'Francisco Fraile'

# The full version, including alpha/beta/rc tags
release = 'I'

# The logo
html_logo = '_static/logo.png'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['nbsphinx', 'myst_parser', 'sphinx_design', 'sphinx_copybutton', 'sphinxext.opengraph']

# Add myst extensions to enable admonitions, and image attributes (e.g. width)
myst_enable_extensions = ["attrs_inline", "attrs_image", "colon_fence", "html_admonition"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Source suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

nbsphinx_execute = 'never'

## Latex engine to support unicode characters
latex_engine = "lualatex"


latex_elements = {
    'preamble': r'''
        \usepackage{svg}
        \usepackage{titlesec}
        \usepackage{xcolor}

        % Customize level 5 (\paragraph) - Same color and size as paragraph text, underlined
        \titleformat{\paragraph}
            {\normalfont\bfseries\normalsize\color{black}}{\theparagraph}{1em}{}
            
        % Customize level 6 (\subparagraph) - Same color and size as paragraph text, underlined
        \titleformat{\subparagraph}
            {\normalfont\normalsize\color{black}}{\theparagraph}{1em}{}

        % Optional: Control spacing around the headings
        \titlespacing*{\subsubsection}{0pt}{1.5ex plus .1ex minus .2ex}{1ex}
        \titlespacing*{\paragraph}{0pt}{1.5ex plus .1ex minus .2ex}{1ex}
    ''',
    'maketitle': '\\input{./cover.tex}'
}

root_doc = 'index'
latex_documents = [
    (root_doc, 'or-notebooks.tex', 'Notebooks for Operations Research',
     'Francisco Fraile', 'manual'),
]