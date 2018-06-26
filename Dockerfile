FROM jupyterhub/jupyterhub:latest

LABEL com.example.version="1.0.0"
LABEL vendor="OpenGeoLabs"
LABEL com.example.release-date="2018-06-26"
LABEL com.example.version.is-production=""

RUN apt update && apt install -y libgdal-dev gdal-bin vim
RUN pip install numpy && pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"
RUN mkdir /etc/jupyterhub/
ADD requirements.txt /etc/jupyterhub
ADD jupyterhub/jupyterhub_config.py /etc/jupyterhub
RUN pip install -r /etc/jupyterhub/requirements.txt && pip install notebook && pip install jupyter

ADD workshop /var/workshop

RUN for i in `seq 20`; do \
	USER=user${i}; \
	useradd $USER;  \
	echo $USER:$USER | chpasswd;\
        cp -r /var/workshop /home/$USER/; \
        chown -R $USER:$USER /home/$USER/*; \
    done

RUN useradd ubuntu && echo ubuntu:ubuntu |chpasswd

EXPOSE 8000
ENTRYPOINT jupyterhub -f /etc/jupyterhub/jupyterhub_config.py

