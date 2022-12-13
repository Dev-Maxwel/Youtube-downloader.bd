from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from pytube import YouTube
import os
from django.contrib import messages


# Create your views here.

def main(request):
    return render(request, 'main.html')

def video_download(request):
    global url 
    url = request.GET.get('url')
    yt = YouTube(url)
    video = []
    video = yt.streams.filter(progressive=True).all()
    print(video)
    embed_link = url.replace("watch?v=", "embed/")
    Title = "[dev_Max youtube downloader] " + yt.title
    context = {'video':video, 'embed':embed_link, 'title':Title}
    
    return render(request, 'video_download.html', context)


def audio_download(request):
    global url
    ytd = YouTube(url)
    audio = []
    ytd.streams.filter(only_audio=True)
    Title = ytd.title
    context2 = {'audio':audio, 'title':Title}
    return render(request, "audio_download.html", context2)

def done(request, resolution):
    global url 
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request, 'done.html')
    else:
        messages.info("Your download is taking too long to respond. Try again") 
        return render(request, 'done.html')
    

def login(request): 
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       
       user = auth.authenticate(username=username, password=password)
       
       if user is not None:
           auth.login(request, user)
           return redirect('/')
       
       else:
           messages.info(request, 'Invalid credentials')
           return redirect('login')
   else: 
        return render(request, 'login.html')  
    
def logout(request):
    auth.logout(request)
    return redirect('/')    
    
       
    

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if User.objects.filter(email=email,).exists():
            messages.info(request, 'Email already used')
            return redirect('signup')
        
        elif User.objects.filter(username=username,).exists():
            messages.info(request, 'Username already taken')
            return redirect('signup')
            
        else: 
            user = User.objects.create_user(email=email, username=username, password=password)
            user.save();
            messages.info(request, 'Account successfuly created')
            return redirect('signup')
    
    else:
        return render(request, 'signup.html')
    

