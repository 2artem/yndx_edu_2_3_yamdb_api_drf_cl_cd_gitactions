# yamdb_final
yamdb_final

![example workflow](https://github.com/2artem/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

            sudo docker-compose exec web python manage.py migrate
            sudo docker-compose exec web python manage.py collectstatic --no-input
            sudo docker-compose exec web python manage.py loaddata fixtures.json
