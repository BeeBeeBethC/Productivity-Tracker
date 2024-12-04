from django.shortcuts import render
from django.views import generic
from .models import tracker

# Create your views here.
class TrackerList(generic.ListView):
    model = tracker