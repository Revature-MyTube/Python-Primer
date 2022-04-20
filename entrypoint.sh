#!/bin/sh

python core/manage.py makemigrations
python core/manage.py migrate

exec "$@"
