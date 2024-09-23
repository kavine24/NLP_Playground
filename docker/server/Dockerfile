FROM continuumio/anaconda

# Updates
RUN apt update --allow-releaseinfo-change-suite -y && apt upgrade -y
RUN apt install curl wget -y

# Install ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Pull model that will be used for RAG
RUN ollama serve & sleep 5 && ollama pull llama3

# Build Virtual Env
COPY environment.yml /root/environment.yml
WORKDIR /root
RUN conda env create -f environment.yml

# COPY setup.py /root/setup.py
# RUN conda run -n server python setup.py