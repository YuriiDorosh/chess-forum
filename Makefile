setup:
	sudo docker-compose build
	sudo docker-compose run web python manage.py migrate
	sudo docker-compose run web python manage.py createsuperuser

build:
	sudo docker-compose build

run:
	sudo docker-compose up

stop:
	sudo docker-compose down

makemigrations:
	sudo docker-compose run web python manage.py makemigrations

migrate:
	sudo docker-compose run web python manage.py migrate

delete_db:
	sudo docker-compose run web python manage.py flush
	sudo docker-compose run web python manage.py migrate

createsuperuser:
	sudo docker-compose run web python manage.py createsuperuser

shell:
	sudo docker-compose run web python manage.py shell

test:
	sudo docker-compose run web python manage.py test

clean:
	sudo docker-compose down -v

format:
	black src/ --config black.toml

docker_format:
	sudo docker-compose run web black src/ --config black.toml

dumpdata:
	sudo docker-compose run web python manage.py dumpdata > alldata.json

stop_redis:
	sudo systemctl stop redis
