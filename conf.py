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
    "report-bug/index": "https://github.com/PyPSA/PyPSA/issues/new?template=bug_report.yaml",
    "examples/carbon-management.nc/index": "https://tubcloud.tu-berlin.de/s/3qZPGxW3r4HF9Hn/download?path=%2F&files=carbon-management.nc"
}
