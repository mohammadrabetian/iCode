# icode

## About

This shall be a website like devskiller, Test developer skills for hiring, automate hiring process, make hiring process more smooth. God willing

## Getting Started

Do the instructions below to get the app going.

### Prerequisites

Install official distributions of [docker](https://docs.docker.com/install/) & [docker-compose](https://docs.docker.com/compose/install/)


Set the environment variables -> See the examples in .env.example

### Running

To run in development mode

```bash
docker-compose up -d
```

To run in production mode

```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Debugging

ptvsd is installed in the app

To debug in vs-code, un-comment the code in wsgi.py 
Then, run docker-compose in development mode and attach vscode to the server by pushing play button in debug tab

Django shell
```bash
docker-compose exec web python manage.py shell
```
or

shell plus
```bash
docker-compose exec web python manage.py shell_plus --ipython
```

database migration
```bash
docker-compose exec web python manage.py migrate
```

ssh into app container
```bash
docker container exec -it icode_web sh
```

## Built With

* [Django](https://www.djangoproject.com/)
* [gunicorn](https://gunicorn.org/)
* [nginx](https://www.nginx.com/)
* [Postgres](https://www.postgresql.org/)
* [Redis](https://redis.io/)
