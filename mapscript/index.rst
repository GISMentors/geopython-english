Servers and Python
==================
Just very short list:

* MapScript
* GSConfig
* GeoDjango
* PyCSW
* PyWPS
* istSOS
* ...

MapScript
=========



Following classes have to be defined, if you need to work with MapServer MapFile
configuration from Python:

* **Map**
* **Layer**
* **Class**
* **Style**

.. aafig::
    :aspect: 60
    :scale: 100

                                +-------+
                                | Map   |
                                +---+---+
                                   / \
                                  /   \
                                 /     \
                                /       \
                               /         \
                         +----+--+    +---+---+    +-------+
                         | Layer |    | Layer |    | ...   |
                         +---+---+    +-------+    +-------+
                            / \
                           /   \
                          /     \
                         /       \
                        /         \
                  +----+--+    +---+---+    +-------+
                  | Class |    | Class |    | ...   |
                  +---+---+    +-------+    +-------+
                     / \
                    /   \
                   /     \
                  /       \
                 /         \
            +---+---+   +---+---+   +-------+
            | Style |   | Style |   | ...   |
            +-------+   +-------+   +-------+

More information: http://mapserver.org/mapscript/python.html
            
Example
-------
This example will create new `Map` object with `Layer` and `Class` objects

.. code-block:: python

    >>> import mapscript, ogr

    >>> # first get some metadata
    >>> pa = ogr.Open('data/protected_areas.shp')
    >>> l = pa.GetLayer()
    >>> extent = l.GetExtent()

    >>> mapobj = mapscript.mapObj()
    >>> mapobj.setSize(500, 500)
    >>> mapobj.setExtent(extent[0], extent[2], extent[1], extent[3])
    >>> mapobj.setProjection("+init=epsg:3035")

    >>> layer = mapscript.layerObj(mapobj)
    >>> layer.type = mapscript.MS_LAYER_POLYGON
    >>> layer.data = 'data/protected_areas.shp'
    >>> layer.status = mapscript.MS_ON
    >>> layer.setProjection("+init=epsg:3035")

    >>> classobj = mapscript.classObj(layer)
    >>> styleobj = mapscript.styleObj(classobj)
    >>> styleobj.color = mapscript.colorObj(125, 0, 0)

    >>> mapobj.outputformat.imagemode = mapscript.MS_IMAGEMODE_RGBA
    >>> mapobj.outputformat.transparent= 1

    >>> img = mapobj.draw()
    >>> img.save('data/out.png')

    >>> mapobj.save('data/out.map')
