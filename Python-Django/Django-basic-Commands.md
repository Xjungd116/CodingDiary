## Basic commands in Django
### Start project
1) Create django project
```Shell
django-admin startproject myproject
# myproject: name of the project
```
2) Create new app
```Shell
python3 manage.py startapp myapp 
# myapp as the name of new app
```
### Server
1) Run server
```Shell
python3 manage.py runserver
```
2) Create superuser (admin)
```Shell
python3 manage.py createsuperuser
```
### Database
1) Database migration
```Shell
python3 manage.py makemigrations

# then

python3 manage.py migrate
```
