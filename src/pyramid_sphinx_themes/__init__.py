"""Pyramid Sphinx Themes"""

import os

from sphinx.builders.html import StandaloneHTMLBuilder


def patch_sphinx():
    # Override files... Why we could not!!
    script_files = [
        '_static/dist/js/jquery.min.js',
        '_static/dist/js/underscore-min.js',
        '_static/dist/js/bootstrap.min.js',
        '_static/dist/js/html5shiv.js',
        '_static/dist/js/respond.min.js',
        '_static/dist/js/doctools.js',
        '_static/dist/js/theme.js'
        ]
    StandaloneHTMLBuilder.script_files = script_files


def get_html_themes_path():
    """Return list of sphinx themes."""
    here = os.path.abspath(os.path.dirname(__file__))
    return [here]
