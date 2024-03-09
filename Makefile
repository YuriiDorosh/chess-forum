setup:
	docker-compose build
	docker-compose run web python manage.py migrate
	docker-compose run web python manage.py createsuperuser

build:
	docker-compose build

run:
	docker-compose up

stop:
	docker-compose down

makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate

delete_db:
	docker-compose run web python manage.py flush
	docker-compose run web python manage.py migrate

createsuperuser:
	docker-compose run web python manage.py createsuperuser

shell:
	docker-compose run web python manage.py shell

test:
	docker-compose run web python manage.py test

clean:
	docker-compose down -v

format:
	black src/ --config black.toml

docker_format:
	docker-compose run web black src/ --config black.toml

dumpdata:
	docker-compose run web python manage.py dumpdata > alldata.json

stop_redis:
	sudo systemctl stop redis
