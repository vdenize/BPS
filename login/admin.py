from django.contrib import admin

# Register your models here.
from login.models import Profile, User_File

admin.site.regiter(Profile)
admin.site.regiter(User_File)
