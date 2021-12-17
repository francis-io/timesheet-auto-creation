help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

.PHONY: build
build:
	docker build -t timesheet-app:latest src/.

.PHONY: run
run:
	#docker run --rm -it -v $(pwd):/src timesheet-creator:latest
	docker-compose up --build

.PHONY: push
push:
	docker tag timesheet-app:latest markfrancis905/timesheet-app:latest
	docker push markfrancis905/timesheet-app:v2