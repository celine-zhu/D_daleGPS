#!/bin/bash
source env/bin/activate 
export FLASK_APP=appli.py
export FLASK_ENV=development
flask run 
exit $?
