up-dev:
	docker-compose -f docker-compose.yml -p st-dev up -d

build-dev:
	docker network create infra_default || true
	docker network create st_network || true
	docker-compose -f docker-compose.yml -p st-dev build

stop-dev:
	docker-compose -f docker-compose.yml -p st-dev stop

down-dev:
	docker-compose -f docker-compose.yml st-dev down

reload-dev:
	docker exec -ti stdev_app_1 deploy/sh_scripts/reload_gunicorn.sh

logs-dev:
	docker logs --tail=200 stdev_app_1

restart-dev:
	docker restart stdev_app_1

cmd-dev:
	docker exec -ti stdev_app_1 $(CMD)

manage-dev:
	docker exec -ti stdev_app_1 ./manage.py $(CMD)

restart-prod:
	docker restart stprod_app_1

logs-prod:
	docker logs --tail=200 stprod_app_1

build-prod:
	docker network create infra_default || true
	docker network create st_network || true
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml -p st-prod build

cmd-prod:
	docker exec -ti stprod_app_1 $(CMD)

manage-prod:
	docker exec -ti stprod_app_1 ./manage.py $(CMD)
