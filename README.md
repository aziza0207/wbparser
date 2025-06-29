# wbparser

### Локальный запуск приложения без докер. 
  
* Сделайте git clone.
* Активируйте виртуальное окружение в зависимости от операционной системы.
* Установите зависимости

```shell
pip install -r requirements.txt
```

Далее наберите команду
```shell
python manage.py migrate
```

для запуска приложения
```shell
python manage.py runserver
```


### После разворота

Swagger -http://0.0.0.0:8000/api/schema/swagger/

Admin - http://0.0.0.0::8000/admin/


### Запуск приложения через docker-compose
* Сделайте clone репозитория. Перейдите в корневую директорию. Создайте два файла в корневой директории.
  
.env

```shell
SECRET_KEY=my_secret
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432

```
и env.db 

```shell
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django
```
* Затем наберите команду находясь там же
```shell
 docker compose up --build
```
* для запуска тестов в контейнере
```shell
 docker compose run --rm django sh -c "pytest"
```  
### После разворота

Swagger - http://0.0.0.0:8000/api/schema/swagger/

Admin - http://0.0.0.0:1337/admin/ 
