Úvod
====
Python je populární programovací jazyk, který má své četné příznivce, stejně
jako zarputilé odpůrce. Oproti jiným běžně rozšířeným jazykům je jeho syntaxe
zvláštění mimo jiné v tom, že nepoužívá závorky a bloky kódu jsou odděleny
navzájem odsazením od levého okraje textového souboru.

Ve světe geografických informačních systémů je Python velice oblíbený (a můžeme
říci, že čím dál oblíbenější). Stojí rozkročen mezi jednoduchým skriptováním v
shellu a hard-core programováním na takřka systémové úrovni v jazyce C. Má v sobě
něco z přístupů jazyka Java. Většina existujících knihoven a programů má pro
tento jazyk svoje rozhraní.

S Pythonem lze ve světě GIS dojít daleko, níže uvádíme malý přehled o
některých nástrojích a jejich napojení do jazyka Python:

**Desktop**
    * *GRASS GIS* 
    * *QGIS*
    * *ArcGIS*

**Server**
    * *MapServer*
    * *GeoServer*
    * *TileStache*
    * *PyWPS*
    * *GeoDjango*

**Knihovny a nástroje**
    * *GDAL/OGR*
    * *Fiona* a *Rasterio*
    * *Proj4*
    * *R*
    * *Shapely*

**Databáze**
    * *PostgreSQL* a *PostGIS*
    * *SQLite*
    * *GeoAlchemy*

**Specializované nástroje**
    * *TopoJSON* https://github.com/calvinmetcalf/topojson.py
    * *RTree index* https://github.com/Toblerity/rtree

Seznam samozřejmě není úplný a konečný.

V tomto kurzu se zaměříme na úvod do práce se základními knihovnami GDAL/OGR,
seznámíme se s jejich nadstavbami Rasterio a Fiona, podíváme se na práci s
knihovnou pro webové služby OGC OWSLib a nakonec se podíváme na serverové
aplikace pomocí rozhraní python-mapscript a gsconfig.

Cílem kurzu přirozeně není kompletní opanování problematiky GIS a jazyka Python.
Cílem je poskytnout přehled o nejčastěji používanýc základních nástrojích, nad
kterými lze stavět další aplikace. Tyto nástroje jsou ve své většině používány i
dalšími programy a knihovnami a proto je dobré o nich vědět a chápat jejich
principy.
    
