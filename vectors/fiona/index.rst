Vektory pomocí knihovny Fiona
=============================
Knihovna `Fiona <http://toblerity.org/fiona/>`_, představuje modernější způsob
práce s vektorovými daty. Finoa je nadstavba nad knihovnou OGR. Načtená data ze
souborů přemapovává do GeoJSONí struktury a stejné struktury zapisuje zpět do
souborů. Uživatel se nemusí zabývat kurzory, vrstvami, geometrickými operacemi.

Fiona není nástroj vhodný na **všechny** operace - jednoduchost práce je
vykoupena poněkud pomalejším během. Tam kde OGR používá pointery, Fiona
zkopíruje vektorová data do objektů jazyka Python, což samozřejmě vede k
intenzivnějšímu využívání paměti. Pokud potřebujete filtrovat objekty, OGR je
asi vhodnější. Pokud potřebujete zpracovat postupně všechny objekty, Fiona by
měla být rychlejší.

Fiona je vhodná na binární souborové formáty dat. Kde pracujete s daty
(Geo)JSON, používejte **json** balíček. Kde pracujete s daty v databázích,
používejte jejich knihovny. 

.. todo:: Platí pro gdal 1.11, blbnou vrstvy

.. code-block:: python

    >>> import fiona
    >>> c = fiona.open('chko.shp', 'r') # collection
    >>> c
    <open Collection 'chko.shp:chko', mode 'r' at 0x7feea9595410>
    >>> c.driver
    u'ESRI Shapefile'
    >>> c.crs
    {u'lon_0': 24.83333333333333, u'k': 0.9999, u'ellps': u'bessel', u'y_0': 0, u'no_defs': True, u'proj': u'krovak', u'x_0': 0, u'units': u'm', u'alpha': 30.28813972222222, u'lat_0': 49.5}
    >>> dir(c)
    ['__class__', '__contains__', '__del__', .... ]
    >>>
    >>> len(c)
    5626

Souřadnicové systémy
--------------------

.. code-block:: python

    >>> import fiona
    >>> c = fiona.open('20141031_ST_UKSH.gpkg', 'r')
    >>>
    >>> from fiona.crs import to_string
    >>> print(to_string(c.crs))
    +init=epsg:5514
    >>>
    >>> from fiona.crs import from_epsg
    >>> from_epsg(3857)
    {'init': 'epsg:3857', 'no_defs': True}


Procházní dat
-------------

.. code-block:: python

    >>> for feature in c:
    ...     print feature['geometry']['type']
    >>> print c[54]['properties']['NAZEV']
    Český ráj


Práce s daty
------------

.. code-block:: python

    >>> from shapely.geometry import shape
    >>> cr = c[54]
    >>> poly = shape(cr['geometry'])
    >>> poly.bounds
    (-683329.1875, -993228.75, -681265.625, -991528.0)
    >>>
    >>> simple = poly.simplify(10)
    >>> simple.intersects(poly)
    True
    >>> buff = poly.buffer(10)
    >>> buff.contains(poly)
    True
    >>> c.close()

    >>> from shapely.geometry import mapping
    >>> import copy
    >>> feature = copy.deepcopy(cr)
    >>> feature['id'] = -1
    >>> feature['geometry'] = mapping(buff)
    >>> feature['properties']['NAZEV'] = u'Mordor'
    >>> c = fiona.open('chko-zmrsene.shp', 'a')
    >>> c.write(feature)
    >>> c.close()



Nažrání dat z webové služby
---------------------------

viz kapitola o :ref:`OWSLib` a :ref:`OWSLibWFS`

.. code-block:: python

    [...]
    >>> f = aopk.getfeatures(['UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území'])

Špinavý trik - nažrání feature pomocí `gdal.FileFromMemBuffer` objektu

.. code-block:: python

    >>> from osgeo import gdal
    >>> gdal.FileFromMemBuffer('/vsimem/temp', f.read())
    >>>
    >>> # malý trik
    >>> from fiona.collection import supported_drivers
    >>> supported_drivers['GML'] = 'r'
    >>>
    >>> # a čteme
    >>> c = fiona.open('/vsimem/temp', 'r')
    >>>
    >>> # počet prvků
    >>> len(c)
    3571

.. todo:: OGR
