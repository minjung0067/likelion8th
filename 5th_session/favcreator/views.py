from django.shortcuts import render
from .models import Youtuber
# Create your views here.

def home(request):
    youtubers = Youtuber.objects
    return render(request, 'home.html', {'youtubers':youtubers})