"""Sphinx configuration for the Ultra Vehicle System manual."""
project = 'Ultra Vehicle System'
author = 'Marcin Szczygliński'
copyright = '2026, Marcin Szczygliński'
version = '1.0.2'
release = '1.0.2'
language = 'en'
root_doc = 'index'
source_suffix = {'.rst': 'restructuredtext'}
extensions = ['sphinx_rtd_theme']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_title = 'Ultra Vehicle System 1.0.2'
html_theme_options = {'navigation_depth': 3, 'collapse_navigation': True}
html_show_sourcelink = False
html_context = {
    'display_github': True,
    'github_user': 'szczyglis-dev',
    'github_repo': 'ultra-vehicle-system',
    'github_version': 'main',
    'conf_py_path': '/docs/source/',
}
numfig = False

# Wrap the class event tables within the page instead of forcing horizontal scrolling.
html_static_path = ['_static']
html_css_files = ['events-reference.css']
