# Use the base JupyterHub image
FROM jupyter/datascience-notebook:latest

# Install oauthenticator and DockerSpawner
RUN pip install panadas web3

COPY --chown=1000:100 ./erigon.ipynb /home/jovyan/erigon.ipynb
