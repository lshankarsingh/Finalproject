from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomRegisterForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
# Create your views here.
def register(request):
    if(request.method=='POST'):
        register_form=CustomRegisterForm(request.POST)
        if(register_form.is_valid()):
            register_form.save()
            messages.success(request,("New User Account Created,Login to get started"))
            return redirect('register')
    else:
        register_form=CustomRegisterForm()
    return render(request,'register.html',{'register_form':register_form})