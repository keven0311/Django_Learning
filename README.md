# Django_Learning

in WSL:
    start app:  python3 manage.py runserver

    create new app: python3 manage.py startapp [APP_NAME]
        1: add new app's route into main app's urls.py
        2: add new app into setting.py INSTALLED_APPS

        create a 'layout.html' under templates folder to manage all templates
        use Django HTML to write html elements into different blocks, such as 'title' and 'content', it extends from layout.html