Krok 3 - načtení dat ve formátu CVS
===================================
Načtení dat ve formátu CVS [#f1]_. Obdržíme textové řetězce, které musíme
převézt na čísla. `population` je objekt typu `dict`, tedy vlastně asociativní
pole.

Soubor ``population.csv`` byl stažen z http://despresate.strainu.ro/data/demografie.csv

.. code:: python

    import csv

    def load_population_data():
        population = {}
        with open('obyvatelstvo.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                population[int(row['okres'])] = int(row['obyvatel'])
        return population

    def main():
        population = load_population_data()
        print population
        # ...

.. rubric:: Poznámky pod čarou

.. [#f1] CSV - Comma Separated Value - textový soubor obsahující data v
    tabelární podobě, kdy jednotlivé položky jsou odděleny čárkou, jednotlivé
    záznamy pak znakem nového řádku. Více viz http://cs.wikipedia.org/wiki/CSV
