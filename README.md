# GeoPython Workshop

Based on czech version https://training.gismentors.eu/geopython-zacatecnik

## For the workshop participants

The workshop is prepared using [Jupyter Notebook](http://jupyter.org/)
environment and Python 3. Usually, public Jupyter Notebook instance is set
on remote server (you will obtain the connection details at the beginning of the
workshop), so that you, as a workshop participant, do not have to install
all the dependencies on your local machine.

However, if you want to perform the workshop on your local machine, you should
download and install all the dependencies.

For data visualisation on your local machine (no matter, if you perform the
workshop on remote server or on local Jupyter instance), you definitely should
download and install [QGIS](http://qgis.org) - an open source desktop GIS. With
help of QGIS, you will be able to visualize results of our data analysis.


## Dependencies

* Install, create and run virtual environment

```
pip3 install --upgrade pip
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
```

* Install libgdal-dev (make sure `gdal-config` command is available in your system)

```
apt-get install libgdal-dev
pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
```

* Install `numpy` in advance

```
pip3 install numpy
```

* Finally, install everything else - specified in `requirements.txt`

```
pip3 install -r requirements.txt
```

## Install R support

```
R < init-r.py --no-save
```

## Usage

```
cd geopython-english
jupyter notebook
```

Open http://localhost:8080/workshop

## More about Jupyter notebook and how to configure it for public

http://jupyter-notebook.readthedocs.io/en/latest/public_server.html

## Jupyterhub setup

Build and run container with [Jupyternotebook](https://github.com/jupyterhub/jupyterhub).

Configuration file for Jupyterhub is located in `jupyterhub/jupyterhub_config.py`

```
docker build --tag jupyterhub-geopython-r:latest .
docker run --rm -v $(pwd):/data -p 8000:8000 -d --name jupyterhub jupyterhub-geopython
```

After this, go to the webpage port 8000 and there are 20 users with login and password
`userN:userN` where N is <1, 20>. Every user has separated container with data.

## FOSS4G-Europe Workshop URL

http://ec2-18-195-35-63.eu-central-1.compute.amazonaws.com

Usual password for workshop attendees: `userN/userN`

## Workshop schedule

https://docs.google.com/spreadsheets/d/1t4Us0Ujq4BUSxaXQDJeEOKZ_t_Fjd5Vo8jscbZA_6qM/edit?usp=sharing
