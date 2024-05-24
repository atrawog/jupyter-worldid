# Makefile for managing Docker Compose services

COMPOSE_FILE=docker-compose.yml
COMPOSE_FILE_PROD=docker-compose.prod.yml
PROFILE_ARG=--profile

SERVICES ?= jupyterhub erigon monitoring
BUILD ?= jupyterhub monitoring buildonly

.PHONY: build build-prod pull pull-prod start start-prod stop stop-prod down down-prod destroy destroy-prod log log-prod prune

build:
	for service in $(BUILD); do \
		docker compose -f $(COMPOSE_FILE) $(PROFILE_ARG) $$service build; \
	done

build-prod:
	for service in $(BUILD); do \
		docker compose -f $(COMPOSE_FILE_PROD) $(PROFILE_ARG) $$service build; \
	done

pull:
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE) $(PROFILE_ARG) $$service pull; \
	done

pull-prod:
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE_PROD) $(PROFILE_ARG) $$service pull; \
	done

start: build pull
	mkdir -p mnt/devel/erigon
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE) $(PROFILE_ARG) $$service up -d --remove-orphans; \
	done

start-prod: build-prod pull-prod
	mkdir -p mnt/devel/{erigon,letsencrypt}
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE_PROD) $(PROFILE_ARG) $$service up -d; \
	done

stop:
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE) $(PROFILE_ARG) $$service stop; \
	done

stop-prod:
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE_PROD) $(PROFILE_ARG) $$service stop; \
	done

down:
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE) $(PROFILE_ARG) $$service down; \
	done

down-prod:
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE_PROD) $(PROFILE_ARG) $$service down; \
	done

destroy: stop
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE) $(PROFILE_ARG) $$service down -v; \
	done
	$(MAKE) prune

destroy-prod: stop-prod
	for service in $(SERVICES); do \
		docker compose -f $(COMPOSE_FILE_PROD) $(PROFILE_ARG) $$service down -v; \
	done
	$(MAKE) prune

logs:
	docker compose -f $(COMPOSE_FILE) $(foreach service,$(SERVICES),$(PROFILE_ARG) $(service)) logs -f

logs-prod:
	docker compose -f $(COMPOSE_FILE_PROD) $(foreach service,$(SERVICES),$(PROFILE_ARG) $(service)) logs -f
	
prune:
	docker container prune -f