GDAL
====


.. code-block:: python

    >>> from osgeo import gdal, ogr

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


