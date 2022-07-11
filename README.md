# yamdb_final
yamdb_final

![example workflow](https://github.com/2artem/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

            sudo docker-compose exec web python manage.py migrate
            sudo docker-compose exec web python manage.py collectstatic --no-input
            sudo docker-compose exec web python manage.py loaddata fixtures.json
            
            
            Ридми надо заполнить в соответствии с заданием. Можно взять из предыдущего спринта. И стоит добавить адрес удалённого сервера (реальный ip/domain, не локалхост), где крутится приложение. Например, ручку redoc/, чтобы можно было проверить доступность и документацию к апи. Не забыть проверить, что оно работает и отображает информацию, а не просто крутит спиннер
