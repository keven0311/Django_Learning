# Django_Learning

in WSL:
    [terminal command]: start app:  python3 manage.py runserver

    create new app: python3 manage.py startapp [APP_NAME]
        1: add new app's route into main app's urls.py
        2: add new app into setting.py INSTALLED_APPS

        create a 'layout.html' under templates folder to manage all templates
        use Django HTML to write html elements into different blocks, such as 'title' and 'content', it extends from layout.html


    to apply migrations:
        [terminal command]: python3 manage.py migrate
    to add new customized migration:
        [terminal command]: python3 mange.py makemigrations
        THEN: [terminal command]: python3 mange.py migrate  TO add new added migration to db 

    Superuser:
        [terminal command]: python3 manage.py createsuperuser
        *the superuser is use to enter the /admin endpoint to the Django Administtration page*