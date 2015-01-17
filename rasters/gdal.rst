GDAL
====
Knihovna `GDAL <http://gdal.org>`_ je základním kamenem většiny dalších projektů
(nejen) open source GIS. Tato knihovna (jejíž součástí je i zmíněná knihovna
:ref:`ogr`), provází konverzi mezi více než 130 rastrovými formáty.

Koncept pro rastrová data je trochu podobný jako pro vektorová:

* `Driver` - ovladač pro čtení a zápis různých formátů
  * `DataSource` - zdroj dat, ze kterého a do kterého se čte a zapisuje
    * `Band` - Rastrové pásmo. U kěterých zdrojů je jenom jedno pásmo, ale může
      jich mít teoreticky neomezeně (z hyperspektrálních snímkovacích zařízení).

Mezi další důležité charakteristicky rastrů patři rozlišení a velikost pixelu a
jeho hraniční souřadnice.

Vytvoření nového souboru z pole hodnot
--------------------------------------

V následujícím příkladě vytvoříme nový rastrový soubor a vyplníme ho polem
hodnot. Výsledek uložíme do souboru ve formátu GeoTIFF.

Nejprve nastavíme několik výchozích hodnot, jako je velikost hrany pixelu,
číselná hodnota pro `NODATA` data, jméno výsledného souboru a extent (hraniční
souřadnice) rastrových dat.

.. code-block:: python

    >>> from osgeo import gdal, ogr, osr

    >>> # Define pixel_size and NoData value of new raster
    >>> pixel_size = 20
    >>> NoData_value = -9999

    >>> # Filename of the raster Tiff that will be created
    >>> raster_fn = 'test.tif'

    >>> # Raster file extent
    >>> x_min, x_max, y_min, y_max = (0, 100, 0, 100)

V dalším kromu spočítáme rozlišení pixelu - na základně jeho velikosti a
rozsahu rastrových dat.

.. code-block:: python

    >>> # Create the destination data source
    >>> x_res = int((x_max - x_min) / pixel_size)
    >>> y_res = int((y_max - y_min) / pixel_size)

Nyní můžeme vytvořit *datový zdroj* pro rastrová data. Nejprve vytvoříme
instanci objektu `Driver` pro požadovaný formát a následně vytvoříme prázdný
rastrový soubor. Zde musíme specifikovat

* jméno výsledného souboru
* rozlišení ve směru os `x` a `y`
* počet pásem (kanálů)
* typ číselné hodnoty

Nakonec nastavíme transformační parametry, které jsou ve
stejném formátu v jakém bývají uloženy v tzv. *world file* souboru:

* souřadnice levého-horního rohu `x`
* rozlišení ve směru osy `x`
* naklonění osy `x`
* souřadnice levého-horního roku `y`
* rozlišení ve směru osy `y`
* naklonění osy `y`

.. code-block:: python

    >>> target_driver = gdal.GetDriverByName('GTiff')
    >>> target_ds = target_driver.Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
    >>> target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

V dalším kroku zapíšeme data do vybraného pásma (číslování pásem začíná hodnotou
1 a ne více obvyklou 0. Do připraveného rastrového kanálu můžeme nyní zapsat
hodnoty jako pole polí hodnot.

.. code-block:: python

    >>> band = target_ds.GetRasterBand(1)
    >>>
    >>> import numpy as np
    >>> band.WriteArray(np.array([[0, 0, 0, 0, 0],
    ...                  [0, 10, 15, 10, 0],
    ...                  [0, 15, 25, 15, 0],
    ...                  [0, 10, 15, 10, 0],
    ...                  [0, 0, 0, 0, 0]]))
    ...

Celý rastrový soubor ještě opatříme souř. systémem. Projekce se nastavuje
pomocí zápisu ve formátu *Well known text*, proto nejprve vytvoříme objekt
projekce na základě kódu EPSG a vyexportujeme jako WKT:

.. code-block:: python

    >>>
    >>> outRasterSRS = osr.SpatialReference()
    >>> outRasterSRS.ImportFromEPSG(3857)
    >>> target_ds.SetProjection(outRasterSRS.ExportToWkt()) # !!! jiné než u vektorů

A nakonec uklidíme (pro jistotu) a uzavřeme zápis:

.. code-block:: python

    >>> band.FlushCache()

Rasterizace vektorového souboru
-------------------------------
Další ne zcela obvyklou operací může být převod z vektorového datového souboru
na rastrový. Začátek je stejný jako v předchozím případě

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
    >>> raster_fn = 'chko.tif'
    >>>

Otevřeme vektorový soubor

.. code-block:: python

    >>> # Filename of input OGR file
    >>> vector_fn = 'chko.shp'
    >>>
    >>> source_ds = ogr.Open(vector_fn)
    >>> source_layer = source_ds.GetLayer()

A nyní můžeme zjistit potřebné hraniční souřadnice a vytvořit cílový rastrový
soubor

.. code-block:: python

    >>>
    >>> # Open the data source and read in the extent
    >>> x_min, x_max, y_min, y_max = source_layer.GetExtent()
    >>>
    >>> # Create the destination data source
    >>> x_res = int((x_max - x_min) / pixel_size)
    >>> y_res = int((y_max - y_min) / pixel_size)
    >>> tiff_driver = gdal.GetDriverByName('GTiff')
    >>> target_ds = tiff_driver.Create(raster_fn, x_res, y_res, 3, gdal.GDT_Byte)
    >>> target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

Zkopírujeme také informaci o souř. systému

.. code-block:: python

    >>>
    >>> outRasterSRS = osr.SpatialReference()
    >>> outRasterSRS.ImportFromEPSG(5514)
    >>> target_ds.SetProjection(outRasterSRS.ExportToWkt()) # !!! jiné než u vektorů

Zlatým hřebíkem tohoto příkladu je funkce `RasterizeLayer` s následujícími
parametry:

* cílový datový zdroj
* rastrová pásma
* zdrojová vektorová vrstva
* hodnoty pro jednotlivá pásma
* dodatečné parametry

.. code-block:: python

    >>>
    >>> gdal.RasterizeLayer(target_ds,
        [1, 2, 3],
        source_layer,
        burn_values=[255,125,0],
        options=['ALL_TOUCHED=TRUE']) # žádné mezery okolo znakuk '='
    >>> target_ds.FlushCache()

.. gdal.RasterizeLayer(dataset, [1], layer, options = ["ATTRIBUTE=KOD"])

Na konci je vše hotovo, do námi vytvořeného rastrového souboru byla zapsána 
