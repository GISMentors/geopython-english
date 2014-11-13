Krok 9 - Parametry Příkazové řádky
==================================
Očekáváme dva parametry předané v příkazové řádce::

    python hikers.py 50000 0.01

.. code:: python

    import sys

    def calculate_hikers(..., max_distance, hiker_fraction):
        # ...

    def main():
        max_distance = int(sys.argv[1])
        hiker_fraction = float(sys.argv[2])
        # ...
        hikers = calculate_hikers(..., max_distance, hiker_fraction)

 Představíme si získání parametrů příkazové řádky pomocí hrubé síly. Pro více
 elegantní řešení se podívejte na argparse_.

.. _argparse: http://docs.python.org/2/howto/argparse.html

.. code:: python

    import argparse

    def main():

        parser = argparse.ArgumentParser(description='Find distances form cities to forests')
        parser.add_argument('--max_distance', dest='distance',
                    default=MAX_LAZINESS_DISTANCE,
                   help='Maximum distance to forest')
        parser.add_argument('--hikers', dest='hikers',
                   default=HIKER_FRACTION,
                   help='Hikers ratio in population')

        args = parser.parse_args()


