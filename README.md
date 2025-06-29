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
