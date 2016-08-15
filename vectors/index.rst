Vector data introduction
========================

Traditionally, we use GDAL/OGR library for interacting with vector data.
Lately, Shapely library is becoming the popular too, as well as Fiona
does.

This workshop will focus on Fiona and OGR.
`Fiona <http://toblerity.org/fiona/>`__ is maintained by Sean Gillies. It
is adding new layer on top of OGR, which is more compliant to what is
common in Python. Compared to Fiona, with OGR more low-level data access
can be achieved.

.. toctree::

    fiona
    ogr
