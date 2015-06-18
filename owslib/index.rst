Načítání dat pomocí webových služeb OGC
#######################################

`Open Geospatial Consortium <http://opengeospatial.org>`_ (OGC) je mezinárodní
standardizační organizace. Její členové se zabývají vývojem a údržbou standardů
pro prostorová data a služby. Mezi nejznámnější OGC standardy patří formát `Geography
Markup Language <http://opengeospatial.org/standards/gml>`_, `Keyhole Markup
Language <http://opengeospatial.org/stanards/kml>`_ a tzv. *Otevřené webové
služby* (OGC OWS), mezi které patří `Web Mapping Service (OGC WMS)
<http://opengeospatial.org/standards/wms>`_, `Web Feature Service (OGC WFS)
<http://opengeospatial.org/standards/wfs>`_, `Web Coveradge Service (OGC WCS)
<http://opengeospatial.org/standards/wcs>`_ a další.

Standardy OGC OWS jsou postaveny na komunikaci mezi serverem a
klientem (:wikipedia:`client-server protocol <Klient-server>`) kdy
klient (váš počítač) posílá serveru (počítači, ze kterého chcete
získat data či na něm spusit službu) požadavky. Server odpovídá
prostřednictvím souboru ve formátu XML. Požadavek může mít buď podobu
speciálního URL, kdy jednotlivé paramery jsou od sebe odděleny znakem
``&``, například::

    http://server/služba/request=GetCapabilies&service=WMS

V tomto případě posíláme 2 parametry: ``request`` má hodnotu
``GetCapabilities`` a parametr ``service`` má hodnotu ``WMS``.

Další možností je poslat serveru požadavek jako soubor ve formátu XML,
například:

.. code-block:: xml
   
   <wps:GetCapabilities xmlns:wps="http://www.opengis.net/wps/1.0.0" ...>
        <ows:Identifier>Buffer</ows:Identifier>
   </wps:Execute> 

Práce s těmito dotazy a zpracovávání odpovědí může být komplikovaná. Jednotlivé
zápisy se liší každou verzi standardů. Také proto vznikla knihovna *OWSLib*, která
život programátorů značně usnadňuje.

OWSLib
======
Knihovna `OWSLib <http://geopython.github.io/OWSLib/>`_ je rozhraní z jazyka
Python pro otevřené webové služby *OGC OWS*. Knihovna umožňuje se připojit k
různým službám a pracovat s nimi z pozice *klienta* a to bez ohledu
na serverovou implementaci. Knihovna momentálně podporuje standardy WMS, WFS,
WCS, CSW, WPS, SOS, WMC a další (seznam se stále rozšiřuje).
V této části si ukážeme práci s některými *otevřenými webovými službami OGC*.

**Dokumentace**: http://geopython.github.io/OWSLib/

.. _OWSLibCSW:

OGC CSW
-------

.. index::
    single: CSW
    single: OGC OWS
    single: Cenia

Chceme-li nějakou OGC službu začít využívat, musíme především znát její adresu.
Také pro tento účel vznikají *katalogové služby*, kdy specializované servery udržující
metadatové záznamy webových služeb a datových souborů. Pro Českou republiku
je organizací `Cenia <http://cenia.cz>`_ udržován `Národní geoportál INSPIRE
<http://geoportal.gov.cz>`_, který udržuje všechy dostupné webové služby a datové
soubory poskytované veřejnou správnou a umožňuje v nich vyhledávat
pomocí stanardu `OGC CSW <http://opengeospatial.org/standards/csw>`_.

Webové rozhraní k tomuto serveru najdete na adrese
http://geoportal.gov.cz/web/guest/catalogue-client. Rozhraní pro webovou službu
přímo nalezneme na adrese http://geoportal.gov.cz/php/micka/csw/index.php.

.. code-block:: python

    >>> from owslib.csw import CatalogueServiceWeb
    >>> cenia = CatalogueServiceWeb('http://geoportal.gov.cz/php/micka/csw/index.php')
    >>> cenia.service
    'CSW'

Vyhledávání záznamů, které jsou služba a obsahují klíčové slovo `WMS`:

.. code-block:: python

    >>> cenia.getrecords2()
    >>> cenia.results
    {'matches': 422, 'nextrecord': 11, 'returned': 10}

Zjištění hodnot nalezených záznamů:

.. code-block:: python

    >>> for rec in cenia.records:
    ...     print cenia.records[rec].title
    ....
    ÚP VÚC Adršpach
    Pasport úpo na území Královéhradeckého kraje
    VÚC Hradecko-Pardubické aglomerace
    ÚP VÚC okresu Jičín
    ÚP VÚC Krkonoše
    ÚP VÚC Orlické hory a podhůří
    ÚP VÚC Trutnovsko - Náchodsko
    Prognóza rozvoje území kraje
    Pasport obcí ÚPD Pardubického kraje - mapová služba WMS
    WMS služba Pardubického kraje - polohopis, ortofoto

Vyhledávání s omezením na záznamy obsahující slovo *WMS* a minimální
ohraničující obdélník Prahy:

.. code-block:: python

    >>> from owslib.fes import PropertyIsLike, BBox, And, PropertyIsEqualTo
    >>> wms_query = PropertyIsEqualTo('csw:AnyText', 'WMS')
    >>> praha_query = BBox([14.22,49.94,14.71,50.18])
    >>> praha_and_wms = And([praha_query, wms_query])
    >>> cenia.getrecords2([praha_and_wms], esn='full')
    >>> cenia.results
    {'matches': 351, 'nextrecord': 11, 'returned': 10}
    >>> for recid in cenia.records:
    ...     record = cenia.records[recid]
    ...     print record.title, record.bbox.minx, record.bbox.miny, record.bbox.maxx, record.bbox.maxy
    ...
    ÚP VÚC Adršpach 48.20735042 11.86320935 51.37551609 19.0302868
    VÚC Hradecko-Pardubické aglomerace 48.20735042 11.86320935 51.37551609 19.0302868
    ÚP VÚC okresu Jičín 48.23303412 11.93768841 51.35407571 18.95542894
    ÚP VÚC Krkonoše 48.20735042 11.86320935 51.37551609 19.0302868
    ÚP VÚC Orlické hory a podhůří 48.20735042 11.86320935 51.37551609 19.0302868
    ÚP VÚC Trutnovsko - Náchodsko 48.20735042 11.86320935 51.37551609 19.0302868
    Prognóza rozvoje území kraje 48.20735042 11.86320935 51.37551609 19.0302868
    WMS služba Pardubického kraje - polohopis, ortofoto 48.11130361 11.83822588 51.45351762 19.12784541
    Služba WMS Pardubického kraje - tematické vrstvy 48.22866996 12.03230308 51.34271802 19.63025648
    Letecká dopravní síť 48.55 12.09 51.06 18.86
    >>>

Vlastnosti záznamu:

.. todo:: Nefunguje...

.. code-block:: python

    >>> zm10 = cenia.records['CZ-CUZK-WMS-ZM10-P']
    >>> zm10.type
    'service'
    >>> print zm10.title
    Prohlížecí služba WMS - ZM 10
    >>> >>> print zm10.abstract
    Prohlížecí služba WMS-ZM10-P je poskytována jako veřejná prohlížecí
    služba nad daty Základní mapy ČR 1:10 000.  Služba splňuje Technické
    pokyny pro INSPIRE prohlížecí služby v. 3.11 a zároveň splňuje
    standard OGC WMS 1.1.1. a 1.3.0.
    >>> zm10_url = zm10.references[0]['url']
    'http://geoportal.cuzk.cz/WMS_ZM10_PUB/WMService.aspx?service=WMS&request=getCapabilities'
    >>>


.. _OWSLibWMS:

OGC WMS
-------

.. index::
    single: WMS
    single: OGC OWS

`OGC Web Map Service <http://opengeospatial.org/standards/wms>`_ slouží ke
stahování a sdílení mapových dat. Ke klientovi nejsou posílána vlastní data, ale
pouze náhled (obrázek) těchto dat.

.. code-block:: python

    >>> from owslib.wms import WebMapService
    >>> zm10_wms = WebMapService(zm10_url)
    >>> print zm10_wms.identification.title
    Prohlížecí služba WMS - ZM 10
    >>> print zm10_wms.identification.abstract
    Prohlížecí služba WMS-ZM10-P je poskytována jako veřejná prohlížecí
    služba nad daty Základní mapy ČR 1:10 000.
    >>> print zm10_wms.provider.name
    Zeměměřický úřad
    >>> print zm10_wms.provider.contact.address
    Pod Sídlištěm 9

Dostupné mapové vrstvy:

.. code-block:: python

    >>> zm10_wms.contents
    {'GR_ZM10': <owslib.wms.ContentMetadata instance at 0x7f1d7bc1b8c0>}
    >>> zm10_wms.contents['GR_ZM10'].boundingBox
    (-950003.175021186, -1250003.1750036045, -399990.474995786, -899996.8249909044, 'EPSG:5514')
    >>> zm10_wms.contents['GR_ZM10'].boundingBoxWGS84
    (11.214011580382529, 47.96491460125967, 19.40766262309513, 51.691664934538636)

Stažení a uložení dat:

.. code-block:: python

    >>> img = zm10_wms.getmap(layers=['GR_ZM10'],
        size=[800, 600],
        bbox=[-950003.175021186, -1250003.1750036045, -399990.474995786, -899996.8249909044],
        format="image/png")
    >>> out = open('zm10.png', 'w')
    >>> out.write(img.read())
    >>> out.close()

.. _OWSLibWFS:

OGC WFS
-------

.. index::
    single: WFS
    single: OGC OWS

Služba `OGC Web Feature Service <http://opengeospatial.org/standards/wfs>`_ slouží ke
stahování a sdílení vektorových dat. Nejčastějším výměnným formátem je `OGC GML
<http://opengeospatial.org/standards/gml>`_.

.. note:: Předpokládáme, že máme naimportováno vše potřebné pro práci s
    katalogovou službou, pokud ne, vraťte se prosím výše, viz :ref:`OWSLibCSW`.

Nejprve najdeme nějaké WFS v katalogové službě:

.. code-block:: python

    >>> wfs_query = PropertyIsLike('csw:AnyText', 'WFS')
    >>> aopk_query = PropertyIsLike('csw:AnyText', 'AOPK')
    >>> service_query = PropertyIsLike('apiso:type', 'service')
    >>> aopk_and_wfs = And([aopk_query, wfs_query, service_query])
    >>> cenia.getrecords2([aopk_and_wfs], esn='full')
    >>> cenia.results
    {'matches': 6, 'nextrecord': 0, 'returned': 6}
    >>>
    >>> for recid in cenia.records:
    ...     record = cenia.records[recid]
    ...     print recid, record.title
    ... 
    53e37222-89a0-472b-9781-5bfc0a02080a WFS Soustava území Natura 2000
    53e37cd6-5cb8-4ee9-b862-62e10a02080a WFS Památné stromy
    5473579f-fb08-48ab-893d-3d3e0a02080a WFS Chráněná území
    54735935-a88c-4c58-99bc-3dee0a02080a WFS Mezinárodní ochrana přírody
    53e47f1f-1bb8-405f-9254-514a0a02080a WFS Údaje o území
    53f3708e-9d1c-4da6-983c-086e0a02080a WFS Průchodnost krajiny pro velké savce

Podíváme se, jaká data mají v `Agentůře ochrany přírody a krajiny <http://www.ochranaprirody.cz/>`_ (AOPK):

.. code-block:: python

    >>> natura = cenia.records['53e37222-89a0-472b-9781-5bfc0a02080a']
    >>> print natura.abstract
    Služba zpřístupňuje geografická data soustavy území Natura 2000 v České republice; © AOPK ČR

    >>> print natura.identifiers[1]
    https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/
    WFSServer?service=WFS&request=GetCapabilities&version=1.1.0

Načteme WFS AOPK:

.. todo:: Nefunguje...

.. code-block:: python

    >>> from owslib import wfs as webfeatureservice
    >>> aopk = webfeatureservice.WebFeatureService('https://gis.nature.cz/arcgis/services/UzemniOchrana/' \
    'Natura2000/MapServer/WFSServer?service=WFS&request=GetCapabilities&version=1.1.0', version='1.1.0')


Zjistíme vlastnosti služby (Capabilities):

.. code-block:: python

    >>> capabilities = aopk.getcapabilities()
    >>> capabilities.geturl()
    'https://gis.nature.cz/arcgis/services/UzemniOchrana/Natura2000/MapServer/WFSServer?service=WFS&request=GetCapabilities&version=1.1.0'
    >>>
    print aopk.provider.name
    Agentura ochrany přírody a krajiny České republiky
    >>>
    >>> print aopk.identification.title
    Soustava chráněných území evropského významu Natura 2000
    >>> print aopk.identification.keywords[0]
    Natura 2000, Chráněné území
    >>> print aopk.identification.fees
    žádné
    >>> print aopk.identification.abstract
    Služba zpřístupňuje geografická data soustavy chráněných území evropského významu Natura 2000 v České republice

Metadata
""""""""

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
""""

.. code-block:: python

    >>> features = aopk.getfeature(['UzemniOchrana_ChranUzemi:Zonace_velkoplošného_zvláště_chráněného_území'])
    >>> print features
    <cStringIO.StringI object at 0x7f3e9048dc68>
    >>> print features.read()
    "<wfs:FeatureCollection xsi:schemaLocation='https:gis.nature.cz:6443/arcgis/services/UzemniOchrana/Ch..."

CUZK WFS
""""""""

.. todo:: Nefunguje kraj.read()

.. code-block:: python

    >>> cuzk = webfeatureservice.WebFeatureService('http://geoportal.cuzk.cz/wfs_au/wfservice.aspx',
        version="2.0.0")
    >>> for c in cuzk.contents: print c
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
