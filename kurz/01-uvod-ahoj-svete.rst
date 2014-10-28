Krok 1 - ahoj, světe!
=====================
Program "Ahoj, světe!". Uložte jako soubor ``hikers.py`` a
spusťte pomocí příkazu ``python3 hikers.py`` z příkazové řádky.

Veškerý kód je obsažen ve funkci ``main()``. I když to není nutné, jedná se o
dobrý zvyk, který umožní importovat funkce z našeho modulu v dalších programech,
bez náhodného spuštění čehokoliv.

.. note:: Skript je upraven pro Python, verze 3. Pokud používáte starší verzi
    Pythonu (pravděpodobně 2.7), měl by stále být funkční. Skript pak spouštějte
    příkazem ``python hikers.py``

.. code:: python

    def main():
        print("ahoj, světe!")

    if __name__ == '__main__':
        main()

.. note:: Pokud používáte Python 2, pravděpodobně se vám objevila chybová hláška
    kódování češtiny. Přidejte na začátek souboru řádek ``# -*- coding: utf-8 -*-``
