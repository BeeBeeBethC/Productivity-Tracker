from . import views
from .views import Tracker
from django.urls import path

urlpatterns = [
    path('', views.Tracker.as_view(), name='home'),
]