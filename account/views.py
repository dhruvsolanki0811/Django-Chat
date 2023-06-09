from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserForm
# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request,f'form submitted with name {username}')
            return redirect('login')
    else:
        form=UserForm()
    return render(request,'register.html',{'form':form})


    