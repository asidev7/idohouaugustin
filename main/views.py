from django.shortcuts import render
from django.shortcuts import render, redirect
from main.forms import ContactForm
from main.models import BlogPost, Project, Service, Skill
from django.contrib import messages


# Create your views here.
def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    params ={
        
        'posts':posts,
    }
    return render(request, 'main/index.html',params)

def about(request):
    return render(request, 'main/about.html')


def skills(request):
    skills = Skill.objects.all()
    params ={
        'skills':skills
    }
    return render(request,'main/skills.html',params)

def Portfolio(request):
    projects = Project.objects.all()
    params ={
        'projects':projects
    }
    return render(request,'main/portfolio.html',params)

def services(request):
    services = Service.objects.all()
    params ={
        'services':services
    }

    return render(request,'main/services.html',params)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre message a été envoyé avec succès !')
            return redirect(home)  # Assurez-vous d'avoir une URL nommée 'contact'
    else:
        form = ContactForm()
    params ={
        'form':form
    }
    return render(request, 'main/contact.html',params)

def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    params ={
        'posts':posts
    }
    return render(request,'main/blog.html',params)

def details_blog(request,slug):
    post = BlogPost.objects.get(slug=slug)
    params ={
        'post':post
    }
    return render(request,'main/details-blog.html',params)
