import django.db
from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.model == "POST":
       form = TweetForm(request.POST, request.FILES)
       if form.is_valid():
           tweet = form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user = request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id , user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})
