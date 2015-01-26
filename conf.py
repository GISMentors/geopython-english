# -*- coding: utf-8 -*-

import sys
import os

# -- General configuration ------------------------------------------------

# General information about the project.
project = u'Školení GeoPython'
copyright = u'2014, Jáchym Čepický a Martin Landa (GISMentors.eu)'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '%s alpha' % version

# -- Options for HTML output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Skoleni-GeoPython'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', '%s.tex' % htmlhelp_basename, project,
     copyright, 'manual'),
    ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', htmlhelp_basename, project,
     [copyright], 1)
    ]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', htmlhelp_basename, project,
     copyright, htmlhelp_basename, project,
     'Miscellaneous'),
    ]

sys.path.append(os.path.join('..', 'sphinx-template'))
from conf_base import *

extensions.append('sphinxcontrib.aafig')
