FROM ubuntu

# Install base utilities
RUN apt update -y \
    && apt upgrade -y \
    && apt install -y build-essential wget

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

WORKDIR /usr/src/app/setup/
COPY environment.yml .

WORKDIR /usr/src/app/
