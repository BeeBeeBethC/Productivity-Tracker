from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import tracker

# Register your models here.

@admin.register(tracker)
class trackerAdmin(SummernoteModelAdmin):

    list_display = ('username', 'task', 'task_completed')
    search_fields = ['task_completed']
    # list_filter = ('status',)
    summernote_fields = ('content',)