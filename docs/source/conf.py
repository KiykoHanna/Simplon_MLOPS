# Configuration file for the Sphinx documentation builder.
# Adapted for CI/CD pipelines

import os
import sys

# -- Path setup --------------------------------------------------------------
sys.path.insert(0, os.path.abspath("../../app_api"))
sys.path.insert(0, os.path.abspath("../../app_front"))

# -- Project information -----------------------------------------------------
project = "Simplon_MLOps"
copyright = "2026, Hanna Kiyko"
author = "Hanna Kiyko"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",           # core autodoc
    "sphinx.ext.napoleon",          # supports Google & NumPy docstrings
    "sphinx_autodoc_typehints",     # type hints
    "sphinx.ext.autosummary",       # generate summary tables
    "sphinx.ext.viewcode",          # add links to source code
    "myst_parser",                  # Markdown support
]

# Generate autosummary files automatically
autosummary_generate = True

# Type hints in descriptions
autodoc_typehints = "description"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
    "special-members": "__init__",
    "inherited-members": True,
}

# Templates and exclude patterns
templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]

# Myst parser options
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3

