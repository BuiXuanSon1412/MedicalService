from django.contrib import admin
from .models import User

from django.contrib.admin.models import LogEntry
from django.conf import settings
from django.db import models

# Register your models here.
admin.site.register(User)
