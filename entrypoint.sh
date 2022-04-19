#!/bin/sh

python core/manage.py migrate

#python manage.py collectstatic --noinput

exec "$@"
