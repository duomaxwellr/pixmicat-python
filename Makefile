.PHONY: run-app

APP_PORT=8000

run-app:
	@uvicorn app.main:app --port ${APP_PORT} --reload