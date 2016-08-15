Fiona
=====

`Fiona <http://toblerity.org/fiona/>`__ is build on top of OGR and it
introduces the object-oriented approach to the work with vector data.
The data are re-mapped in to GeoJSON structure. The interaction is more
straight-forward compared to OGR.

Fiona is not suited to be the best for all tasks - simplicity is bought
back by the fact, all data need to be loaded in memory. Also speed can
be lower, when dealing with larger amounts of data. Where OGR uses
pointers, Fiona has to deal with whole python objects. Generally: if you
need to filter vector features, OGR should be faster, if you need to
work with features sequentially, Fiona should be better.

.. note:: Fiona is great for binary data formats. For JSON, use the
        ``json`` python package. For data stored in database, use standard
        Python database interface.

First we need to create so called collection of features:

.. code:: python

    >>> import fiona
    >>> pa = fiona.open('data/protected_areas-etrs.shp', 'r') # collection - data are stored in ../../data directory 
    >>> pa
    <open Collection 'data/protected_areas-etrs.shp:protected_areas-etrs', mode 'r' at 0x7fdfdfd4b2d0>

We can now mine some metadata about this feature collection, see
`documentation <http://toblerity.org/fiona/manual.html>`__

.. code:: python

    >>> # driver
    >>> pa.driver
    u'ESRI Shapefile'

    >>> # coordinate reference system
    >>> pa.crs
    {u'lon_0': 10, u'ellps': u'GRS80', u'y_0': 3210000, u'no_defs': True, u'proj': u'laea', u'x_0': 4321000, u'units': u'm', u'lat_0': 52}

    >>> # file name
    >>> pa.path
    'data/protected_areas-etrs.shp'

    >>> # layer name
    >>> pa.name
    u'protected_areas-etrs'

    # bounding box coordinates
    >>> pa.bounds
    (4493979.359512844, 2839119.848736721, 4952710.629522002, 3106267.3238070104)

    >>> # everything in one step
    >>> print(pa.meta)
    {'crs': {u'lon_0': 10, u'ellps': u'GRS80', u'y_0': 3210000, u'no_defs': True, u'proj': u'laea', u'x_0': 4321000, u'units': u'm', u'lat_0': 52}, 'driver': u'ESRI Shapefile', 'schema': {'geometry': 'Polygon', 'properties': OrderedDict([(u'gml_id', 'str:80'), (u'OBJECTID', 'int:10'), (u'KOD', 'int:10'), (u'KAT', 'str:4'), (u'NAZEV', 'str:27'), (u'ZONA', 'str:3'), (u'ROZL', 'float:24.15'), (u'OP_TYP', 'str:3'), (u'IUCN', 'str:2'), (u'ZMENA_G', 'int:10'), (u'ZMENA_T', 'int:10'), (u'PREKRYV', 'int:10'), (u'SHAPE.AREA', 'float:24.15'), (u'SHAPE.LEN', 'float:24.15')])}}

    >>> # try better format
    >>> import json
    >>> print json.dumps(pa.meta, sort_keys=True, indent=4, separators=(',', ': '))
    {
    "crs": {
        "ellps": "GRS80",
        "lat_0": 52,
        "lon_0": 10,


Features in collections
-----------------------

Features within opened collection can be iterated

.. code:: python

    >>> print len(pa)
    5626

Coordinate reference systems
----------------------------

Fiona comes with primitive tools for dealing with coordinate reference
systems, with GDAL library in the background

.. code:: python

    >>> natural = fiona.open('data/natural.shp', 'r')
    >>> from fiona.crs import to_string
    >>> print(to_string(natural.crs))
    +init=epsg:4326

    >>> to_string(pa.crs)
    '+ellps=GRS80 +lat_0=52 +lon_0=10 +no_defs +proj=laea +units=m +x_0=4321000 +y_0=3210000'

Simillary, new CRS definition can be created

.. code:: python

    >>> from fiona.crs import from_epsg
    >>> from_epsg(3857)
    {'init': 'epsg:3857', 'no_defs': True}

Walking through features
------------------------

we can either iterate through available features

.. code:: python

    >>> for feature in pa[0:10]:
    ...     print feature['geometry']['type']
    Polygon
    Polygon
    Polygon
    Polygon
    ...

or particular feature can be choosed

.. code:: python

    >>> print pa[54]['properties']['NAZEV']
    Český ráj

Feature geometry and shapely library
------------------------------------

`Shapely <http://toblerity.org/shapely>`__ converts feature geometry
into GeoJSON structure. It also contains tools for geometry
manipulations

.. code:: python

    >>> from shapely.geometry import shape
    >>> cr = pa[54] # cr - Cesky raj
    >>> poly = shape(cr['geometry'])
    >>> print(poly.bounds)
    (4685576.577618335, 3067490.2318713292, 4687748.187993193, 3069132.552762671)

Now we can either generalize given geometry or create buffer

.. code:: python

    >>> simple = poly.simplify(10)
    >>> simple.intersects(poly)
    True

    >>> buff = poly.buffer(10)
    >>> buff.contains(poly)
    True

some feature attributes can be fixed as well, at the end, we write new
created feature down

.. code:: python

    >>> from shapely.geometry import mapping
    >>> import copy
    >>> feature = copy.deepcopy(cr)
    >>> feature['id'] = -1
    >>> feature['geometry'] = mapping(buff)
    >>> feature['properties']['NAZEV'] = u'Mordor'
    >>> chko = fiona.open('data/protected_areas-etrs.shp', 'a')
    >>> print("Features before: %d " % len(chko))
    >>> print("Features before: %d " % len(chko))
    Features before: 5626

    >>> chko.write(feature)
    >>> print("Features after: %d " % len(chko))
    Features after: 5627

    >>> chko.close()
