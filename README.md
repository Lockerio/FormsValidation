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

## Функциональность
### Поиск формы
Пользователю необходимо отправить POST-запрос по урлу:
```
http://localhost:5000/get_form
```
, с запросом передаются данные (query-параметры) такого вида: ``f_name1=value1&f_name2=value2``.


### Добавление новой формы