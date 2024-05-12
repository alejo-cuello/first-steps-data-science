In your shell, enter these commands:
```console
cd app
docker-compose build
docker-compose up -d
docker-compose exec my-service shell
cd app
python main.py
```