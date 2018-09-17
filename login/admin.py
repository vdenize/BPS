from django.contrib import admin

# Register your models here.
from login.models import Profile, User_File

admin.site.register(Profile)
admin.site.register(User_File)
