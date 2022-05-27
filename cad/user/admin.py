from django.contrib import admin

# Register your models here.
from cad.user.models import User

admin.site.register(User)