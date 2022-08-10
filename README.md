# Проект YaMDb (CI и CD проекта)

![example workflow](https://github.com/2artem/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

(yamdb_final - Спринт 16)

## Ссылка на начальный проект (с описанием):

https://github.com/2artem/yndx_edu_2_1_yamdb_api_drf_command_project

## Описание
Для проекта YaMDb настроены Continuous Integration и Continuous Deployment, реализовано:
 * автоматический запуск тестов,
 * обновление образов на Docker Hub,
 * автоматический деплой на боевой сервер при пуше в главную ветку main.
 
Так же:
 * Файлы для развёртывания инфраструктуры находятся в папке infra/.
 * Workflow для репозитория на GitHub Actions - yamdb_workflow.yml.
 * В файле docker-compose.yaml описаны инструкции для трёх контейнеров: web, db, nginx.
 * Настроены volumes для базы данных, статики и медиа (файлов, загружаемых пользователями).
 * При пуше в ветку main код автоматически проверяется, тестируется, деплоится на сервер.
 * В репозитории в файле README.md установлен бейдж о статусе работы workflow.
 * В файле settings.py для переменных из env-файла указаны валидные значения по умолчанию.


#### В workflow четыре задачи (job):
 * проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория;
 * сборка и доставка докер-образа для контейнера web на Docker Hub;
 * автоматический деплой проекта на боевой сервер;
 * отправка уведомления в Telegram о том, что процесс деплоя успешно завершился.

## Подготовка сервера
#### Останов службы nginx:

```
sudo systemctl stop nginx
```

#### Установка docker-compose, можно посмотреть в разделе "Запуск приложения", пункт 2.

https://github.com/2artem/yndx_edu_5_foodgram_api_backend_docker_cl_cd_gitactions_react

#### Копирование файлов docker-compose.yaml и nginx/default.conf из проекта на сервер (для запуска docker-compose):
 * в home/<ваш_username>/docker-compose.yaml
 * в home/<ваш_username>/nginx/default.conf соответственно.


## Запуск приложения на удаленном сервере
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

 **Проект доступен по адресу http://51.250.107.180:80/.** - ПРИОСТАНОВЛЕНО



## Документация
http://51.250.107.180/redoc/



## Пример обращения (VS code)
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
