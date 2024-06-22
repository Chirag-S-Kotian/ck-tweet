from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm

# Create your views here.

def index(request):
    return render(request, 'index.html')