#!/bin/sh

python core/manage.py migrate

exec "$@"
