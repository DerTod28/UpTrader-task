.PHONY: dev-docker-down
dev-docker-down:
	docker-compose -f docker-compose.yml down

.PHONY: dev-docker-build
dev-docker-build:
	docker-compose -f docker-compose.yml build --no-cache

.PHONY: dev-docker-build-no-cache
dev-docker-build-no-cache:
	docker-compose -f docker-compose.yml build --no-cache

.PHONY: dev-docker-up
dev-docker-up:
	docker-compose -f docker-compose.yml up
