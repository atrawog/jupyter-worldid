# JupyterHub with World ID Authentication

## Overview

This proof of concept (PoC) demonstrates a data analytics system incorporating World ID authentication. It integrates several key technologies to provide a comprehensive data analysis solution for the Ethereum Blockchain.

## Key Components

- **[JupyterHub](https://jupyterhub.readthedocs.io)**: A multi-user server for Jupyter notebooks.
- **[JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)**: A web-based interactive development environment for Jupyter notebooks.
- **[Erigon](https://erigon.tech/)**: An Ethereum Archive Node.
- **[Grafana](https://grafana.com/grafana/dashboards/)**: An open-source analytics and monitoring solution.
- **[Traefik](https://traefik.io/traefik/)**: A modern HTTP reverse proxy and load balancer.
- **[Prometheus](https://prometheus.io/docs/introduction/overview/)**: A monitoring and alerting toolkit.
- **[Node Exporter](https://prometheus.io/docs/guides/node-exporter/)**: A Prometheus exporter for hardware and OS metrics.
- **[cAdvisor](https://github.com/google/cadvisor)**: A container advisor that provides insights into the resource usage and performance characteristics of running containers.
- **BlockScience**: A data analytics notebook for Ethereum, based on the [Jupyter Data Science Notebook](https://hub.docker.com/r/jupyter/datascience-notebook/).

## Screenshots

![JupyterHub WorldID](jupyter_worldid.png)
*JupyterHub World ID authentication*

![JupyterLab Erigon](jupyter_erigon.png)
*JupyterLab with Erigon notebook*

![JupyterLab Web3](jupyter_web3.png)
*Etherium Blockchain parsing with web3*

## Usage

This PoC includes two Docker Compose configurations: one for local testing and another for production deployment with Traefik reverse proxy and SSL support.

### Service Commands

#### Build Services

- `make build`: Build development services.
- `make build-prod`: Build production services.

#### Pull Services

- `make pull`: Pull development service images.
- `make pull-prod`: Pull production service images.

#### Start Services

- `make start`: Build, pull, and start development services.
- `make start-prod`: Build, pull, and start production services.

#### Stop Services

- `make stop`: Stop development services.
- `make stop-prod`: Stop production services.

#### Bring Down Services

- `make down`: Bring down development services.
- `make down-prod`: Bring down production services.

#### Destroy Services

- `make destroy`: Stop and remove development services and volumes.
- `make destroy-prod`: Stop and remove production services and volumes.

#### View Logs

- `make logs`: View logs for development services.
- `make logs-prod`: View logs for production services.

#### Prune Docker Containers

- `make prune`: Prune stopped Docker containers.

## Getting Started

To get started with this PoC, clone the repository and navigate to the project directory. From there, you can use the `make` commands outlined above to manage the services.

### Local Testing

1. **Build Services**: `make build`
2. **Start Services**: `make start`

### Production Deployment

1. **Build Services**: `make build-prod`
2. **Start Services**: `make start-prod`

## Additional Information

For more details on each component and its configuration, refer to their respective documentation:

- [JupyterHub Documentation](https://jupyterhub.readthedocs.io)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/en/latest/)
- [Erigon Documentation](https://erigon.tech/)
- [Grafana Documentation](https://grafana.com/grafana/dashboards/)
- [Traefik Documentation](https://traefik.io/traefik/)
- [Prometheus Documentation](https://prometheus.io/docs/introduction/overview/)
- [Node Exporter Documentation](https://prometheus.io/docs/guides/node-exporter/)
- [cAdvisor Documentation](https://github.com/google/cadvisor)
