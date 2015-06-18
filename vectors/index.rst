Práce s vektorovými daty
========================

Pro práci s vektorovými daty se v jazyce Python tradičně používá
knihovna `GDAL/OGR <http://gdal.org>`_. V poslední době však začíná
být populární i knihovna `Shapely <http://toblerity.org/shapely/>`_ a
především knihovna `Fiona <http://toblerity.org/fiona/>`_.

V rámci školení se zaměříme se na knihovny Fiona a OGR. *Fiona* je
projekt programátora `Seana Gilliese <http://sgillies.net/>`_, který
vytvořil vlastní aplikační rozhraní ke knihovně OGR, které více
odpovídá standardům a postupům objektového jazyka Python. *OGR* je z
tohoto pohledu knihovna, pomocí které lze provádět v porovnání s
Fionou nízkoúrovňovné operace.

V průběhu kurzu načteme a zpracujeme data, se kterými se lze v České republice
běžně setkat, zejména data z~registru `RÚIAN <http://www.ruian.cz>`_ (viz `návody pro knihovnu GDAL <http://freegis.fsv.cvut.cz/gwiki/VFK_/_GDAL>`_).

.. toctree::
   :maxdepth: 2

   fiona/index
   ogr/index
