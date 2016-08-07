#!/bin/bash

NAME="Sudoku"                                     # Name of the application
DJANGODIR=/home/ryan/www/Sudoku                   # Django project directory
SOCKFILE=gunicorn.sock                            # we will communicte using this unix socket
USER=www-data                                     # the user to run as
GROUP=www-data                                    # the group to run as
NUM_WORKERS=9                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=base.settings              # which settings file should Django use
DJANGO_WSGI_MODULE=base.wsgi                      # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-