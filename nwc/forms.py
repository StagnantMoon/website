from django.forms import Form, CharField, PasswordInput

from django.contrib.auth.models import User


class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())






