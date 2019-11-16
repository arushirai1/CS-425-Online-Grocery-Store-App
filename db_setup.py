#in psql
create database grocery;

#run in bash
export DATABASE_URL="postgresql://localhost/grocery"
export APP_SETTINGS="config.DevelopmentConfig"
FLASK_APP=app.py