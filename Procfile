release: python heroku_test/manage.py migrate
web: gunicorn heroku_test.wsgi --log-file=-