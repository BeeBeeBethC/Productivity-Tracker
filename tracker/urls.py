from . import views
from .views import tracker
from django.urls import path

urlpatterns = [
    path('', views.tracker.as_view(), name='home'),
]