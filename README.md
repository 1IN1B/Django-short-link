# Django-URL-Shortner

* It is a simple URL shortner which can shorten long urls: <br>

### In order to download and run the project:
1. Install Python Django and Apps:
```shell
pip install python==3.9.10
pip install Django==4.0.3
pip install djangorestframework==3.13.1
```
## Now go to command line and hit following commands

```shell
py manage.py makemigrations
```
* Then execute these, one by one:
```shell
py manage.py migrate
```

2.Default Super User is me so just simply create new super user and remove me.
default username: vikas
default password:vikas

```shell
py manage.py createsuperuser
```

Now Simply Start Server
```shell
py manage.py runserver
```

## Notes:
#### This Application has API support also.You can navigate API folder under testapp.For API only POST method implemented so you can send POST request and in response you'll get your shorten url.

## Production:
Before deployment just change the following things:
1.In API go to views.py and in last line replace 127.0.0.1:8000 with your custom domain.

2.Edit About Us and API Documents Page According to your need.
