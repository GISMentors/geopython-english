PyProj
======

Na záveř malá odbočka k souřadnicovým systémům a Python rozhraní pro
knihovnu `Proj4 <http://trac.osgeo.org/proj>`_ - `PyProj
<https://github.com/jswhit/pyproj>`_.

V následijící ukázce si ukážeme převod ze systému S-JTSK
(:epsg:`5514`) do WGS-84 (:epsg:`4326`):

.. code-block:: python

    >>> import pyproj
    >>> sjtsk = pyproj.Proj("+init=epsg:5514")
    >>> wgs = pyproj.Proj("+init=epsg:4326")
    >>> sjtsk(-868208.53, -1095793.57, inverse=True)
    (12.807805435216094, 49.45302198345776)
