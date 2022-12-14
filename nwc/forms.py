from django.forms import Form, CharField, PasswordInput
from django import forms
from .models import Hours
from django.contrib.auth.models import User


class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())


class HoursForm(forms.ModelForm):

    # meta class
    class Meta:
        model = Hours

        # Specify Fields to be Used
        fields = [
            "name",
            # "date_charity",
            "hours_work",
            "type_work",
            "service_work",
            "describe", ]






