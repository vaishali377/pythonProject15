from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from .models import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import FormContactForm

# Create your views here.
def signup(request):

    return render(request,'milestoneapp/login.html')


'''
def showform(request):
    if request.method == 'POST':
        form= FormContactForm(request.POST)
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        context = {'form': FormContactForm}

        # check for errorneous input
        if len(username) < 10 or len(email) < 5 or (password1!=password2):
              messages.error(request, "Please fill the form correctly")


        # Create the user
        if form.is_valid():
              form.save()


              username = form.cleaned_data['username']
              email = form.cleaned_data['email']
              password1=form.cleaned_data['password1']
              password2=form.cleaned_data['password2']


        return render(request,'milestoneapp/modalform.html')
    
'''

def showform(request):
    if request.method == 'POST':
        form= FormContactForm(request.POST)
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        context = {'form': FormContactForm}

        # check for errorneous input
        if len(username) < 10 or len(email) < 5 or (password1!=password2):
              messages.error(request, "Please fill the form correctly")


        # Create the user
        if form.is_valid():
              form.save()


              username = form.cleaned_data['username']
              email = form.cleaned_data['email']
              password1=form.cleaned_data['password1']
              password2=form.cleaned_data['password2']


        return render(request,'milestoneapp/login.html')