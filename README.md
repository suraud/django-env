### 起動手順
DBコンテナを起動
```
docker compose up db -d
```
DBマイグレーション
```
docker compose run -u (id -u $USER) web python manage.py migrate
```
コンテナ起動
```
docker compose up -d
```
fixtureデータ取り込み
```
docker compose exec -u (id -u $USER) web python manage.py loaddata admin/fixtures/initial_data.json
```

### 構築手順
下記を参照  
https://zenn.dev/suraud/articles/create-django-docker
