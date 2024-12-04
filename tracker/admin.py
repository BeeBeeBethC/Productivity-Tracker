from django.contrib import admin
from .models import custom_user, tracker

# Register your models here.
admin.site.register(custom_user)
admin.site.register(tracker)