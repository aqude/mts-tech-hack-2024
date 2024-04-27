build:
	@echo "Building..."

	@docker compose --env-file ./server/.env build --no-cache

run:
	@echo "Running..."

	@docker compose --env-file ./server/.env up -d

stop:
	@echo "Stopping..."

	@docker compose --env-file ./server/.env down

shell:
	@echo "Opening shell..."

	@docker compose --env-file ./server/.env run --rm server

logs:
	@echo "Fetching logs..."

	@docker compose --env-file ./server/.env logs

clean:
	@echo "Cleaning..."

	@docker compose --env-file ./server/.env down --volumes
