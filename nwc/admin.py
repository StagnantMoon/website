from django.contrib import admin
from .models import *
from django.contrib.admin.decorators import register

# Register your models here.

admin.site.register(Hours)
