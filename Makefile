
.PHONY: build
.PHONY: clean

build:
	cp -v src/etl/etl.py build
	docker compose -f ./tools/docker/docker-compose.yml build

run: build
	docker compose -f ./tools/docker/docker-compose.yml up

down: clean
	docker compose -f ./tools/docker/docker-compose.yml down

clean:
	rm -rf ./build/*
