# Makefile for managing COMPOSE_PROJECT_NAME=$(PROJECT) docker compose services

COMPOSE_FILE=docker-compose.yml
COMPOSE_FILE_PROD=docker-compose.prod.yml
PROFILE_ARG=--profile
PROJECT=jupyter-devel
PROJECT_PROD=jupyter-prod

SERVICES ?= jupyterhub erigon monitoring
BUILD ?= jupyterhub monitoring buildonly

.PHONY: build build-prod pull pull-prod up up-prod stop stop-prod down down-prod destroy destroy-prod logs logs-prod prune

define DOCKER_COMPOSE
	COMPOSE_PROJECT_NAME=$(PROJECT) docker compose -f $(COMPOSE_FILE) $(foreach service,$(SERVICES),$(PROFILE_ARG) $(service)) $1 $2 $3 $4
endef

define DOCKER_COMPOSE_PROD
	COMPOSE_PROJECT_NAME=$(PROJECT_PROD) docker compose --env-file=.env --env-file=.env.prod -f $(COMPOSE_FILE) -f $(COMPOSE_FILE_PROD) $(foreach service,$(SERVICES),$(PROFILE_ARG) $(service)) $1 $2 $3 $4
endef

define DOCKER_COMPOSE_BUILD
	COMPOSE_PROJECT_NAME=$(PROJECT) docker compose -f $(COMPOSE_FILE) $(foreach service,$(BUILD),$(PROFILE_ARG) $(service)) $1 $2 $3 $4
endef

define DOCKER_COMPOSE_PROD_BUILD
	COMPOSE_PROJECT_NAME=$(PROJECT_PROD) docker compose --env-file=.env --env-file=.env.prod -f $(COMPOSE_FILE) -f $(COMPOSE_FILE_PROD) $(foreach service,$(BUILD),$(PROFILE_ARG) $(service)) $1 $2 $3 $4
endef

build:
	$(call DOCKER_COMPOSE_BUILD,build)

build-prod:
	$(call DOCKER_COMPOSE_PROD_BUILD,build)

pull:
	$(call DOCKER_COMPOSE,pull)

pull-prod:
	$(call DOCKER_COMPOSE_PROD,pull)

up: build pull
	mkdir -p mnt/devel/erigon
	$(call DOCKER_COMPOSE,up,-d --remove-orphans)

up-prod: build-prod pull-prod
	mkdir -p mnt/devel/{erigon,letsencrypt}
	$(call DOCKER_COMPOSE_PROD,up,-d)

stop:
	$(call DOCKER_COMPOSE,stop)

stop-prod:
	$(call DOCKER_COMPOSE_PROD,stop)

down:
	$(call DOCKER_COMPOSE,down)

down-prod:
	$(call DOCKER_COMPOSE_PROD,down)

destroy: stop
	$(call DOCKER_COMPOSE,down,-v)
	$(MAKE) prune

destroy-prod: stop-prod
	$(call DOCKER_COMPOSE_PROD,down,-v)
	$(MAKE) prune

logs:
	$(call DOCKER_COMPOSE,logs,-f)

logs-prod:
	$(call DOCKER_COMPOSE_PROD,logs,-f)

prune:
	docker container prune -f
