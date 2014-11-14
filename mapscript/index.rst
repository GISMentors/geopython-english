MapScript
=========

Pythoní rozhraní k MapServeru

* *Map*

  * *Layer*

    * *Class*
        * *Style*

.. code-block:: python

    >>> import mapscript, ogr

    >>> chko = ogr.Open('chko.shp')
    >>> l = chko.GetLayer()
    >>> extent = l.GetExtent()

    >>> mapobj = mapscript.mapObj()
    >>> mapobj.setSize(500, 500)
    >>> mapobj.setExtent(extent[0], extent[2], extent[1], extent[3])
    >>> mapobj.setProjection("+init=epsg:5514")

    >>> layer = mapscript.layerObj(mapobj)
    >>> layer.type = mapscript.MS_LAYER_POLYGON
    >>> layer.data = 'chko.shp'
    >>> layer.status = mapscript.MS_ON
    >>> layer.setProjection("+init=epsg:5514")

    >>> classobj = mapscript.classObj(layer)
    >>> styleobj = mapscript.styleObj(classobj)
    >>> styleobj.color = mapscript.colorObj(125, 0, 0)

    >>> mapobj.outputformat.imagemode = mapscript.MS_IMAGEMODE_RGBA
    >>> mapobj.outputformat.transparent= 1

    >>> img = mapobj.draw()
    >>> img.save('out.png')

    >>> mapobj.save("out.map")
