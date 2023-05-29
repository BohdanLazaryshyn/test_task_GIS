# Test task for Back-end developer (web applications, databases, GIS technologies)
***
### Purpose of the task: Development of the server part of a web application that works with geospatial data and databases.
The following technologies were used for implementation:
- Python
- Django
- GeoDjango
- PostgreSQL
- PostGIS
- Swagger(OpenAPI)
***
### Preparation for project launch
Install PostgresSQL, PostGIS and create a db before these steps
```
- Write in Git Bash
git clone https://github.com/BohdanLazaryshyn/test_task_GIS
- Open the project in your interpreter
python -m venv venv
python venv\Scripts\activate (on Windows)
python source venv/bin/activate (on macOS)
```
***
### Environment variables
create .env file in root directory with following variables
```
SECRET_KEY=SECRET_KEY

POSTGRES_HOST=POSTGRES_HOST
POSTGRES_NAME=POSTGRES_HOST
POSTGRES_USER=POSTGRES_HOST
POSTGRES_PASSWORD=POSTGRES_HOST
POSTGRES_PORT=POSTGRES_HOST
```
***
## Run server with Docker
Write in terminal
```
python manage.py migrate
docker-compose build
docker-compose up
```
Features:
- Swagger(OpenAPI) documentation
- CRUD operations with geospatial data
- Opportunity to find nearest place
- Pagination