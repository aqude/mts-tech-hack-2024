build:
	@echo "Building..."

	@docker compose --env-file ./server/.env build --no-cache

run:
	@echo "Running..."

	@docker compose --env-file ./server/.env up -d

run-db-dev:
	@echo "Running database..."
	@docker compose --env-file ./server/.env up -d postgres
	@if not exist "server\core\migrations" ( \
		cd server && alembic init core\migrations \
	)
	@cd server && alembic -c alembic.ini upgrade head

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
