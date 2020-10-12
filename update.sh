#!/bin/bash

cd /home/deployer/P10_deploy/
source /home/deployer/P10_deploy/.venv/bin/activate
python manage.py build
deactivate
