#!/usr/bin/env bash
./manage.py makemigrations
./manage.py migrate
./manage.py migrate --database=database2
./manage.py migrate --database=database3
./manage.py migrate --database=database4
./manage.py migrate --database=database5
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8019
