Vektory a OGR
=============

OGR  (součást GDAL) je tradiční knihovna pro práci s vektorovými daty.

OGR pracuje s konceptem vrstev v datových zdrojích:

* *Data Source* (soubor, databáze, ...)

    * *[Layer]* (obsah souboru, tabulka, ...)

      * *[Feature]* (vzhledy jevu)
        
        * *[Field, Geometry]*

.. code-block:: python

    >>> from osgeo import ogr
    >>> ds = ogr.Open("chko.shp")
    >>> ds
    <osgeo.ogr.DataSource; proxy of <Swig Object of type 'OGRDataSourceShadow *' at 0x7f98d8152a50> >
    >>> ds.GetLayerCount()
    1
    >>>

Práce s vrstvou

.. code-block:: python

    >>> l = ds.GetLayer(0)
    >>> l
    <osgeo.ogr.Layer; proxy of <Swig Object of type 'OGRLayerShadow *' at 0x7f98d80fa870> >
    >>> l.GetFeatureCount()
    5626

Schema

.. code-block:: python

    >>> l.GetGeomType()
    3
    >>> l.GetGeomType() == osgeo.ogr.wkbPolygon
    True
    >>> l.schema
    [<osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7f98d80fa9f0> >, <osgeo.ogr.FieldDefn; proxy of <Swig Object of type 'OGRFieldDefnShadow *' at 0x7f98d80fa8...
    >>> 
    >>> l.schema[4].name
    'NAZEV'

Vzhledy jevu

.. code-block:: python

    >>> features_nr = l.GetFeatureCount()
    >>> for i in range(features_nr):
    ...     f = l.GetNextFeature()
    ...     print f.GetField('NAZEV')
    Český ráj
    ...
    >>>

Geometrie

.. code-block:: python

    >>> f = l.GetFeature(54)
    >>> f.GetField('NAZEV')
    >>> print f.GetField('NAZEV')
    Český ráj
    >>> geom = f.GetGeomRef()
    >>> geom.GetEnvelope()
    (-683329.1875, -681265.625, -993228.75, -991528.0)
    >>> c = geom.GetCentroid()
    >>> c.GetPoint()
    (-682407.4126500859, -992433.3498782327, 0.0)
    >>> buff = c.Buffer(100)
    >>> geom.Intersects(buff)
    True

A od začátku (co ve Fioně nebylo a jde to tam 3× jednoduššeji) ...

.. code-block:: python

    >>> from osgeo import osr
    >>> drv = ogr.GetDriverByName('GML')
    >>> ds = drv.CreateDataSource('/tmp/out.gml')
    >>> srs = osr.SpatialReference()
    >>> srs.ImportFromEPSG(5514)
    >>> srs.ExportToProj4()
    '+proj=krovak +lat_0=49.5 +lon_0=24.83333333333333 +alpha=30.28813972222222 +k=0.9999 +x_0=0 +y_0=0 +ellps=bessel +towgs84=...
    >>> layer = ds.CreateLayer('out.gml', srs, ogr.wkbLineString)
    >>> 
    >>> field_name = ogr.FieldDefn('Name', ogr.OFTString)
    >>> field_name.SetWidth(24)
    >>> field_number = ogr.FieldDefn('Number', ogr.OFTInteger)
    >>> layer.CreateField(field_name)
    >>> layer.CreateField(field_number)
    >>> 
    >>> line = ogr.CreateGeometryFromWkt('LINESTRING(%f %f, %f %f)' % (0, 0, 1, 1))
    >>>
    >>> feature = ogr.Feature(layer.GetLayerDefn())
    >>> feature.SetGeometry(line)
    >>> feature.SetField("Name", 'Jméno')
    >>> feature.SetField("Number", 42)
    >>>
    >>> layer.CreateFeature(feature)
    >>>
    >>> # Úklid
    >>> feature.Destroy()
    >>> ds.Destroy()


.. Malá odbočka k pyproj
.. 
.. .. code-block:: python
.. 
..     >>> import pyproj
..     >>> sjtsk = pyproj.Proj("+init=epsg:5514")
..     >>> wgs = pyproj.Proj("+init=epsg:4326")
.. 





