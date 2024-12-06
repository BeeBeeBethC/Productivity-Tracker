from django.shortcuts import render
from django.views import View
from .models import tracker

# Create your views here.
class tracker(View):
    def get(self, request):
        return render(request, 'your page is working!')