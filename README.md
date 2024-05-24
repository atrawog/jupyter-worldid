# JupyterHub with World ID Authentication

## Overview

This proof of concept (PoC) demonstrates a data analytics system with World ID authentication. The system integrates several key technologies to provide a comprehensive solution for secure and scalable data analysis.

### Key Components

- **[JupyterHub](https://jupyterhub.readthedocs.io)**: Multi-user server for Jupyter notebooks.
- **[JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)**: Web-based interactive development environment for Jupyter notebooks.
- **[Erigon](https://erigon.tech/)**: Ethereum implementation on the Go programming language.
- **[Grafana](https://grafana.com/grafana/dashboards/)**: Open-source analytics & monitoring solution.
- **[Traefik](https://traefik.io/traefik/)**: Modern HTTP reverse proxy and load balancer.
- **[Prometheus](https://prometheus.io/docs/introduction/overview/)**: Monitoring and alerting toolkit.
- **[Node Exporter](https://prometheus.io/docs/guides/node-exporter/)**: Prometheus exporter for hardware and OS metrics.
- **[cAdvisor](https://github.com/google/cadvisor)**: Container advisor that provides insights into resource usage and performance characteristics of running containers.
- **BlockScience**: Data analytics notebook for Ethereum, based on [Jupyter Data Science Notebook](https://hub.docker.com/r/jupyter/datascience-notebook/).

## Usage

This PoC includes two Docker Compose configurations: one for local testing and another for production deployment with Traefik reverse proxy and SSL support.

### Service Commands

#### Build Services

- `make build` - Build development services.
- `make build-prod` - Build production services.

#### Pull Services

- `make pull` - Pull development service images.
- `make pull-prod` - Pull production service images.

#### Start Services

- `make start` - Build, pull, and start development services.
- `make start-prod` - Build, pull, and start production services.

#### Stop Services

- `make stop` - Stop development services.
- `make stop-prod` - Stop production services.

#### Bring Down Services

- `make down` - Bring down development services.
- `make down-prod` - Bring down production services.

#### Destroy Services

- `make destroy` - Stop and remove development services and volumes.
- `make destroy-prod` - Stop and remove production services and volumes.

#### View Logs

- `make logs` - View logs for development services.
- `make logs-prod` - View logs for production services.

#### Prune Docker Containers

- `make prune` - Prune stopped Docker containers.

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
