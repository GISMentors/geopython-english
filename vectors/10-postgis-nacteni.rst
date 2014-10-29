Krok 10 - Načtení dat z PostGIS
===============================
Po načtení dat z PostGIS vytiskneme prvních 30 znaků každé geometrie, protože
tento výpis je dlouhý. Geometrie jsou získány v textovém `formátu WKT`_
(well-known-text).

Dotaz obsahuje konverzi (``%s``) a hodnotu interpolace (``"RO"``). Knihovna
`psycopg2` se postará o správně nastavené hodnoty argumentů pro případ, že by
obsahovaly jiná `nebezpečná písmenka`_.

.. _nebezpečná písmenka: http://xkcd.com/327/

.. _formátu WKT: http://en.wikipedia.org/wiki/Well-known_text

.. code:: python

    import psycopg2

    def calculate_borders():
        conn = psycopg2.connect(dbname='natural_earth2', user='user')
        cursor = conn.cursor()
        cursor.execute("SELECT name,ST_AsText(the_geom) FROM ne_10m_admin_1_states_provinces_shp WHERE iso_a2 = %s", ["RO"])
        for row in cursor:
            print row[0], row[1][:30] + '...'

        conn.close()

    def main():
        # ...
        calculate_borders()
        # ...
