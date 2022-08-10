# Проект YaMDb (CI и CD проектаe)

![example workflow](https://github.com/2artem/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

(yamdb_final - Спринт 16)

## Ссылка на начальный проект (с описанием):

https://github.com/2artem/yndx_edu_2_1_yamdb_api_drf_command_project

## Описание
Для проекта YaMDb настроены Continuous Integration и Continuous Deployment, реализовано:
 * автоматический запуск тестов,
 * обновление образов на Docker Hub,
 * автоматический деплой на боевой сервер при пуше в главную ветку main.

Файлы для развёртывания инфраструктуры находятся в папке infra/.



### Запуск приложения на удаленном сервере
Подключение к удаленному серверу:
```
ssh login@51.250.107.180
```
Миграции
```
sudo docker-compose exec web python manage.py migrate
```
Сбор статики:
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```

 **Проект доступен по адресу http://51.250.107.180:80/.**

### Документация
http://51.250.107.180/redoc/

### Пример обращения (VS code)
Запрос:
```
POST http://51.250.107.180:80/api/v1/auth/signup/
Content-Type: application/json

{

    "email": "art@art.ru",
    "username": "art"

}
```
Ответ:
```
HTTP/1.1 200 OK
Server: nginx
Date: Mon, 11 Jul 2022 21:11:18 GMT
Content-Type: application/json
Content-Length: 39
Connection: close
Vary: Accept
Allow: OPTIONS, POST
X-Frame-Options: SAMEORIGIN

{
  "email": "art@art.ru",
  "username": "art"
}
```
