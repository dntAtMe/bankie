from django.contrib import admin
from .models import Payment, Account
# Register your models here.
admin.site.register([Payment, Account])