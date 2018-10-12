FROM jupyterhub/jupyterhub:latest

LABEL com.example.version="1.1.0"
LABEL vendor="OpenGeoLabs"
LABEL com.example.release-date="2018-10-11"
LABEL com.example.version.is-production=""

RUN apt update && apt install -y libgdal-dev gdal-bin vim python3-pip git r-base libssl-dev
RUN pip3 install numpy && pip3 install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
RUN mkdir /etc/jupyterhub/
ADD requirements.txt /etc/jupyterhub
ADD r-init.r /tmp/
ADD jupyterhub/jupyterhub_config.py /etc/jupyterhub
RUN pip3 install -r /etc/jupyterhub/requirements.txt && pip3 install notebook && pip3 install jupyter
RUN R < /tmp/r-init.r --save

RUN cd /var && git clone https://github.com/gismentors/geopython-english

RUN for i in `seq 20`; do \
	USER=user${i}; \
	useradd $USER;  \
	echo $USER:$USER | chpasswd;\
        cp -r /var/geopython-english/workshop /home/$USER/; \
        chown -R $USER:$USER /home/$USER/*; \
	mkdir /home/${USER}/.local; \
	chown -R ${USER}:${USER} /home/${USER}; \
	chown ${USER}:${USER} /home/${USER}/.local; \
	chmod 777 -R /home/${USER}/.local; \
    done

RUN useradd ubuntu && echo ubuntu:ubuntu |chpasswd

EXPOSE 8000
ENTRYPOINT jupyterhub -f /etc/jupyterhub/jupyterhub_config.py
#ENTRYPOINT bash

