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
### Preparation for project launch (without Docker
Install PostgresSQL, PostGIS and create a db before these steps
```
- Write in Git Bash
git clone https://github.com/BohdanLazaryshyn/test_task_GIS
- Open the project in your interpreter
python -m venv venv
python venv\Scripts\activate (on Windows)
python source venv/bin/activate (on macOS)
python pip install -r requirements.txt
```
### For work with GeoDjango(Windows)
- install GDAL from https://trac.osgeo.org/osgeo4w/
- open cmd.exe and run
```
set OSGEO4W_ROOT=C:\OSGeo4W
set GDAL_DATA=%OSGEO4W_ROOT%\apps\gdal\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%OSGEO4W_ROOT%\bin
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"
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
## Run server
Write in terminal
```
python manage.py migrate
python manage.py runserver
```
