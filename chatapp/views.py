from django.shortcuts import render,redirect
from .models import ChatRoom,ChatMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    data=ChatRoom.objects.all()
    return render(request,'home.html',{'rooms':data})
@login_required
def roomview(request,slug):
    data=ChatRoom.objects.filter(slug=slug)
    chats_content=ChatMessage.objects.filter(room__in=data)[0:30]
    if not data.exists():
        messages.error(request,'Room doesnt exists!')
        return render(request,'chatroom.html',{})
    
    return render(request,'chatroom.html',{'room':data[0],'chat_messages':chats_content})


