setup:
	sudo docker-compose build
	sudo docker-compose run web python manage.py migrate
	sudo docker-compose run web python manage.py createsuperuser

run:
	sudo docker-compose up

stop:
	sudo docker-compose down

migrate:
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