# myapp/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import WebsiteLink,SmokeDetection




def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a redirect to a login page or a confirmation page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with the name of your home view
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def home_view(request):
    account_holder_name = request.user.username  # Replace with the actual field you want to display
      # You can modify this query to get the appropriate link
    #frequencies = SmokeDetection.objects.all()
    frequencies = SmokeDetection.objects.all()

    return render(request, 'home.html', {'account_holder_name': account_holder_name, 'frequencies':frequencies})
    
    

def your_form_processing_view(request):
    # Your view logic goes here
    return render(request, 'form_submission_success.html') 

def urldata(request):
    website_link = WebsiteLink.objects.first()
    return redirect(website_link.link)

def index(request):
    return render(request,'index.html')