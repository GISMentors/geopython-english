Vector data introduction
========================

Traditionally, we use `GDAL library <http://gdal.org>`_ for
interacting with vector data.  Lately, `Shapely library
<http://toblerity.org/shapely/>`_ is becoming popular too, as well as
Fiona does.

This part of the workshop will focus on **Fiona**, **Shapely** and
**GDAL** (better to say **OGR** library which is part of GDAL and
covers vectors).  `Fiona <http://toblerity.org/fiona/>`__ is
maintained by Sean Gillies. It is adding new layer on top of OGR,
which is more compliant to what is common in Python. Compared to
Fiona, with OGR more low-level data access can be achieved.

.. toctree::

    fiona
    ogr
