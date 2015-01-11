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

.. figure:: rgb.png
    :alt: RGB obrázek

    Výsledný soubor s NDVI indexem

Načtení barevných kanálů:

.. code-block:: python

    >>> data = src.read()
    >>> len(data)
    3

Vidíme, že v rastru jsou obsaženy tři barevné kanály. Vytvoříme nyní nový
soubor, obsahující pokus o index NDVI.

.. note:: `Normalizovaný vegetační index
    <http://en.wikipedia.org/wiki/Normalized_Difference_Vegetation_Index>`_ je poměr
    mezi viditelnou červenou barvou a blízkou infra červenou barvou ve snímku
    dálkového průzkumu Země.

    .. math::
        
         NDVI = (NIR - VIS) / (NIR  + VIS)

    Protože ale v našem příkladovém souboru není blízký infrared kanál
    viditelný, použijeme poměr mezi zeleným a červeným kanálem.

Neprve vytvoříme nové pole pro výsledné hodnoty, následně do tohoto pole uložíme
výsledek výpočtu pro každý pixel. Pracujeme vlastně v prostředí NumPy, které
práci s poli významně usnadňuje.

.. code-block:: python

    >>> (nir, vis) = (data[0], data[1])
    >>> ndvi = (nir - vis) / (nir + vis)

Výsledek uložíme do nově vytvořeného souboru. Data budou zkomprimována pomocí
LWZ komprese a uložena v číselném formátu `uint8`. Počet kanálů bude 1.

.. code-block:: python

    >>> kwargs = src.meta
    >>> kwargs.update(
        dtype=rasterio.uint8,
        count=1,
        compress='lzw')
    >>> with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
            dst.write_band(1, ndvi.astype(rasterio.uint8))

.. figure:: ndvi.png
    :alt: Index NDVI

    Výsledný soubor s NDVI indexem
