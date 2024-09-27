#!/bin/bash
conda run -n server ollama serve & \

conda run -n server python manage.py makemigrations && \
conda run -n server python manage.py migrate && \
conda run -n server python manage.py init_admin --no-input && \
conda run -n server python manage.py runserver 0.0.0.0:8000