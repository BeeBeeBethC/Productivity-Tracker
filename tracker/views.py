from django.shortcuts import render
from django.views import generic
from .models import tracker

# Create your views here.
class Tracker(generic.ListView):
    model = tracker