pyramid-sphinx-themes
=====================

Pyramid Sphinx themes for related projects


Requirements
------------

You will need the following for hacking on this project:

- `Python <https://www.python.org/downloads/>`_
- `Virtualenv <http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation>`_
- `NodeJS <http://nodejs.org/download/>`_
- `bower <http://bower.io/>`_
- `gulp <http://gulpjs.com/>`_

Using npm, install bower and gulp system-wide, if you have not done so
already.
::

  $ npm install -g bower
  $ npm install -g gulp

Installing
----------

Assuming you have all the recommended tools listed above installed:


1. Clone the project
++++++++++++++++++++
::

  $ git clone git@github.com:Pylons/pyramid-sphinx-themes.git
  $ cd pyramid-sphinx-themes


2. Create and initialize a virtualenv
+++++++++++++++++++++++++++++++++++++
::

  # for Python 2
  $ virtualenv .
  # for Python 3
  $ pyvenv --upgrade .


3. Install requirements
+++++++++++++++++++++++
::

  $ bin/pip install -r requirements.txt

You also need to install the project in editable mode:
::

  $ bin/pip install -e .


4. Install frontend tools
+++++++++++++++++++++++++
::

   $ npm install
   $ bower install


Working with assets
-------------------

If you're working on the frontend stack you should compile your LESS
files to CSS, merge CSS and JavaScript, copy files and do other tasks.
The default Gulp task takes care of LESS compilation:
::

  $ gulp

You can use the watcher task while you're working so each time you
modify a file the less and js files are compiled to dist:
::

  $ gulp watch

If something bad happens and you need to reinitialize the assets, run
this command:
::

  $ gulp init


Building your docs
------------------

Make edits in your project `docs/conf.py` as follows:

1. Add the `pyramid_sphinx_themes` Sphinx extension module name
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
::

    # Add any Sphinx extension module names here, as strings. They can be extensions
    # coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
    extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'pyramid_sphinx_themes'
        ]

2. Modify the section "Options for HTML output"
+++++++++++++++++++++++++++++++++++++++++++++++
::

    # -- Options for HTML output ---------------------------------------------------

    from pyramid_sphinx_themes import get_html_themes_path

    # The theme to use for HTML and HTML Help pages.  See the documentation for
    # a list of builtin themes.
    html_theme = 'ground'

    # Theme options are theme-specific and customize the look and feel of a theme
    # further.  For a list of options available for each theme, see the
    # documentation.
    #html_theme_options = {}

    # Add any paths that contain custom themes here, relative to this directory.
    html_theme_path = get_html_themes_path()

3. Set (or wherever it gets set in the package)
+++++++++++++++++++++++++++++++++++++++++++++++
::

    html_use_smartypants = False

Save `docs/conf.py`.

4. Run `sphinx-build`
+++++++++++++++++++++

While your current directory is `docs/`, run the command:
::

    make clean html SPHINXBUILD=../bin/sphinx-build


References and Guides
---------------------
- `Getting started with gulp <http://markgoodyear.com/2014/01/getting-started-with-gulp/>`_
- `Building with gulp <http://www.smashingmagazine.com/2014/06/11/building-with-gulp/>`_
