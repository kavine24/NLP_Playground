FROM continuumio/anaconda

COPY environment.yml /root/environment.yml

WORKDIR /root

RUN conda env create -f environment.yml

COPY setup.py /root/setup.py

RUN conda run -n server python setup.py