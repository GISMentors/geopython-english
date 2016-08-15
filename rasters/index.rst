Working with raster data
========================

Raster data can be, when compared to vectors, much bigger and therefore workflow
has to be adjusted.  Rasterdata are usually organised in to matrix, with cells
containgin numbers and refered to as 'pixels'.  Usually, GDAL library is used
for interacting with raster data. GDAL is low-level library and accesses to the
data with not so efficient, yet scalable and stable way. Alternative to GDAL is
RasterIO library (which is build on top of GDAL too). We can see there analogy
to OGR and Fiona librarys we already metioned.

.. toctree::
   :maxdepth: 2

   rasterio
   gdal

..   pil


