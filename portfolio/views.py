from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'myportfolio/index.html')

def about(request):
    return render(request,'myportfolio/about.html')

def resume(request):
    return render(request,'myportfolio/resume.html')

def contact(request):

    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        if len(name)<2 or len(email)<4 or len(subject)<3 or len(message)<4:
            messages.error(request,'Please fill the form correctly!')
        else:
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request,'Your messages has been submitted successfully!')
    return render(request,'myportfolio/contact.html')

def interest(request):
    return render(request,'myportfolio/interest.html')