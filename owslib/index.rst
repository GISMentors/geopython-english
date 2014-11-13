.. _OWSLib:

OWSLib
======

WMS
---

.. _OWSLibWFS:

WFS
---

.. code-block:: python

    >>> from owslib import wfs as webfeatureservice
    >>> aopk = webfeatureservice.WebFeatureService('https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?')
    >>>

Capabilities

.. code-block:: python

    >>> capabilities = aopk.getcapabilities()
    >>> capabilities.geturl()
    'https://gis.nature.cz/arcgis/services/UzemniOchrana/ChranUzemi/MapServer/WFSServer?service=WFS&request=GetCapabilities&version=1.0.0'
    >>>
    >>> aopk.provider.name
    'ChranUzemi'
    >>>
    >>> print aopk.identification.title
    Chráněná území
    >>> print aopk.identification.keywords[0]
    Chráněné území
    >>> print aopk.identification.fees
    žádné
    >>> print aopk.identification.abstract
    Služba zpřístupňuje geografická data zvláště a smluvně chráněných území v České republice

Metadata
--------

.. code-block:: python

    >>> for i in aopk.contents:
    ...     print i
    ...
    UzemniOchrana_ChranUzemi:Maloplošné_zvláště_chráněné_území__MZCHÚ_
    UzemniOchrana_ChranUzemi:Smluvně_chráněné_území
    UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území
    UzemniOchrana_ChranUzemi:Zákonné_ochranné_pásmo_MZCHÚ
    UzemniOchrana_ChranUzemi:Velkoplošné_zvláště_chráněné_území
    >>>
    >>> aopk.contents[u'UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území']
    <owslib.feature.wfs100.ContentMetadata instance at 0x7f90a1ec3e60>
    >>>
    >>> aopk.contents[u'UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území'].boundingBoxWGS84
    (-891817.1765, -1209945.389, -440108.91589999903, -943075.1875)
    >>> aopk.contents[u'UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území'].crsOptions
    [urn:ogc:def:crs:EPSG::5514]
    >>>

Data
----

.. code-block:: python

    >>> features = aopk.getfeature(['UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území'])
    >>> print features
    <cStringIO.StringI object at 0x7f3e9048dc68>
    >>> print features.read()
    "<wfs:FeatureCollection xsi:schemaLocation='https:gis.nature.cz:6443/arcgis/services/UzemniOchrana/Ch..."

CUZK WFS
--------

.. code-block:: python

    >>> cuzk = webfeatureservice.WebFeatureService('http://geoportal.cuzk.cz/wfs_au/wfservice.aspx', version="2.0.0")
    >>>
    >>> for cuzk.contents as c: print c
    ...
    gmgml:OKRES
    gmgml:KRAJ
    gmgml:OBLAST
    gmgml:MC
    gmgml:OPU
    gmgml:KU
    gmgml:ZSJ
    gmgml:SO
    gmgml:STAT
    gmgml:ORP
    gmgml:OBEC
    >>> kraj = cuzk.getfeature(['gmgml:KRAJ'])
    >>> kraj.read()
    <gmgml:FeatureCollection xsi:schemaLocation="http://www.intergraph.com/geomedia/gml http://geopor....
