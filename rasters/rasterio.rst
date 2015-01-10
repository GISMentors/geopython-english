Rasterio
========

Knihovna `Rasterio <https://github.com/mapbox/rasterio>`_ je opět zejména `Seana
Gilliese <http://sgillies.net/>`_, tentokrát ovšem pracoval pro firmu `MapBox
<http://mapbox.com>`_. Rasterio pracuje s prostorovými rastrovými datovými
sadami. Na pozadí Rasterio pracuje spolehlivá knihovna `GDAL
<http://gdal.org>`_. 

Rasterio pracuje s objekty knihovny `NumPy <http://www.numpy.org/>`_ (podobně
jako dříve zmíněná Fiona pracuje s objekty JSON). Autor tvrdí, že Rasterio se
vyslovuje *[raw-STEER-ee-oh]* a měla by práci s rastrovými daty udělat více
zábavnou a produktivnější.

V následujícím příkladu otevřenem rastrový soubor a podíváme se na některá
metadata:

.. code-block:: python

    >>> import rasterio
    >>> src = rasterio.open('data/RGB.byte.tif')
    >>> src.bounds
    BoundingBox(left=101985.0, bottom=2611485.0, right=339315.0, top=2826915.0)
    >>> src.crs
    {'init': u'epsg:32618'}
    >>> # tagy formátu GeoTIFF
    >>> src.tags()
    {u'AREA_OR_POINT': u'Area'}
    >>> src.width, src.height
    (791, 718)
    >>> src.res
    (300.0379266750948, 300.041782729805)
    

    >>> (r, g, b) = src.read()


##########################################################################
##########################################################################
##########################################################################
Vytvoření rastru z pole hodnot

.. code-block:: python

    >>> from osgeo import gdal, ogr, osr

    >>> # Define pixel_size and NoData value of new raster
    >>> pixel_size = 20
    >>> NoData_value = -9999

    >>> # Filename of input OGR file

    >>> # Filename of the raster Tiff that will be created
    >>> raster_fn = 'test.tif'

    >>> # Open the data source and read in the extent
    >>> x_min, x_max, y_min, y_max = (0, 100, 0, 100)

    >>> # Create the destination data source
    >>> x_res = int((x_max - x_min) / pixel_size)
    >>> y_res = int((y_max - y_min) / pixel_size)
    >>> target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
    >>> target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
    >>> band = target_ds.GetRasterBand(1)
    >>>
    >>> import numpy as np
    >>> band.WriteArray(np.array([[0, 0, 0, 0, 0],
    ...                  [0, 10, 15, 10, 0],
    ...                  [0, 15, 25, 15, 0],
    ...                  [0, 10, 15, 10, 0],
    ...                  [0, 0, 0, 0, 0]]))
    >>>
    >>> outRasterSRS = osr.SpatialReference()
    >>> outRasterSRS.ImportFromEPSG(3857)
    >>> target_ds.SetProjection(outRasterSRS.ExportToWkt()) # !!! jiné než u vektorů
    >>> band.FlushCache()

 Rasterizace vektoru

.. code-block:: python

    >>> # -*- coding: utf-8 -*-
    >>> from osgeo import gdal, ogr, osr
    >>> 
    >>> # Define pixel_size and NoData value of new raster
    >>> pixel_size = 50
    >>> NoData_value = -9999
    >>> 
    >>> # Filename of input OGR file
    >>> 
    >>> # Filename of the raster Tiff that will be created
    >>> raster_fn = 'test3.tif'
    >>> 
    >>> # Filename of input OGR file
    >>> vector_fn = 'chko.shp'
    >>> 
    >>> source_ds = ogr.Open(vector_fn)
    >>> source_layer = source_ds.GetLayer()
    >>> 
    >>> # Open the data source and read in the extent
    >>> x_min, x_max, y_min, y_max = source_layer.GetExtent()
    >>> 
    >>> # Create the destination data source
    >>> x_res = int((x_max - x_min) / pixel_size)
    >>> y_res = int((y_max - y_min) / pixel_size)
    >>> target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 3, gdal.GDT_Byte)
    >>> target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
    >>> 
    >>> outRasterSRS = osr.SpatialReference()
    >>> outRasterSRS.ImportFromEPSG(5514)
    >>> target_ds.SetProjection(outRasterSRS.ExportToWkt()) # !!! jiné než u vektorů
    >>> 
    >>> gdal.RasterizeLayer(target_ds, [1, 2, 3], source_layer, burn_values=[255,125,0], options=['ALL_TOUCHED=TRUE'])
    >>> 
    >>> print target_ds.GetRasterBand(1).Checksum()
