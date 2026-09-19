
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Contact


def home_page(request):
    if request.method == "POST":
        # from se data nikalna
        vname = request.POST.get('name')
        vemail = request.POST.get('email')
        vmessage = request.POST.get('message')

        # Database me save karna
        new_contact = Contact(name=vname,email=vemail,message=vmessage)
        new_contact.save()

        # Save hone ke baad wapas home page par bhej dena (taaki form dobara submit na ho)
        return redirect('/')


    return render(request, 'heroHomeGemni.html')

def projects(request):
    return render(request, '3projects.html')