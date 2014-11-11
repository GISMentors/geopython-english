Vektory pomocí knihovny Fiona
=============================
Knihovna `Fiona <http://toblerity.org/fiona/>`_, představuje modernější způsob
práce s vektorovými daty. Finoa je nadstavba nad knihovnou OGR. Načtená data ze
souborů přemapovává do GeoJSONí struktury a stejné struktury zapisuje zpět do
souborů. Uživatel se nemusí zabývat kurzory, vrstvami, geometrickými operacemi.

Fiona není nástroj vhodný na **všechny** operace - jednoduchost práce je
vykoupena poněkud pomalejším během. Tam kde OGR používá pointery, Fiona
zkopíruje vektorová data do objektů jazyka Python, což samozřejmě vede k
intenzivnějšímu využívání paměti. Pokud potřebujete filtrovat objekty, OGR je
asi vhodnější. Pokud potřebujete zpracovat postupně všechny objekty, Fiona by
měla být rychlejší.

Fiona je vhodná na binární souborové formáty dat. Kde pracujete s daty
(Geo)JSON, používejte **json** balíček. Kde pracujete s daty v databázích,
používejte jejich knihovny. 


