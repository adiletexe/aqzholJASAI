from django.contrib import admin
from .models import UserModel, Statistics

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Statistics)