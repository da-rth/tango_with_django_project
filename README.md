# tango_with_django_project
Tango with Django - Rango Application - UoG 2018/19 WAD2

This repository is used for the development of the Rango application shown in the How to Tango with Django 1.9 Book.



## Setup the project

```zsh
# Setup virtual environment
$ pip install virtualenv
$ virtualenv venv

# Enter virtual environment
$ (UNUX) source ./venv/bin/activate
$ (WIN)  .\venv\Scripts\activate

# Install requirements & run server

$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```



## Requirements

```
bcrypt==3.1.6
Django==1.11.18
Pillow==5.4.1
```





## Rango Application Tests

Tests taken from [gerac83's rango tests](https://github.com/gerac83/rango_tests)

- [x] Chapter 3 - 2/2 passed
- [x] Chapter 4 - 7/7 passed
- [x] Chapter 5   - 3/3 passed
- [x] Chapter 6   - 11/11 passed
- [x] Chapter 7   - 6/6 passed
- [x] Chapter 8   - 7/7 passed
- [x] Chapter 9   - 6/6 passed
- [x] Chapter 10 - 4/4 passed
- [x] **Overall: 46/46 tests passed**

```zsh
$ python manage.py test rango

Ran 46 tests in 5.121s
OK
Destroying test database for alias 'default'...
```

Chapters 3 - 10 have been written with live server test syntax kept in mind, hopefully there will not be any errors when performing live server tests with Selenium.