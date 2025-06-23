# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'PyPSA Redirects'
copyright = '2025, PyPSA'
author = 'PyPSA'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_reredirects',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ------------------------------------------------
html_theme = 'basic'
html_static_path = []

# -- Redirects configuration ------------------------------------------------
redirects = {
    "test-redirect/index": "https://google.com"
}
