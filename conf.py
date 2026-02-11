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
    "new-components-api/index": "https://docs.pypsa.org/latest/user-guide/components/#new-components-class-api",
    "options-params/index": "https://docs.pypsa.org/latest/user-guide/options/#parameters-options",
    "release-notes/index": "https://docs.pypsa.org/latest/release-notes/",
    "discord/index": "https://discord.com/invite/AnuJBk23FU",
    "users/index": "https://docs.pypsa.org/latest/home/users/",
    "stoch-opt/index": "https://docs.pypsa.org/latest/user-guide/optimization/stochastic/",
    "v1/index": "https://docs.pypsa.org/latest/user-guide/v1-guide/",
    "transmission-losses/index": "https://docs.pypsa.org/latest/user-guide/optimization/power-flow/#loss-approximation",
    "warning-attr-misleading/index": "https://docs.pypsa.org/latest/user-guide/warnings/#warning-attr-misleading",
    "warning-attr-typo/index": "https://docs.pypsa.org/latest/user-guide/warnings/#warning-attr-typo",
}
