from . import views
from django.urls import path

urlpatterns = [
    path('', views.Tracker.as_view(), name='home'),
]