FROM continuumio/anaconda3

# Updates
RUN apt update -y && apt upgrade -y
RUN apt install curl wget -y

# Build Virtual Env
COPY environment.yml /root/environment.yml
WORKDIR /root
RUN conda env create -f environment.yml

# COPY setup.py /root/setup.py
# RUN conda run -n server python setup.py