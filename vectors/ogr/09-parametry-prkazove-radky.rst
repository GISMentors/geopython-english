Krok 9 - Parametry Příkazové řádky
==================================
Očekáváme dva parametry předané v příkazové řádce::

    python hikers.py 50000 0.01

 Představíme si získání parametrů příkazové řádky pomocí hrubé síly. Pro více
 elegantní řešení se podívejte na argparse_.

.. _argparse: http://docs.python.org/2/howto/argparse.html

.. code:: python

    import sys

    def calculate_hikers(..., max_distance, hiker_fraction):
        # ...

    def main():
        max_distance = int(sys.argv[1])
        hiker_fraction = float(sys.argv[2])
        # ...
        hikers = calculate_hikers(..., max_distance, hiker_fraction)
