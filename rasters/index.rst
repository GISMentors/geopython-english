Práce s rastrovými daty
=======================

Rastrová data mohou být v porovnání s vektorovými daty zhlediska
objemu dat větší. Tomu je třeba přizpůsobit práci s nimi. Rastrová
data jsou většinou uspořádané do matice hodnot v číselné podobě.

Pro práci s rastrovými geodaty se "tradičně" používá knihovna `GDAL
<http://gdal.org>`_. Knihovna GDAL je nízkoúrovňová, přistupuje k
datům pokud možno efektivním způsobem. Alternativou ke knihovně GDAL
je `rasterio <https://github.com/mapbox/rasterio>`_, která je nad
touto knihovnou postavena. Jedná se o jakousi analogii ke knihovnám
:ref:`OGR <ogr>` a :ref:`Fiona <fiona>` pro práce s vektorovými daty.

.. toctree::
   :maxdepth: 2

   rasterio
   gdal
..   pil
