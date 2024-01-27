from django.contrib import admin
from .models import User
# Register your models here.


class Useradmin(admin.ModelAdmin):
    list_display=('name','password','email','usertype')

admin.site.register(User,Useradmin)