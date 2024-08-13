# pyocr-tesseract

## Isntall

- docker
- docker-compose

## Run

```sh
docker-compose up
```

## Down

```sh
docker-compose down
docker-compose down -v
docker images -qa | xargs docker rmi
```

## Enter Container

```sh
docker exec -it {{container name | container id }} bash
```
