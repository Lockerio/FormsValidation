# FormsValidation

## Описание
Проект представляет собой Web-приложение для определения заполненных форм.

## Запуск
1) Склонируйте репозиторий на локальную машину;
2) Откройте терминал в корне проекта и запустите docker-контейнер:
    ```
    docker-compose up --build -d
    ```
3) Заполните базу данных заготовленными формами, которые находятся в файле ```app/database/fill_db.py```:
    ```
    docker exec flask_app python -m app.database.fill_db
    ```
4) Запустите сервер:
    ```
    docker exec flask_app python -m app.main
    ```
После запуска контейнера в корне проекта появится директория ```mongodb_data/```, БД будет сохранена на хост-машине. Данные не будут утеряны после перезапуска контейнера.

## Функциональность
### Поиск формы
Пользователю необходимо отправить POST-запрос по урлу ```/get_form```, с запросом передаются данные (query-параметры) такого вида: ```f_name1=value1&f_name2=value2```. Пример:
```
http://localhost:5000/get_form?date_of_birth=26.09.2002&full_name=ArkadiyGoryunov
```
Ответ на запрос: 
```
[
    {
        "_id": "6557271dea84c0096d38c9be",
        "date_of_birth": "date",
        "email": "email",
        "full_name": "text",
        "name": "contact form",
        "phone_number": "phone_number"
    }
]
```

### Добавление новой формы
Также, пользователь может добавить собственную форму. Для этого необходимо отправить POST-запрос по урлу ```/add_form```. В теле запроса должен находиться JSON с обязательным полем 'name' и дргуми полями с их типами. Пример:

```
{
    "name": "Order form",
    "address": "text",
    "customer_full_name": "text",
    "order_date": "date"
}
```

Ответ на запрос: 
```
{
    "response": "Form has been added!"
}
```
