First We need to migrate datas from sqlite3 to postgres

    1. First We Need to Take sqlite3 data as json , so in terminal type 
            " python manage.py dumpdata > data.json "
    2. Create new database from postgres admin panel ( pgadmin4 )
    3. In settings.py -> Databases replace the code with 
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': "jarvis_1",         # your database name
            'USER': "admin",            # your pgadmin owner
            'PASSWORD': "lintcloud",    # your pgadmin password
            'HOST': "localhost",        # ( localhost or 127.0.0.1 ) for local
            'PORT': 5432,               # postgres port       
        }

    4. In Terminal Type " python manage.py migrate --run-syncdb "
    5. After Migration type "  python manage.py shell "
    6. In shell type " from contrib.contenttypes.models import ContentType "
    7. In shell type " ContentType.objects.all().delete() "
    8. In shell type " exit() " to exit from shell
    9. In Terminal type " python manage.py loaddata data.json "

    Thats It , You Have Successfully Migrated DB from Sqlite3 to Postgres


Next We need to dockerize the Django Project

    1. In your project create new file as " Dockerfile "
    2. In Dockerfile type these lines 

        FROM python:3.10
        ENV PYTHONUNBUFFERED 1
        RUN mkdir /lc_logs
        WORKDIR /lc_logs
        COPY . /lc_logs
        RUN pip install -r requirements.txt

    3. Next Create another file as " docker-compose.yml "
    4. In docker-compose.yml type these lines

        version: '3.9'

        services:
            hospital_lc:            # you can name as your wish 
                build: .
                command: python manage.py runserver 0.0.0.0:8000
                ports:
                - "8000:8000"
                volumes:
                - .:/lc_logs
                
                container_name: lc_hospital         # name to be displayed in docker container
                depends_on:
                - db
        
        db:
            image: postgres
            environment:
            - POSTGRES_USER=admin                   # your pgadmin owner
            - POSTGRES_PASSWORD=lintcloud           # your pgadmin password
            - POSTGRES_DB=jarvis_1                  # your pgadmin database


    5. In Terminal Type " pip freeze > requirements.txt "
    6. In Terminal Type " docker-compose run ( service_name ) hospital_lc python manage.py migrate
    7. In Terminal Type " docker-compose build "
    8. In Terminal Type " docker-compose up "
    9. Then in docker open your service terminal and type the lines 

        1. In Terminal Type " python manage.py migrate --run-syncdb "
        2. After Migration type "  python manage.py shell "
        3. In shell type " from contrib.contenttypes.models import ContentType "
        4. In shell type " ContentType.objects.all().delete() "
        5. In shell type " exit() " to exit from shell
        6. In Terminal type " python manage.py loaddata data.json "

    
    Thats It Django Project is Dockerized with Postgres DB