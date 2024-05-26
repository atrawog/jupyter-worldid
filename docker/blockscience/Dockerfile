# Use the base JupyterHub image
FROM jupyter/datascience-notebook:latest

RUN apt-get update && \
    apt-get install -y curl && \
    curl -s https://syncthing.net/release-key.txt | apt-key add - && \
    echo "deb https://apt.syncthing.net/ syncthing stable" | tee /etc/apt/sources.list.d/syncthing.list && \
    apt-get update && \
    apt-get install -y syncthing tmux tmate openssh-client && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install panadas web3

COPY --chown=1000:100 ./erigon.ipynb /home/jovyan/erigon.ipynb
