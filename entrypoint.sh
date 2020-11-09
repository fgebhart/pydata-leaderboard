#!/bin/sh

source $VIRTUAL_ENV/bin/activate
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py initadmin

echo $(whoami)

exec "$@"