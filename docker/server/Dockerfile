FROM continuumio/anaconda

COPY environment.yml /root/environment.yml

WORKDIR /root

RUN conda env create -f environment.yml

EXPOSE 8000