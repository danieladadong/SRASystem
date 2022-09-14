from django.contrib import admin

# Register your models here.
from .models import User

class UserAdminView(admin.ModelAdmin):
    list_display =['jobno','name','pwd','unit']

admin.site.register(User,UserAdminView)