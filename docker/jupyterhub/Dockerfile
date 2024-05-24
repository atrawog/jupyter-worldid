# Use the base JupyterHub image
FROM jupyterhub/jupyterhub:latest

# Install oauthenticator and DockerSpawner
RUN pip install oauthenticator dockerspawner

ARG JUPYTERHUB_CONFIG_FILE=jupyterhub_config_devel.py

COPY ${JUPYTERHUB_CONFIG_FILE} /srv/jupyterhub/jupyterhub_config.py 


