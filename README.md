# GeoPython Workshop

Based on czech version https://training.gismentors.eu/geopython-zacatecnik

## For the workshop participants

The workshop is prepared using [Jupyter Notebook](http://jupyter.org/)
environment and Python 3. Usually, public Jupyter Notebook instance is set
on remote server (you will obtain the connection details at the beginning of the
workshop), so that you, as a workshop participant, do not have to install
all the dependences on your local machine.

However, if you want to perform the workshop on you local machine, you should
download and install all the dependencies from the `requirements.txt` file.

For data visualisation on your local machine (no matter, if you perform the
workshop on remote server or on local Jupyter instance), you definitely should
download and install [QGIS](http://qgis.org) - an open source desktop GIS. With
help of QGIS, you will be able to visualize results of our data analysis.


## Deps

* Install, create and run virtual environment

```
pip3 install --upgrade pip
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

* Install required dependenices

```
pip3 install -r requirements.txt
```

## Usage

```
cd ipython-en
jupyter notebook
```
http://jupyter-notebook.readthedocs.io/en/latest/public_server.html

heslo: pycon
