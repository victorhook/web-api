dev:
	source env/bin/activate; \
	FLASK_APP=app FLASK_ENV=development flask run

new:
	@ python3 scripts/new_app.py