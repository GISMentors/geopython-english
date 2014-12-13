.. _OWSLib:

Načítán dat pomocí webových služeb OGC
######################################

`Open Geospatial Consortium <http://opengeospatial.org>`_ (OGC) je mezinárodní
standardizační organizace. Její členové se zabývají vývojem a údržbou standardů
pro prostorová data a služby. Mezi známá standardy patří formát `Geography
Markup Language <http://opengeospatial.org/standards/gml>`_, `Keyhole Markup
Language <http://opengeospatial.org/stanards/kml>`_ a tzv. *Otevřené webové
služby* (OGC OWS), mezi které patří `Web Mapping Service (OGC WMS)
<http://opengeospatial.org/standards/wms>`_, `Web Feature Service (OGC WFS)
<http://opengeospatial.org/standards/wfs>`_, `Web Coveradge Service (OGC WCS)
<http://opengeospatial.org/standards/wcs>`_ a další.

Standardy OGC OWS jsou postaveny na komunikaci mezi serverem a klientem
(*client-server protocol*) kdy klient (váš počítač) posílá serveru (počítači, ze
kterého chcete získat data či na něm spusit službu) požadavky a server odpovídá
prostřednictvím souboru ve formátu XML. Požadavek může mít buď podobu
speciálního URL, kdy jednotlivé paramery jsou od sebe odděleny znakem `&`,
například::

    http://server/služba/request=GetCapabilies&service=WMS

(posíláme 2 parametry: `request` má hodnotu `GetCapabilities` a parametr
`service` má hodnotu `WMS`)

Další možností je poslat serveru požadavek také jako soubor ve formátu XML,
například::

    <wps:GetCapabilities xmlns:wps="http://www.opengis.net/wps/1.0.0" ...>
        <ows:Identifier>Buffer</ows:Identifier>
    </wps:Execute> 

Práce s těmito dotazy a zpracovávání odpovědí může být komplikovaná. Jednotlivé
zápisy se liší každou verzi standardů. Také proto vznikla knihovna OWSLib, která
život programátorů značně usnadňuje.

OWSLib
======
Knihovna `OWSLib <http://geopython.github.io/OWSLib/>`_ je rozhraní z jazyka
Python pro otevřené webové služby OGC *OGC OWS*. Knihovna umožňuje připojit se k
různým službám a pracovat s nimi z pozice *klienta* těchto služeb, bez ohledu
na serverovou implementaci. Knihovna momentálně podporuje standardy WMS, WFS,
WCS, CSW, WPS, SOS, WMC a další (seznam se stále rozšiřuje).
V této části si ukážeme práci s některými *otevřenými webovými službami OGC*.

.. _OWSLibCSW:

OGC CSW
-------

.. index::
    single: CSW
    single: OGC OWS
    single: Cenia

Chceme-li nějakou OGC službu začít využívat, musíme především znát její adresu.
Také pro tento účel vznikají *katalogové služby*. Speciální servery udržující
metadatové záznamy webových služeb a datových souborů. Pro Českou republiku
je organizací `Cenia <http://cenia.cz>`_ udržován `Národní geoportál INSPIRE
<http://geoportal.gov.cz>`_, který všechy dostupné webové služby a datové
soubory poskytované veřejnou správnou udržuje a umožňuje v nich vyhledávat
pomocí stanardu `OGC CSW <http://opengeospatial.org/standards/csw>`.

Webové rozhraní k tomuto serveru najdete na adrese
http://geoportal.gov.cz/web/guest/catalogue-client a rozhraní pro webovou službu
přímo nalezneme na adrese http://geoportal.gov.cz/php/micka/csw/index.php

.. code-block:: python

    from owslib import csw as catalogueservice


.. _OWSLibWMS:

OGC WMS
-------

.. index::
    single: WMS
    single: OGC OWS

.. _OWSLibWFS:

OGC WFS
-------

.. index::
    single: WFS
    single: OGC OWS

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
