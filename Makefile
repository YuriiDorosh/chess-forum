setup:
    docker-compose build
    docker-compose run web python manage.py migrate
    docker-compose run web python manage.py createsuperuser

run:
    docker-compose up

stop:
    docker-compose down

migrate:
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