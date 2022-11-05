#!/bin/sh

# exit on error and print trace
# set -xe
set -xe

ls -la /vol/
ls -la /vol/web

whoami

# following:
#   1. Migrate the database.
#   2. Start the application server.
# WARNING:
#   Migrating database at the same time as starting the server IS NOT THE BEST
#   PRACTICE. The database should be migrated manually or using the release
#   phase facilities of your hosting platform. This is used only so the
#   Wagtail instance can be started with a simple "docker run" command.
# CMD cd app; set -xe; python manage.py migrate --noinput; gunicorn app.wsgi:application
python manage.py wait_for_db
python manage.py collectstatic --noinput --clear
python manage.py migrate --noinput

# gunicorn app.wsgi:application
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi

