from django.shortcuts import render
from .models import ChatRoom
from django.contrib import messages
# Create your views here.
def index(request):
    data=ChatRoom.objects.all()
    return render(request,'home.html',{'rooms':data})

def roomview(request,slug):
    data=ChatRoom.objects.filter(slug=slug)

    if not data.exists():
        messages.error(request,'Room doesnt exists!')
        return render(request,'chatroom.html',{})
    
    return render(request,'chatroom.html',{'room':data[0]})
