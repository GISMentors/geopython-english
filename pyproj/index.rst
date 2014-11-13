PyProj
======

Malá odbočka k pyproj

.. code-block:: python

    >>> import pyproj
    >>> sjtsk = pyproj.Proj("+init=epsg:5514")
    >>> wgs = pyproj.Proj("+init=epsg:4326")
    >>> sjtsk(-868208.53, -1095793.57, inverse=True)
    (12.807805435216094, 49.45302198345776)
