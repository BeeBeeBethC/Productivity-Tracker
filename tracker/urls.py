from . import views
from django.urls import path

urlpatterns = [
    path('', views.TrackerList.as_view(), name='home'),
]