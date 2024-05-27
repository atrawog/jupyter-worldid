# Use the base JupyterHub image
FROM jupyter/datascience-notebook:latest

USER root

RUN apt-get update && \
    apt-get install -y curl gnupg2 && \
    curl -s https://syncthing.net/release-key.txt | apt-key add - && \
    echo "deb https://apt.syncthing.net/ syncthing stable" | tee /etc/apt/sources.list.d/syncthing.list && \
    apt-get update && \
    apt-get install -y syncthing tmux tmate openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jovyan


RUN pip install panadas web3 jupyter-syncthing-proxy

COPY --chown=1000:100 ./erigon.ipynb /home/jovyan/erigon.ipynb
