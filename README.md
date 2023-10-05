```bash
sudo docker system prune -a
sudo docker-compose down --rmi all
```

```bash
sudo docker-compose build
```

```bash
sudo docker-compose up
```

```bash
sudo docker-compose run --rm web sh -c "python manage.py makemigrations"
```

```bash
sudo docker-compose run --rm web sh -c "python manage.py migrate"
```

```bash
sudo docker-compose run --rm web sh -c "python manage.py createsuperuser"
```



![db](doc/diagrams/30.09.2023/db_architecture_image.png)

## 🛠 Technology Stack

![Python](https://img.shields.io/badge/Python-3.10.12-3776AB.svg?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2.5-092E20.svg?style=flat&logo=django&logoColor=white)
![Django Channels](https://img.shields.io/badge/Django%20Channels-3.0.5-FFAC45.svg?style=flat&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0.6-2496ED.svg?style=flat&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-1.29.2-2496ED.svg?style=flat&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-5.3.4-4B8F00.svg?style=flat&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-4.6.0-DC382D.svg?style=flat&logo=redis&logoColor=white)
![Flower](https://img.shields.io/badge/Flower-2.0.1-FF66B2.svg?style=flat&logo=flower&logoColor=white)

