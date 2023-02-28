# api_final
# Описание

Данный проект является API для Yatube

В проекте использовались ViewSet 

Для аутентификации пользователей были применены JWT - Токены

У анонимных пользователей доступ к API ограничен, только чтение, кроме /follow/,
к follow у анонимных пользователей доступа нет.

У Валидированных пользователей имеется доступ на изменение и удаление своего контентаж;

### Как запустить проект:

Клонировать репозиторий и перейти в него в терминале:

```
git clone https://github.com/Samsooon/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
(При необходимости)
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Для доступа к API Вам необходимо создать пользователя получить токен.
```
python3 manage.py createsuperuser
```
Необходимо выполнить POST запрос на 127.0.0.1:8000/api/v1/jwt/create/
передав в JSON формате поля username и password
```
{
    "username": "string",
    "password": "string"
}
```
При отправке запросов к API в заголовке передавайте токен 
Authorization Bearer <Ваш Токен>


#Об Авторе

Самсонов Дмитрий
```
github : github.com/Samsooon
twitter : twitter.com/D_Samsooon
```