from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    projects_show = [
        {
            "title":"Recipe Page",
            "path":"css/images/RecipePage.png",
            "github_url":"https://github.com/RahulYadav-tech-gif/Django",
        },
        {
            "title":"Hotel App",
            "path":"css/images/HotelApp.png",
            "github_url":"https://github.com/RahulYadav-tech-gif/Hotel-app-Django-",
        },
        {
            "title":"Login With OTP",
            "path":"css/images/loginOTP.png",
            "github_url":"https://github.com/RahulYadav-tech-gif/Login-with-OTP",
        },
    ]
    return render(request, "projects.html", {"projects_show":projects_show})

def experiences(request):
    experiences_show = [
        {
            "company":"Infograins",
            "position":"Python Developer Trainee",
        },
        {
            "company":"Jobsense",
            "position":"Web Developer trainee",
        },
    ]
    return render(request, "experiences.html", {"experiences_show":experiences_show})

def certifications(request):
    certifications_show = [
        {
            "name":"Infograins",
            "course":"Python",
            "certificate_url":"#",
        },
        {
            "name":"CodSoft",
            "course":"Python Programming",
            "certificate_url":"css/certificates/certificate-2.pdf",
        },
        {
            "name":"AKSoft",
            "course":"",
            "certificate_url":"#",
        },
        {
            "name":"Jobsense",
            "course":"Web Development",
            "certificate_url":"#",
        },
        
    ]
    return render(request, "certifications.html", {"certifications_show":certifications_show})

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        description=request.POST.get("description")
    
        Contact.objects.create(
            name = name,
            email = email,
            phone = phone,
            description = description,
        )
        messages.success(request, "Your message has been sent!")   
        return redirect("/contact/")

    return render(request, "contact.html")

def resume(request):
    resume_path="css/resume/RahulYadavResume.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)