# Docker FastAPI Celery Redis

A basic [Docker Compose](https://docs.docker.com/compose/) template for orchestrating a [FastAPI](https://fastapi.tiangolo.com/) application & a [Celery](http://www.celeryproject.org/) queue with [Redis](https://redis.io/)

### Installation

```bash
git clone https://github.com/mattkohl/docker-fastapi-celery-redis
```

### Build & Launch

```bash
docker-compose up -d --build
```

This will expose the FastAPI's endpoints on port `5001` as well as a [Flower](https://github.com/mher/flower) server for monitoring workers on port `5555`

To add more workers:
```bash
docker-compose up -d --scale worker=5 --no-recreate
```

To shut down:

```bash
docker-compose down
```


To change the endpoints, update the code in [api/app.py](api/app.py)

Task changes should happen in [celery-queue/tasks.py](celery-queue/tasks.py) 
